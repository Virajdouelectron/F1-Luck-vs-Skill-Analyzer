# 🏎️ F1 Luck vs Skill Analyzer

**F1 Luck vs Skill Analyzer** is a data-driven analytics project that separates **driver skill** from **race luck** in Formula 1 using historical race data. The goal is to answer a fundamental motorsport question: *How much of a driver’s success is earned through performance, and how much is influenced by uncontrollable race events?*

This project builds an **explainable, non–black-box framework** to compute a **Luck Index**, generate **luck-adjusted championship standings**, and identify the **most lucky and unlucky drivers** across seasons.

---

## 🧠 Methodology

Driver performance is decomposed into two components:

**Skill (driver-controlled):**
- Qualifying position percentile  
- Positions gained (excluding DNFs)  
- Average lap time relative to race median  
- Consistency across races  

**Luck (external factors):**
- Mechanical failures (from race status data)  
- Pit stop timing advantage or disadvantage  
- Race chaos (variance in finishing positions)  
- Safety-car proxy using lap-time compression  

All metrics are normalized and combined into a **Skill Score** and **Luck Index**, allowing championship points to be recalculated as **Luck-Adjusted Points**. The entire pipeline prioritizes transparency and analytical reasoning over prediction.

---

## 🛠️ Tech Stack

| Category | Tools |
|--------|------|
| Language | Python 3.8+ |
| Libraries | Pandas, NumPy, Matplotlib |
| Data | Official Formula 1 historical datasets |
| Frontend | HTML, CSS, Vanilla JavaScript |
| Deployment | Netlify (static hosting only) |

---


---

## 📊 Outputs

- Luck-adjusted championship standings  
- Driver-wise Luck Index (season-level)  
- Skill vs Luck visual comparisons  
- Identification of consistently lucky and unlucky drivers  

All results are precomputed in Python and exported as **CSV and PNG files** for static visualization.

---

## ⚠️ Assumptions & Limitations

- Safety car and weather effects are approximated statistically  
- No real-time telemetry or team strategy data  
- Focus is on **explainability**, not prediction  
- Results highlight trends, not absolute driver rankings  

---

## 🚀 Future Scope

- Teammate comparison modeling  
- Weather data integration  
- Interactive frontend filters  
- Constructor-level luck analysis  

---

## 📜 License

MIT License — free to use for learning, research, and portfolio projects.

---

**Author:** Viraj Singh  
*Data Science & Motorsport Analytics Enthusiast*

> *In Formula 1, performance wins races — but luck decides championships.*


