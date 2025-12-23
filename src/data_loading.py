import os
import pandas as pd

data_dir = r'C:\Users\Singh\OneDrive\Desktop\viraj\F1-Luck-vs-Skill-Analyzer\F1 data'

# List of all dataset filenames
filenames = [
    'circuits.csv',
    'constructor_results.csv',
    'constructor_standings.csv',
    'constructors.csv',
    'driver_standings.csv',
    'drivers.csv',
    'lap_times.csv',
    'pit_stops.csv',
    'qualifying.csv',
    'races.csv',
    'results.csv',
    'seasons.csv',
    'sprint_results.csv',
    'status.csv'
]

def load_datasets(data_dir, filenames):
    datasets = {}
    for fname in filenames:
        path = os.path.join(data_dir, fname)
        try:
            df = pd.read_csv(path)
            datasets[fname.replace('.csv','')] = df
            print(f"Loaded {fname}: {df.shape[0]} rows, {df.shape[1]} columns")
        except Exception as e:
            print(f"Error loading {fname}: {e}")
    return datasets

datasets = load_datasets(data_dir, filenames)

# Print concise summaries
for name, df in datasets.items():
    print(f"\n--- {name} ---")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print(f"Nulls: {df.isnull().sum().sum()}")
    print(df.head(1))
