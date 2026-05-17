# ISM2411 Data Cleaning Project

## Project Overview
This is a small Python project that cleans a messy sales dataset (`sales_data_raw.csv`) and produces a cleaned version (`sales_data_clean.csv`). The goal is to demonstrate data cleaning, basic Python skills, and responsible use of AI coding tools (GitHub Copilot).

## Project Structure
ism2411-data-cleaning-copilot/
├── data/
│ ├── raw/
│ │ └── sales_data_raw.csv
│ └── processed/
│ └── sales_data_clean.csv
├── src/
│ └── data_cleaning.py
├── README.md
└── reflection.md

markdown
Copy code

## How to Run
1. Make sure Python 3 and pandas are installed.  
2. From the project root, run:
```bash
python3 src/data_cleaning.py
The cleaned CSV will be saved to data/processed/sales_data_clean.csv.

The script prints the first few rows of the cleaned data.

Cleaning Steps Implemented
Standardized column names (lowercase, underscores).

Stripped leading/trailing whitespace from text columns.

Handled missing values for price and quantity consistently.

Removed rows with negative quantities or prices.

Hello GitHub!
