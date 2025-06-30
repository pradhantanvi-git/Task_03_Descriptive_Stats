import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# === Use a nice style for all plots ===
sns.set_theme(style="whitegrid")
plt.rcParams.update({'figure.autolayout': True})

# === Pick dataset manually ===
dataset = 'twitter'  # 'ads', 'fb_posts', 'twitter'

# === ADS ===
if dataset == 'ads':
    filename = 'data/2024_fb_ads_president_scored_anon.csv'
    numeric_x = 'estimated_spend'
    numeric_y = 'estimated_impressions'

    df = pd.read_csv(filename)

    # Fix numeric conversion
    df[numeric_x] = pd.to_numeric(df[numeric_x], errors='coerce')
    df[numeric_y] = pd.to_numeric(df[numeric_y], errors='coerce')
    df = df.dropna(subset=[numeric_x, numeric_y])
    df = df[(df[numeric_x] > 0) & (df[numeric_y] > 0)]

    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x=numeric_x,
        y=numeric_y,
        data=df,
        hue=numeric_y,
        size=numeric_x,
        palette="viridis",
        alpha=0.7
    )
    plt.title('Ad Spend vs Estimated Impressions', fontsize=16)
    plt.xlabel('Estimated Spend (USD)')
    plt.ylabel('Estimated Impressions')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

# === FACEBOOK POSTS ===
elif dataset == 'fb_posts':
    filename = 'data/2024_fb_posts_president_scored_anon.csv'
    numeric_col = 'Total Interactions'
    text_col = 'Type'

    df = pd.read_csv(filename)

    # Fix numeric
    df[numeric_col] = pd.to_numeric(df[numeric_col], errors='coerce')
    df = df.dropna(subset=[numeric_col, text_col])

    summary = df.groupby(text_col)[numeric_col].mean().reset_index().sort_values(numeric_col, ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=numeric_col,
        y=text_col,
        data=summary,
        palette="mako"
    )
    plt.title('Average Total Interactions by Post Type', fontsize=16)
    plt.xlabel('Average Total Interactions')
    plt.ylabel('Post Type')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

# === TWITTER ===
elif dataset == 'twitter':
    filename = 'data/2024_tw_posts_president_scored_anon.csv'
    date_col = 'month_year'

    df = pd.read_csv(filename)
    df = df.dropna(subset=[date_col])

    summary = df[date_col].value_counts().reset_index()
    summary.columns = ['month_year', 'Tweet Count']
    summary = summary.sort_values('month_year')

    plt.figure(figsize=(12, 6))
    sns.lineplot(
        x='month_year',
        y='Tweet Count',
        data=summary,
        marker='o',
        linewidth=2,
        color="crimson"
    )
    plt.title('Number of Tweets Over Time (By Month)', fontsize=16)
    plt.xlabel('Month-Year')
    plt.ylabel('Number of Tweets')
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

else:
    print("Invalid dataset!")
