import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = 'ads'  # 'ads', 'fb_posts', 'twitter'

if dataset == 'ads':
    filename = 'data/2024_fb_ads_president_scored_anon.csv'
    numeric_x = 'estimated_spend'
    numeric_y = 'estimated_impressions'

    # Load
    df = pd.read_csv(filename)
    df = df.dropna(subset=[numeric_x, numeric_y])

    # Scatter plot: Spend vs Impressions
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=numeric_x, y=numeric_y, data=df)
    plt.title('Ad Spend vs Estimated Impressions')
    plt.xlabel('Estimated Spend (USD)')
    plt.ylabel('Estimated Impressions')
    plt.tight_layout()
    plt.show()

elif dataset == 'fb_posts':
    filename = 'data/2024_fb_posts_president_scored_anon.csv'
    numeric_col = 'Likes'

    # Load
    df = pd.read_csv(filename)
    df = df.dropna(subset=[numeric_col])

    # Histogram: Likes Distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(df[numeric_col], bins=30, kde=True)
    plt.title('Distribution of Likes on Facebook Posts')
    plt.xlabel('Likes')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

elif dataset == 'twitter':
    filename = 'data/2024_tw_posts_president_scored_anon.csv'
    numeric_col = 'retweetCount'
    text_col = 'source'

    # Load
    df = pd.read_csv(filename)
    df = df.dropna(subset=[numeric_col, text_col])

    # Group by source and get average retweets
    summary = df.groupby(text_col)[numeric_col].mean().reset_index().sort_values(numeric_col, ascending=False).head(5)

    # Bar chart: Average Retweets by Source
    plt.figure(figsize=(8, 5))
    sns.barplot(x=numeric_col, y=text_col, data=summary)
    plt.title('Average Retweets by Source (Top 5)')
    plt.xlabel('Average Retweets')
    plt.ylabel('Source')
    plt.tight_layout()
    plt.show()

else:
    print("Invalid dataset choice!")