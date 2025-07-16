import gspread
import pandas as pd
from gspread_dataframe import get_as_dataframe
from oauth2client.service_account import ServiceAccountCredentials

from utils import GOOGLE_SHEETS, KNOWN_BRANDS, GoogleSheet

def get_sheet_url(sheet: GoogleSheet, page_name: str) -> str:
    gid = sheet.pages[page_name]
    return f"https://docs.google.com/spreadsheets/d/{sheet.id}/edit#gid={gid}"


def authenticate():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    return client


def get_data_from_google_sheet(sheet_name: str, page_name: str, client):
    sheet_meta = GOOGLE_SHEETS[sheet_name]
    url = get_sheet_url(sheet_meta, page_name)
    sheet = client.open_by_url(url)
    worksheet = sheet.worksheet(page_name)
    df = get_as_dataframe(worksheet, evaluate_formulas=True, dtype=str, header=1)
    df.dropna(how="all", inplace=True)
    
    return df


def parse_product_info_v2(name: str, known_brands: list):
    if not isinstance(name, str) or not name.strip():
        return pd.Series([None, None, None], index=['Brand', 'Model', 'Extra'])
    name_upper = name.strip().upper()
    extra_from_parens = None
    if '(' in name and ')' in name:
        start_idx = name.find('(')
        end_idx = name.find(')')
        extra_from_parens = name[start_idx + 1:end_idx].strip()
        name = name[:start_idx].strip()
        name_upper = name.upper()
    found_brand = None
    for brand in known_brands:
        if name_upper.startswith(brand.upper()):
            found_brand = brand
            break
    if not found_brand:
        return pd.Series([None, None, extra_from_parens], index=['Brand', 'Model', 'Extra'])
    rest_of_string = name[len(found_brand):].strip()
    parts = rest_of_string.split()
    model = parts[0] if parts else None
    extra = " ".join(parts[1:]) if len(parts) > 1 else None
    if extra_from_parens:
        extra = f"{extra} {extra_from_parens}".strip() if extra else extra_from_parens
    return pd.Series([found_brand.title(), model, extra], index=['Brand', 'Model', 'Extra'])


def parse_data_for_frames(client):
    df = get_data_from_google_sheet("Raport_Produse", "Rame", client)
    df = df[df["Denumire"].notna()]
    initial_row_count = len(df)
    
    sorted_brands = sorted(KNOWN_BRANDS, key=len, reverse=True)
    parsed_df = df["Denumire"].apply(lambda name: parse_product_info_v2(name, sorted_brands))
    df[['Brand', 'Model', 'Extra']] = parsed_df

    df_filtered = df[df['Brand'].notna()].copy()
    
    print("--- Data Processing Report ---")
    print(f"Total rows processed: {initial_row_count}")
    print(f"Rows with a known brand (included): {len(df_filtered)}")
    print(f"Rows with an unknown brand (excluded): {initial_row_count - len(df_filtered)}\n")

    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 120) 
    pd.set_option('display.max_rows', 100) 

    print("--- Verification: Correctly Parsed Products ---")
    if not df_filtered.empty:
        print(df_filtered[['Denumire', 'Brand', 'Model', 'Extra']])
    else:
        print("No products matched the brands in your KNOWN_BRANDS list.")


if __name__ == "__main__":
    client = authenticate()
    parse_data_for_frames(client)