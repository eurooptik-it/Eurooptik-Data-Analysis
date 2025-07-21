from scipy.stats import norm
import pandas as pd
from main import authenticate, get_data_from_google_sheet

def count_unique_customers_2025(client):
    df = get_data_from_google_sheet("Clienti", "Clienti", client)
    df = df[df["Nume"].notna() & df["Prenume"].notna()]
    df['Nume'] = df['Nume'].str.strip().str.upper()
    df['Prenume'] = df['Prenume'].str.strip().str.upper()
   
    df = df[df['Data ultimei examinari'].notna()]
    df['Data ultimei examinari'] = pd.to_datetime(df['Data ultimei examinari'], errors='coerce', dayfirst=True)
    df_2025 = df[df['Data ultimei examinari'].dt.year == 2025]
    unique_customers = df_2025.drop_duplicates(subset=['Nume', 'Prenume'])
    count = len(unique_customers)
    print(f"\n--- Unique Customers with Examinations in 2025 ---")
    print(f"Count: {count}")
    return count


def calculate_sample_size(population_size, confidence_level=0.95, margin_of_error=0.05, proportion=0.5):
    z = norm.ppf(1 - (1 - confidence_level) / 2)
    p = proportion
    e = margin_of_error
    n_0 = (z**2 * p * (1 - p)) / (e**2)
    n = n_0 / (1 + (n_0 - 1) / population_size)
    return int(round(n))


def print_sample_size_table(population_size, proportion=0.5):
    confidence_levels = [0.90, 0.95, 0.98, 0.99]
    margins_of_error = [0.10, 0.05, 0.03]
    print("\nTabel comparație dimensiuni eșantion pentru populație de {}:".format(population_size))
    print(f"{'Nivel de încredere':<18} {'Marja de eroare':<16} {'Dimensiune eșantion':<20}")
    print("-"*54)
    for cl in confidence_levels:
        for me in margins_of_error:
            n = calculate_sample_size(population_size, cl, me, proportion)
            print(f"{int(cl*100):<18}% {int(me*100):<15}% {n:<20}")


if __name__ == "__main__":
    client = authenticate()
    
    confidence_level = 0.95
    margin_of_error = 0.05
    
    unique_2025 = count_unique_customers_2025(client)

    if unique_2025 > 0:
        sample_size = calculate_sample_size(unique_2025, confidence_level, margin_of_error)
        print(f"Recommended minimum sample size for a {confidence_level * 100}% confidence level and {margin_of_error * 100}% margin of error: {sample_size}")
        print_sample_size_table(unique_2025)
    else:
        print("No customers with examinations in 2025 found.")