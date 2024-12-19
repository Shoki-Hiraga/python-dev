import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting_file.header import *

file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定
input_csv_filename = "2024_09_25.csv"
output_csv_filename = "2024_09_25_export.csv"
input_file = os.path.join(file_directory, input_csv_filename)
output_file = os.path.join(file_directory, output_csv_filename)

# CSVファイルをstring型で読み込み
df = pd.read_csv(input_file, dtype=str)

# 残したいカラムを指定し
columns_to_keep = [
    'CarMaker__c',
    'CarName__c',
    'Id',
    'IsDeleted',
    'LeadSource__c',
    'Years__c'
    ]

# 必要なカラムだけを残す
df_filtered = df[columns_to_keep]

# フィルタリング条件（例: LeadSource__c が "Web" の行だけ）
df_filtered_after = df_filtered[df_filtered['IsDeleted'].astype(str) == 'false']
print(df_filtered_after)

# 新しいCSVファイルとして保存します
df_filtered_after.to_csv(output_file, index=False)
