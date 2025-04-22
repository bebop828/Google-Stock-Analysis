# 📈 <span style="color: blue;">G</span><span style="color: red;">o</span><span style="color: yellow;">o</span><span style="color: blue;">g</span><span style="color: green;">l</span><span style="color: red;">e</span> Stock Performance & Milestone Analysis


This project is a comprehensive 20-year analysis of Google's (now Alphabet Inc.) stock performance, focusing on how the company's strategic decisions, innovations, and business milestones may have influenced its stock price over time. Each year is analyzed in a separate Jupyter notebook, following a consistent format for clarity and reproducibility.

This README outlines the structure, methodology, and key components of the project.

---

## Tools and Technologies

- **Python (Jupyter Notebooks)**
- **pandas** – Data manipulation and filtering
- **matplotlib / seaborn** – Data visualization
- **yfinance** – Supplemental data retrieval for 2024  
- **AI Tools** – Used for information gathering, verification, and writing assistance  

### **Linear Regression imports** 
- **StandardScaler**  
- **train_test_split**  
- **LinearRegression**  
- **root_mean_squared_error, r2_score**  

---

## Data Sources

- **Historical Stock Data (2004–April 2024)**:  
  Sourced from a Kaggle dataset that includes daily stock performance for Google/Alphabet Inc.
  
- **Recent Stock Data (April 2024–Present)**:  
  Pulled using the `yfinance` API to ensure data continuity.

All yearly datasets maintain a consistent schema and formatting for seamless analysis across time periods.

---

## Milestone Research & Verification

To capture the key business events that could have influenced stock movements, milestones for each year were researched using a **collection of AI-assisted tools**. These tools helped in:

- Identifying significant events
- Cross-verifying for accuracy and relevance
- Summarizing complex information for inclusion in the notebooks

A dedicated **Sources and References** document will accompany this project to provide transparency about the AI tools and web-based resources used throughout.

---

## Methodology

1. **Introduction of Key Events**:  
   A summary of Google’s business activities and achievements for the year.

2. **Data Import & Preprocessing**:  
   Stock data is filtered to isolate the selected year and is prepared for visualization.

3. **Visual Analysis**:  
   Stock trends are analyzed using visual tools to highlight:
   - Opening and closing prices
   - Daily highs and lows
   - Trading volume

4. **Insight & Connection**:  
   Stock behavior is then interpreted in the context of Google’s milestones, **manually correlating** potential cause-and-effect relationships.

5. **Summary**:  
   Each notebook concludes with a reflection on how that year’s business activities may have impacted investor confidence and stock performance.

---

## Reusability

This project was developed with reusability in mind. Its format and methodology can be **adapted to analyze other publicly traded companies** using similar data sources and event-driven frameworks. All code, charts, and research practices can serve as a blueprint for comparable long-term stock analyses.

---


## Project Highlights

- Covers **20 years of stock data** from 2004–2024
- Investigates the connection between **innovation and investor behavior**
- Fully reproducible and scalable structure
- Combination of **manual research** and **AI-assisted methodology**
- Readable, year-by-year breakdown in Jupyter Notebook format

