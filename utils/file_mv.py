import argparse
import datetime
import subprocess

import pandas as pd


def main():
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description='Convert Excel file to CSV.')

    # 添加 filename 参数
    parser.add_argument("-f",'--filename')

    # 解析命令行参数
    args = parser.parse_args()

    # 获取文件名
    filename = args.filename
    filename = str(filename).split(".")[0]
    excel_file = f"{filename}.xlsx"
    csv_file = f"{filename}.csv"

    # 读取 Excel 文件
    try:
        df = pd.read_excel(excel_file)
        assert all(df['类别'].duplicated()) == False 
        # 将数据保存为 CSV 文件
        csv_file = f'../sentiment/weekly/{filename}.csv'
        df.to_csv(csv_file, index=False)
        subprocess.run(f"mv {filename}.xlsx ../sentiment/weekly/{filename}.xlsx",shell=True)
    except FileNotFoundError:
        print(f"File {excel_file} not found.")

if __name__ == '__main__':
    main()
