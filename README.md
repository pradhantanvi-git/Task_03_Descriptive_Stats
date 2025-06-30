# 📊 Task_03_Descriptive_Stats

This repository contains:
- `pure_python_stats.py` — descriptive stats using only Python’s standard library.
- `pandas_stats.py` — same stats using Pandas.
- `polars_stats.py` — same stats using Polars.
- `visuals.py` — bonus visualizations for clearer presentation.

> **Note:** The dataset files are NOT included. Add them in a `data/` folder.

---

## 🚀 How to Run

**1️⃣ Place your CSV files:**

data/
├── 2024_fb_ads_president_scored_anon.csv
├── 2024_fb_posts_president_scored_anon.csv
└── 2024_tw_posts_president_scored_anon.csv

---

**2️⃣ In each script, manually enter the dataset name as required:**

```python
dataset = 'ads'  # or 'fb_posts' or 'twitter'

**Note:** You can also adjust the numeric_col or text_col inside each script if you want to explore different columns.

**3️⃣ Run each script one by one in your terminal (e.g. in Visual Studio Code):**
python pure_python_stats.py
python pandas_stats.py
python polars_stats.py
python visuals.py


# 📈 Summary of Visualizations
Ads: Scatter plot visualizes the relationship between how much money was spent and the reach each ad achieved. It highlights which ads are more cost-efficient by comparing spend to estimated impressions.

Facebook Posts: Bar chart shows which post types (Photo, Video, Link, etc.) generate higher average total interactions. This helps identify which content formats are most engaging.

Twitter: Line chart illustrates how tweet activity changes over time, grouped by month/year. It reveals spikes or drops in posting frequency that may align with campaign phases or events.


## 🔍 Reflection
* Using pure Python, Pandas, and Polars produced the same descriptive statistics after ensuring numeric columns were properly converted and missing data handled.
* Pure Python required the most manual coding — loops, grouping logic, and explicit math.
* Pandas made this faster and clearer with .describe() and .groupby().
* Polars was similar to Pandas but felt faster for big CSVs and uses more modern syntax.
* Matching results exactly required careful checks for data types (many fields were strings, not numbers).
* If coaching a junior analyst, I’d recommend Pandas first to build confidence with tabular data, then Polars for speed on larger data.
* Coding AI tools like ChatGPT were helpful for generating template code, especially for Polars syntax and for fixing grouping bugs quickly.
* These AI tools tend to suggest Pandas by default for descriptive stats — and I agree: it’s easy, widely used, and good for learning.
* I performed basic cleaning to convert numeric columns from text and drop invalid or missing rows. 
* For now, I have not unpacked any nested JSON columns, but I plan to explore those fields in the next stage of this research.
* The bonus visualizations show extra insights — they make the numeric summaries more compelling for stakeholders.



