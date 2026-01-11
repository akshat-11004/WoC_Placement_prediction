import pandas as pd
import sys


CSV_FILE = "D:\downloads\woc'26\data\placementdata.csv"  

try:    
    df = pd.read_csv(CSV_FILE)    
    
    print(f"Successfully loaded {CSV_FILE}")
    print(f"DataFrame shape: {df.shape}")    
    
    print(f"\nColumns: {df.columns.tolist()}")    
    
    print("\nFirst 5 rows (df.head()):")
    print(df.head())
    
except FileNotFoundError:
    print(f"Error: File '{CSV_FILE}' not found.")
except Exception as e:
    print(f"Error loading CSV: {e}")