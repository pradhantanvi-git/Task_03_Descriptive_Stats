import csv
from collections import Counter, defaultdict
import math

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
    raise ValueError("Invalid dataset choice")

# === Load CSV ===
with open(filename, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"Total rows: {len(rows)}")

nums = []
texts = []

# === Collect numeric + text values ===
for row in rows:
    val = row.get(numeric_col, '')
    if val and val.isdigit():
        nums.append(int(val))
    texts.append(row.get(text_col, ''))

# === Overall numeric stats ===
if nums:
    mean = sum(nums) / len(nums)
    minimum = min(nums)
    maximum = max(nums)
    stdev = math.sqrt(sum((x - mean) ** 2 for x in nums) / len(nums))
    print(f"\n{numeric_col} → Count={len(nums)}, Mean={mean:.2f}, Min={minimum}, Max={maximum}, StdDev={stdev:.2f}")

# === Non-numeric overall ===
counter = Counter(texts)
print(f"\n{text_col} → Unique={len(counter)}, Most common={counter.most_common(1)}")

# === Group by text_col ===
group1 = defaultdict(list)
for row in rows:
    k = row.get(text_col, '')
    v = row.get(numeric_col, '')
    if v and v.isdigit():
        group1[k].append(int(v))

print(f"\nGrouped by {text_col}:")
for k, vals in group1.items():
    mean = sum(vals) / len(vals)
    minimum = min(vals)
    maximum = max(vals)
    stdev = math.sqrt(sum((x - mean) ** 2 for x in vals) / len(vals))
    print(f"{k}: Count={len(vals)}, Mean={mean:.2f}, Min={minimum}, Max={maximum}, StdDev={stdev:.2f}")

# === Group by page_id + ad_id for Ads only ===
if dataset == 'ads':
    group2 = defaultdict(list)
    for row in rows:
        k = (row.get('page_id', ''), row.get('ad_id', ''))
        v = row.get(numeric_col, '')
        if v and v.isdigit():
            group2[k].append(int(v))
    print("\nGrouped by page_id + ad_id:")
    for k, vals in group2.items():
        mean = sum(vals) / len(vals)
        minimum = min(vals)
        maximum = max(vals)
        stdev = math.sqrt(sum((x - mean) ** 2 for x in vals) / len(vals))
        print(f"{k}: Count={len(vals)}, Mean={mean:.2f}, Min={minimum}, Max={maximum}, StdDev={stdev:.2f}")
