
import gspread
import pandas as pd
from gspread_dataframe import get_as_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import time

from scraper import scrape_smartbuy

from src.utils import GOOGLE_SHEETS, KNOWN_BRANDS, GoogleSheet

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
    if not isinstance(name, str) or not name.strip(): return pd.Series([None, None, None], index=['Brand', 'Model', 'Extra'])
    name_upper = name.strip().upper()
    extra_from_parens = None
    if '(' in name and ')' in name:
        start_idx, end_idx = name.find('('), name.find(')')
        extra_from_parens = name[start_idx + 1:end_idx].strip()
        name = name[:start_idx].strip()
    found_brand = next((brand for brand in known_brands if name.upper().startswith(brand.upper())), None)
    if not found_brand: return pd.Series([None, None, extra_from_parens], index=['Brand', 'Model', 'Extra'])
    rest_of_string = name[len(found_brand):].strip()
    parts = rest_of_string.split()
    model = parts[0] if parts else None
    extra = " ".join(parts[1:]) if len(parts) > 1 else None
    if extra_from_parens: extra = f"{extra} {extra_from_parens}".strip() if extra else extra_from_parens
    return pd.Series([found_brand.title(), model, extra], index=['Brand', 'Model', 'Extra'])

def process_frames():
    try:
        print("Authenticating with Google Sheets...")
        client = authenticate()
        
        print("Fetching data from 'Rame' sheet...")
        df = get_data_from_google_sheet("Raport_Produse", "Rame", client)
        
        print("Parsing product names...")
        sorted_brands = sorted(KNOWN_BRANDS, key=len, reverse=True)
        df[['Brand', 'Model', 'Extra']] = df["Denumire"].apply(lambda name: parse_product_info_v2(name, sorted_brands))

        df_to_process = df[df['Brand'].notna()].copy()

        if df_to_process.empty:
            print("No products with known brands found.")
            return

        print(f"\n--- Starting robust scrape for {len(df_to_process)} products ---")
        
        results = []
        for index, row in df_to_process.iterrows():
            query = f"{row['Brand']} {row['Model']}"
            if pd.notna(row.get('Extra')):
                query += f" {row['Extra']}"
            
            print(f"Scraping: {query}")
            info = scrape_smartbuy(query)
            results.append(info)

        results_df = pd.DataFrame(results, index=df_to_process.index)
        df_enriched = df_to_process.join(results_df.rename(columns={'Error': 'ScraperError'}))

        print("\n--- SCRAPING COMPLETE ---")
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 140)
        pd.set_option('display.max_rows', 100)

        display_cols = ['Denumire', 'Brand', 'Color', 'Gender', 'Price', 'ScraperError']
        print(df_enriched[display_cols])

    except Exception as e:
        print(f"\nA critical error occurred: {e}")
        print("Please check your internet connection, credentials, and file paths.")

if __name__ == "__main__":
    process_frames()