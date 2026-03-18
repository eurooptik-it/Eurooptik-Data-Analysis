# Eurooptik Data Analysis

Python scripts and Jupyter notebooks for collecting, processing, and analyzing Eurooptik operational data (sales, questionnaire, and patient-oriented analysis).

## What This Project Does

- Extracts and normalizes data from Google Sheets and local inputs.
- Processes order/sales records and patient datasets.
- Generates analysis outputs and report-ready artifacts from notebooks.

## Repository Structure

- `main.py` - Entry point for running project logic from scripts.
- `scraper.py` - Data extraction and scraping workflow.
- `questionnaire.py` - Questionnaire-related processing.
- `brands.txt` - Brand dictionary used by data processing/scraping logic.
- `requirements.txt` - Python dependencies.
- `src/utils.py` - Shared constants and helper utilities.
- `src/pacients_analysis.ipynb` - Patient analysis notebook.
- `src/procesare_bon_comanda.ipynb` - Sales/order processing notebook.

## Requirements

- Python 3.10+ recommended.
- A Google service account credentials file named `credentials.json` in the repository root.

## Setup

1. Create a virtual environment.

```bash
python -m venv .venv
```

2. Activate it.

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies.

```bash
pip install -r requirements.txt
```

## Usage

Run script-based workflows:

```bash
python main.py
python scraper.py
python questionnaire.py
```

Run notebook workflows:

1. Open the notebook from `src/` in VS Code or Jupyter Lab.
2. Select the project virtual environment kernel.
3. Execute cells in order (or run all).

## Generated Files Policy

Generated datasets and report exports are intentionally ignored and should stay local, including:

- CSV exports
- Excel exports
- Notebook-rendered HTML/PDF reports

This keeps the repository clean and avoids pushing sensitive or large generated artifacts.

## Security Notes

- Do not commit `credentials.json`.
- Do not commit patient-identifiable raw or processed datasets.
- Share sanitized samples only when needed for debugging.

## Recommended Workflow

1. Pull latest changes and activate your local virtual environment.
2. Run script or notebook workflows to regenerate local outputs.
3. Review generated artifacts locally in `src/results/` and exported data files.
4. Before commit, verify only source code and documentation changes are staged.
5. Keep generated datasets/reports local (they are ignored by `.gitignore`).

## Troubleshooting

- If authentication fails, verify `credentials.json` exists in the project root and has access to the target Google Sheets.
- If imports fail, ensure the active interpreter is the same environment where `requirements.txt` was installed.
