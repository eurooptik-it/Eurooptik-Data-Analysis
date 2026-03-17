# Eurooptik Data Analysis Pipeline 📊

This repository contains the Python-based data analysis pipeline, web scrapers, and reporting tools used for Eurooptik. The project extracts raw data, processes patient/sales information, and generates visual reports using Jupyter Notebooks.

## 🗂 Project Structure

The repository is organized as follows:

- **`main.py`**: The main entry point script (describe briefly what it triggers, e.g., the overall data pipeline).
- **`scraper.py`**: Web scraping script used to extract external data (e.g., fetching brand info using `brands.txt`).
- **`questionnaire.py`**: Script handling the processing of patient/client questionnaire data.
- **`src/`**: Folder containing the core Jupyter Notebooks and utilities for deep data analysis:
  - `pacients_analysis.ipynb`: Generates demographic and visual analysis of patients.
  - `procesare_bon_comanda.ipynb`: Processes and formats order receipts/sales data.
  - `utils.py`: Helper functions used across the notebooks and scripts.
- **`brands.txt`**: Text file containing the list of brands used by the scraper.
- **`requirements.txt`**: List of Python dependencies required to run the project.

*(Note: Raw data files like CSVs or PDFs are excluded from this repository via `.gitignore` for data privacy reasons. They are generated locally when the scripts are run).*

## Getting Started

To run this project locally, please refer to the **"Project Setup"** Issue in the GitHub Issues tab, or follow these basic steps:

1. Ensure **Python (3.8+)** is installed and added to your system PATH.
2. Ensure you have the `credentials.json` file placed in the root directory (needed for Google Sheets API access).
3. Create and activate a virtual environment:
   
```bash
 python -m venv venv
   venv\Scripts\activate 
``` 
4. Install the required libraries:

```bash
pip install -r requirements.txt
```

How to Use
Running the Python Scripts
You can run the standalone scripts directly from the terminal. For example, to run the web scraper:

```Bash
python scraper.py
```
Running the Jupyter Notebooks
To view and generate the visual reports:

Open Visual Studio Code.

Make sure the Jupyter and Python extensions are installed.

Navigate to the src/ folder and open the desired notebook (e.g., pacients_analysis.ipynb).

Click "Run All" at the top of the notebook to execute the cells and generate the latest graphs and HTML/PDF reports.

🔐 Credentials & Security
This project interacts with Google Cloud APIs (Google Sheets/Drive). It requires a valid credentials.json Service Account key.
Never commit the credentials.json or raw patient data (.csv files) to this repository.
