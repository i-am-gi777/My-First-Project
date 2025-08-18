import pandas as pd
import os
import sys

def convert_csv_to_excel(csv_path, excel_path=None):
    if not os.path.exists(csv_path):
        print(f"❌ Error: File '{csv_path}' not found.")
        return

    try:
        df = pd.read_csv(csv_path)
        if excel_path is None:
            excel_path = csv_path.replace('.csv', '.xlsx')
        df.to_excel(excel_path, index=False)
        print(f"✅ Excel file created: {excel_path}")
    except Exception as e:
        print(f"❌ Failed to convert: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("📌 Usage: python convert.py <path-to-csv> [output-xlsx]")
    else:
        csv_file = sys.argv[1]
        excel_file = sys.argv[2] if len(sys.argv) > 2 else None
        convert_csv_to_excel(csv_file, excel_file)


