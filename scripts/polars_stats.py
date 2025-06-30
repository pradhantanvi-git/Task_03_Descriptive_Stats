import polars as pl

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
df = pl.read_csv(filename)
print(f"Total rows: {df.shape[0]}")

# === Overall numeric stats ===
print(f"\n{numeric_col} → Overall Stats:")
print(df.select([
    pl.col(numeric_col).count().alias('count'),
    pl.col(numeric_col).mean().alias('mean'),
    pl.col(numeric_col).std().alias('stddev'),
    pl.col(numeric_col).min().alias('min'),
    pl.col(numeric_col).max().alias('max')
]))

# === Overall text stats ===
print(f"\n{text_col} →")
print("Unique:", df.select(pl.col(text_col).n_unique()))
print("Most common:", df.select(pl.col(text_col).mode()))

# === Group by text_col ===
print(f"\nGrouped by {text_col}:")
group1 = df.group_by(text_col).agg([
    pl.col(numeric_col).count().alias('count'),
    pl.col(numeric_col).mean().alias('mean'),
    pl.col(numeric_col).std().alias('stddev'),
    pl.col(numeric_col).min().alias('min'),
    pl.col(numeric_col).max().alias('max')
])
print(group1)

# === Group by page_id + ad_id for Ads only ===
if dataset == 'ads':
    print("\nGrouped by page_id + ad_id:")
    group2 = df.group_by(['page_id', 'ad_id']).agg([
        pl.col(numeric_col).count().alias('count'),
        pl.col(numeric_col).mean().alias('mean'),
        pl.col(numeric_col).std().alias('stddev'),
        pl.col(numeric_col).min().alias('min'),
        pl.col(numeric_col).max().alias('max')
    ])
    print(group2)
