from collections import Counter
from pathlib import Path

import pandas as pd

p = Path("../sentiment/strong/")
csvs = [i for i in p.glob("*.csv")]
csvs.sort()
# print(csvs)

k = 30

dfs = []
for i in csvs[-k:]:
    df = pd.read_csv(i.absolute())
    dfs.append(df)

all_df = pd.concat(dfs)
c = Counter(all_df["名称"].tolist())
print(c.most_common(20))