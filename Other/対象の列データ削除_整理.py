import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting_file.header import *

# ファイルパス
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定
# 入力するCSVファイル名
input_csv_filename = 'import.csv'
# 出力するCSVファイル名
output_csv_filename = 'import_fix.csv'


# ファイルパスの組み立て
input_file = os.path.join(file_directory, input_csv_filename)
output_file = os.path.join(file_directory, output_csv_filename)

# 削除する列のインデックスのリスト (例：1, 3 の列を削除する場合は、2, 0 と入力する)
columns_to_remove = [4,3,2,1,0]  
columns_to_remove.sort(reverse=True)  # 高いインデックス順にソート

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # ヘッダーを読み込み、指定した列を削除
    headers = next(reader)
    for column in columns_to_remove:
        del headers[column]
    writer.writerow(headers)

    # カウンターを初期化
    processed_count = 0

    for row in reader:
        # 指定した複数の列をリストから削除
        for column in columns_to_remove:
            del row[column]
        
        # 更新した行を書き出し
        writer.writerow(row)
        processed_count += 1

        # 進行状況をターミナルにリアルタイムで表示
        if processed_count % 100000 == 0:
            print(f"Removed columns {', '.join(map(str, columns_to_remove))}: {processed_count} records processed")
