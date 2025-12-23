import pandas as pd
import numpy as np
import os

# Load merged dataset
data_path = r'C:\Users\Singh\OneDrive\Desktop\viraj\F1-Luck-vs-Skill-Analyzer\data\merged_results.csv'
merged = pd.read_csv(data_path)

# --- SKILL SCORE CALCULATION ---
def calculate_skill_scores(df):
    df = df.copy()
    # Qualifying: normalized grid position (1 = pole, 0 = last)
    df['skill_qualifying'] = (df.groupby('raceId')['grid'].transform('max') - df['grid']) \
                            / (df.groupby('raceId')['grid'].transform('max'))
    # Race pace: median lap time vs driver avg lap time (requires lap_times.csv, placeholder here)
    df['skill_race_pace'] = np.nan  # To be filled with lap_times merge
    # Positions gained (excluding DNFs)
    df['skill_positions_gained'] = np.where(df['positionOrder'] > 0,
                                            df['grid'] - df['positionOrder'],
                                            0)
    # Consistency: placeholder (requires lap_times.csv)
    df['skill_consistency'] = np.nan
    # Teammate comparison: placeholder (requires teammate logic)
    df['skill_teammate'] = np.nan
    # Weighted sum (simple for now)
    df['skill_total'] = df['skill_qualifying'].fillna(0)*0.3 + \
                       df['skill_positions_gained'].fillna(0)*0.2
    return df

# --- LUCK INDEX CALCULATION ---
def calculate_luck_index(df):
    df = df.copy()
    # Mechanical DNF: -1 if status is mechanical
    mechanical_statuses = ['Engine', 'Hydraulics', 'Transmission', 'Electrical', 'Clutch', 'Brakes', 'Gearbox', 'Suspension', 'Driveshaft', 'Fuel pressure', 'Oil pressure', 'Water pressure', 'Overheating']
    df['luck_mechanical_dnf'] = df['status'].apply(lambda x: -1 if any(m in str(x) for m in mechanical_statuses) else 0)
    # Safety car/pit timing: placeholder (requires pit/lap analysis)
    df['luck_safetycar_pit'] = np.nan
    # Race chaos: +1/-1 for mass DNFs (placeholder)
    df['luck_chaos'] = np.nan
    # Total luck index (simple sum for now)
    df['luck_total'] = df['luck_mechanical_dnf'].fillna(0)
    return df

# Calculate and save
skill_df = calculate_skill_scores(merged)
luck_df = calculate_luck_index(merged)

# Merge skill and luck
final_df = skill_df.copy()
final_df['luck_total'] = luck_df['luck_total']
final_df.to_csv(r'C:\Users\Singh\OneDrive\Desktop\viraj\F1-Luck-vs-Skill-Analyzer\data\skill_luck_results.csv', index=False)

print('Skill and Luck calculations complete. Output saved to data/skill_luck_results.csv')
