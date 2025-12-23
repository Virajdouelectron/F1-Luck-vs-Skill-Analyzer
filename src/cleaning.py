import pandas as pd
import numpy as np
import os

data_dir = r'C:\Users\Singh\OneDrive\Desktop\viraj\F1-Luck-vs-Skill-Analyzer\F1 data'
output_dir = r'C:\Users\Singh\OneDrive\Desktop\viraj\F1-Luck-vs-Skill-Analyzer\data'

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Load datasets
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
        except Exception as e:
            print(f"Error loading {fname}: {e}")
    return datasets

datasets = load_datasets(data_dir, filenames)

# --- CLEANING & MERGING ---
# Merge core race/driver/constructor info for each result
results = datasets['results']
drivers = datasets['drivers']
races = datasets['races']
constructors = datasets['constructors']
status = datasets['status']

# Merge results with races, drivers, constructors, status
merged = results.merge(races, on='raceId', suffixes=('', '_race')) \
               .merge(drivers, on='driverId', suffixes=('', '_driver')) \
               .merge(constructors, on='constructorId', suffixes=('', '_constructor')) \
               .merge(status, on='statusId', suffixes=('', '_status'))

# Save merged dataset for further analysis
merged.to_csv(os.path.join(output_dir, 'merged_results.csv'), index=False)

# Print info
print(f"Merged results shape: {merged.shape}")
print(f"Columns: {list(merged.columns)}")
print(merged.head(2))
