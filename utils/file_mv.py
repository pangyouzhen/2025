import subprocess
import sys
from pathlib import Path

import pandas as pd


def main():
    # 检查命令行参数
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    
    # 获取文件名
    file_path = sys.argv[1]
    print(file_path)
    excel_file = Path(f"{file_path}")
    filename = excel_file.stem
    csv_file = f"{filename}.csv"
    
    # 读取 Excel 文件
    try:
        df = pd.read_excel(excel_file)
        assert all(df['类别'].duplicated()) == False
        # 将数据保存为 CSV 文件
        csv_file = f'../sentiment/weekly/{filename}.csv'
        df.to_csv(csv_file, index=False)
        subprocess.run(f"mv ../workday_data/{filename}.xlsx ../sentiment/weekly/{filename}.xlsx", shell=True)
    except FileNotFoundError:
        print(f"File {excel_file} not found.")
    except KeyError:
        print("Column '类别' not found in the Excel file.")

if __name__ == '__main__':
    main()
