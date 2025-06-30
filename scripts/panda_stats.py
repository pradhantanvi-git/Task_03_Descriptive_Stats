import pandas as pd

# === Pick your dataset ===
dataset = 'twitter'  # Please change here according to the dataset - 'ads', 'fb_posts', 'twitter'

if dataset == 'ads':
    filename = 'data/2024_fb_ads_president_scored_anon.csv'
    numeric_col = 'estimated_impressions'
    text_col = 'page_id'

elif dataset == 'fb_posts':
    filename = 'data/2024_fb_posts_president_scored_anon.csv'
    numeric_col = 'Likes'
    text_col = 'Facebook_Id'

elif dataset == 'twitter':
    filename = 'data/2024_tw_posts_president_scored_anon.csv'
    numeric_col = 'retweetCount'
    text_col = 'month_year'

else:
    raise ValueError("Invalid dataset choice.")

# === Load CSV ===
df = pd.read_csv(filename)
print(f"Total rows: {len(df)}")

# === Overall numeric stats ===
print(f"\n{numeric_col} →")
print(df[numeric_col].describe())

# === Overall text stats ===
print(f"\n{text_col} → Unique={df[text_col].nunique()}")
print(f"Most common:\n{df[text_col].value_counts().head(1)}")

# === Group by text_col ===
print(f"\nGrouped by {text_col}:")
group1 = df.groupby(text_col)[numeric_col].describe()
print(group1)

# === Group by page_id + ad_id for ads only ===
if dataset == 'ads':
    print("\nGrouped by page_id + ad_id:")
    group2 = df.groupby(['page_id', 'ad_id'])[numeric_col].describe()
    print(group2)
