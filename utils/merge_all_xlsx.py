from pathlib import Path

import natsort  # 用于自然排序
import pandas as pd

p = Path('../sentiment/weekly/')

# 获取所有 Excel 文件，并按自然排序
files = sorted(p.glob('*.xlsx'), key=lambda x: natsort.natsort_key(str(x)))

dfs = []
for file in files:
    df = pd.read_excel(file)
    print(file)
    if '类别' in df.columns:
        df.set_index('类别', inplace=True)
        if not df.index.duplicated().any():
            dfs.append(df)
        else:
            print(f"Warning: Duplicate indices found in {file}. Skipping this file.")
    else:
        print(f"Warning: '类别' column not found in {file}. Skipping this file.")

# 合并数据
if dfs:
    merged_df = dfs[0]
    for i in range(1, len(dfs)):
        merged_df = pd.merge(merged_df, dfs[i], how='outer', on='类别')

    # 保存合并结果
    merged_df.to_excel('../workday_data/merge_all.xlsx')
    print("Merged file saved as 'merge_all.xlsx'")
else:
    print("No valid Excel files found to merge.")
