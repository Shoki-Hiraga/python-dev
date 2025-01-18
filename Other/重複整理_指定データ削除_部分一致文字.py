import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting_file.header import *


# ファイルパス
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定 # file_path.py で定義したファイルディレクトリを指定
input_csv_filename = "2024_organic.csv"
output_csv_filename = "2024_organic_整形後.csv"
input_file = os.path.join(file_directory, input_csv_filename)
output_file = os.path.join(file_directory, output_csv_filename)


# 条件に一致する行を削除したい列のインデックス (0から始まる)
index = 0  # 列指定
# 条件に一致する複数の値を持つリスト
value_list = [
    "/historia/",
    "(not set)",
    "/maker/"
              ]

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # ヘッダーを書き出す
    headers = next(reader)
    writer.writerow(headers)

    # カウンターを初期化
    processed_count = 0

    for row in reader:
        # indexの列の値がvalue_list内のいずれかと部分一致する場合、その行は書き込まない
        if not any(value in row[index] for value in value_list):
            writer.writerow(row)
            processed_count += 1
        print(f"{processed_count}")
        # print(f"{value_list}: {processed_count}")
print("処理が完了しました。")
