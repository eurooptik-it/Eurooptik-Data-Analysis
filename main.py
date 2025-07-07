import gspread
import pandas as pd
from gspread_dataframe import get_as_dataframe
from oauth2client.service_account import ServiceAccountCredentials

from utils import GOOGLE_SHEETS, GoogleSheet


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
    df = get_as_dataframe(worksheet, evaluate_formulas=True, dtype=str)
    df.dropna(how="all", inplace=True) 
    return df

if __name__ == "__main__":
    client = authenticate()
    df = get_data_from_google_sheet("Raport_Produse", "Rame", client)
    print(df.head())
