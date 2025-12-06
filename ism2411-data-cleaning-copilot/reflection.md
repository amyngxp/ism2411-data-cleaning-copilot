# Reflection on Data Cleaning Project

## What Copilot Generated
GitHub Copilot suggested several functions for the cleaning pipeline:
- `load_data(file_path: str)`
- `clean_column_names(df)`
- Parts of `handle_missing_values(df)` and `remove_invalid_rows(df)`  

I triggered Copilot by writing clear comments describing what each function should do.

## What I Modified
- Updated `handle_missing_values` to fill missing prices with product-specific median, falling back to overall median.  
- Added `strip_whitespace_from_text_columns` to ensure text columns are cleaned.  
- Renamed some variables (`prodname`, `qty`) for clarity.  
- Ensured negative quantities and prices are removed consistently.  

These modifications were needed to match the assignment requirements and handle messy real-world data correctly.

## What I Learned
- Cleaning messy CSV data requires careful handling of missing and invalid values, and consistent column naming.  
- Pandas provides powerful tools for handling missing data, applying functions, and filtering rows.  
- Copilot is a helpful assistant, but its suggestions often need review and adaptation. For example, Copilot suggested filling missing prices with a single median; I modified it to consider product-level medians, which is more accurate.
