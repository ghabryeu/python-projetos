import expense_tracker
import pandas as pd

# Read the CSV file into a DataFrame
csv_file_path = 'expenses.csv'
df = pd.read_csv(csv_file_path)

# Save the DataFrame to an Excel file
excel_file_path = 'expenses.xlsx'
df.to_excel(excel_file_path, index=False)
