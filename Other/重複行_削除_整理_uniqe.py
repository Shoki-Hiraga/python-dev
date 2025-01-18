import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting_file.header import *

# ファイルパス
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定 # file_path.py で定義したファイルディレクトリを指定
# 入力するCSVファイル名
input_csv_filename = 'site_search_results_pagenation5ログ.csv'
# 出力するCSVファイル名
output_csv_filename = '重複チェック済み_site_search_results_pagenation.csv'

# ファイルパスの組み立て
input_file = os.path.join(file_directory, input_csv_filename)
output_file = os.path.join(file_directory, output_csv_filename)


# 列数 -1 を指定する (１列目を指定するなら 0)
column = 0

def process_data(input_file, output_file):

    # 値を保持
    seen_values = {}

    with open(input_file, newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        # ヘッダーを読み込む
        header = next(reader, None)  # この行で元ファイルのヘッダーを取得

        # カウンターを初期化
        processed_count = 0

        for row in reader:
            if not row:
                break  # CSV行の終わりを検知した場合、ループを終了する

            # columnをインデックス
            column_value = row[column] 

            # 重複チェック column_value の値をチェック
            if column_value in seen_values:
                # column_value が重複した場合は行を削除
                seen_values[column_value].append(row)
            else:
                # 重複無しの場合はインデックス
                seen_values[column_value] = [row]

            processed_count += 1

            # 進行状況をターミナルにリアルタイムで表示
            if processed_count % 1 == 0:
                print(f" {column_value}: {processed_count} ")

    # 出力ファイルを書き込みモードで開き、処理結果を保存します
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        # CSVファイルの最初の行にヘッダーを書き込みます
        writer.writerow(header)
        # seen_valuesに保存された各値に対してループを実行します
        for value_rows in seen_values.values():
            # 各値に対応する行の中から最も古い行を選択します
            # ここでは最初の列の値を基準にして最小値を見つけます（最初の列が日付や一意の識別子と仮定）
            oldest_row = min(value_rows, key=lambda x: x[0])
            # 選択された最も古い行を出力ファイルに書き込みます
            writer.writerow(oldest_row)


    print("処理が完了しました。")

if __name__ == "__main__":
    process_data(input_file, output_file)
