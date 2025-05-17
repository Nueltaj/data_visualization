import pandas as pd

def csv_to_excel(csv_file_path, excel_file_path=None, sheet_name='Sheet1'):
    """
    Convert a CSV file to an Excel file.
    
    Parameters:
    - csv_file_path: Path to the input CSV file
    - excel_file_path: Path for the output Excel file (default: same as CSV but with .xlsx extension)
    - sheet_name: Name of the worksheet in the Excel file
    """
    # Read the CSV file
    df = pd.read_csv(csv_file_path)
    
    # Set default output path if not provided
    if excel_file_path is None:
        excel_file_path = csv_file_path.replace('.csv', '.xlsx')
    
    # Write to Excel file
    df.to_excel(excel_file_path, sheet_name=sheet_name, index=False)
    
    print(f"Successfully converted {csv_file_path} to {excel_file_path}")

if __name__ == "__main__":
    # Get input from user
    csv_path = input("Enter the path to your CSV file: ")
    output_path = input("Enter the output Excel file path (press Enter to use default): ").strip()
    
    if not output_path:
        csv_to_excel(csv_path)
    else:
        csv_to_excel(csv_path, output_path)