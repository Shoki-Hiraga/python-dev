import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting_file.header import *

# フォルダパス
folder1 = 'C:/Users/hiraga/Downloads/競合UI_2024_1120'
folder2 = 'C:/Users/hiraga/Downloads/競合UI_2024_1122'

# ファイルパス
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定 # file_path.py で定義したファイルディレクトリを指定
file_name = "比較結果.csv"
output_file = os.path.join(file_directory, file_name)


# フォルダ内のファイルリストを取得
files1 = {os.path.basename(f): os.path.join(folder1, f) for f in os.listdir(folder1) if f.endswith('.html')}
files2 = {os.path.basename(f): os.path.join(folder2, f) for f in os.listdir(folder2) if f.endswith('.html')}

# 共通のファイル名を取得
common_files = set(files1.keys()) & set(files2.keys())

# 結果を保存するリスト
results = []

# 各ファイルの比較
for file_name in common_files:
    with open(files1[file_name], 'r', encoding='utf-8') as f1, open(files2[file_name], 'r', encoding='utf-8') as f2:
        content1 = f1.readlines()
        content2 = f2.readlines()
        diff = list(difflib.unified_diff(content1, content2, lineterm=''))
        
        # 差分がある場合のみ結果を追加
        if diff:
            results.append([file_name, "\n".join(diff)])

# CSVに書き込む
with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ファイル名", "異なる要素"])
    writer.writerows(results)

print(f"比較結果を {output_file} に出力しました。")
