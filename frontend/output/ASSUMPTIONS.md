# F1 Luck vs Skill Analyzer - Assumptions & Methodology

## Assumptions

1. **Mechanical DNFs** are identified by status descriptions containing terms like "Engine", "Hydraulics", etc. (see `luck_mechanical_dnf` in code).
2. **Safety car and pit stop luck** are not directly available; placeholders exist for future lap/pit timing analysis.
3. **Teammate comparison** is a placeholder; logic can be added for direct intra-team comparison if required.
4. **Lap time-based metrics** (race pace, consistency) require merging with `lap_times.csv`, currently marked as placeholders.
5. **Positions gained** is set to zero for DNFs (not classified).
6. **Luck-adjusted points** = Official points + Luck Index (simple sum for demonstration, can be refined).
7. **All groupings** (for standings, luck index, etc.) are per season (using `year` from races).
8. **Plots** use available skill and luck scores; missing values (from placeholders) are ignored.
9. **No external data or APIs** are used; only provided CSVs are loaded from the local data folder.

## Methodology

- Data is loaded, cleaned, and merged using `raceId`, `driverId`, `constructorId`, and `statusId`.
- Skill and luck metrics are calculated per driver per race, then aggregated per season.
- All outputs (tables and plots) are saved to the `output/` directory for frontend use.

---

For further refinement, update the placeholders for lap time and teammate logic in `src/skill_luck.py`.
