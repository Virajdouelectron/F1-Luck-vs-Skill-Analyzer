import pandas as pd
import matplotlib.pyplot as plt
import os

# Load skill & luck results
data_path = r'C:\Users\Singh\OneDrive\Desktop\viraj\F1-Luck-vs-Skill-Analyzer\data\skill_luck_results.csv'
df = pd.read_csv(data_path)
output_dir = r'C:\Users\Singh\OneDrive\Desktop\viraj\F1-Luck-vs-Skill-Analyzer\output'
os.makedirs(output_dir, exist_ok=True)

# 1. Luck-adjusted championship standings
df['luck_adjusted_points'] = df['points'] + df['luck_total']  # Simple sum for demonstration
champ = df.groupby(['year','driverId','surname','forename'])[['points','luck_total','luck_adjusted_points']].sum().reset_index()
champ = champ.sort_values(['year','luck_adjusted_points'], ascending=[True,False])
champ.to_csv(os.path.join(output_dir, 'luck_adjusted_championship.csv'), index=False)

# 2. Luck Index per driver (season)
luck_index = df.groupby(['year','driverId','surname','forename'])['luck_total'].sum().reset_index()
luck_index = luck_index.sort_values(['year','luck_total'], ascending=[True,False])
luck_index.to_csv(os.path.join(output_dir, 'luck_index_per_driver.csv'), index=False)

# 3. Most lucky/unlucky drivers per season
most_lucky = luck_index.groupby('year').apply(lambda x: x.loc[x['luck_total'].idxmax()]).reset_index(drop=True)
most_unlucky = luck_index.groupby('year').apply(lambda x: x.loc[x['luck_total'].idxmin()]).reset_index(drop=True)
most_lucky.to_csv(os.path.join(output_dir, 'most_lucky_per_season.csv'), index=False)
most_unlucky.to_csv(os.path.join(output_dir, 'most_unlucky_per_season.csv'), index=False)

# 4. Visual evidence: Luck vs Skill scatter plot (per season)
for year, group in df.groupby('year'):
    plt.figure(figsize=(8,6))
    plt.scatter(group['skill_total'], group['luck_total'], alpha=0.7)
    plt.xlabel('Skill Score')
    plt.ylabel('Luck Index')
    plt.title(f'Luck vs Skill - {year}')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig(os.path.join(output_dir, f'luck_vs_skill_{year}.png'))
    plt.close()

print('All tables and plots exported to output/.')
