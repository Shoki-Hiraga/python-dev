import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting_file.header import *

# ファイルパス
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定
file_name = "scraped_data.csv"
output_file = os.path.join(file_directory, file_name)


# CSVヘッダー行の設定
header_row = ['URL', '買取実績', 'ステータス']

# CSVファイルの区切り文字を指定（デフォルトはカンマ）
csv_delimiter='★'

# # ページネーションURLインスタンス
# from setting_file.scraping_url_Param_or_page.Page_Param import PageParamUrlGenerator
# base_url = "https://www.carsensor.net/usedcar/bNI/s054/index{}.html"
# parameter = ""  # パラメーター無し
# pagenation_min = 1
# pagenation_max = 4
# url_generator = PageParamUrlGenerator(base_url, parameter, pagenation_min, pagenation_max)
# URLS = url_generator.generate_urls()  # URLリストを生成



# ＝＝＝＝＝＝＝＝＝＝個別URLでスクレイピングする時＝＝＝＝＝＝＝＝＝＝
# 個別URLリストインスタンス
from setting_file.scraping_url.Qcarpage_kaitori_ruslut import URLS
for url in URLS:
    # URLを使った処理
    print(f"Scraping {url}...")

# スクレイピング遅延処理
delay_time_set = random.uniform(000.1, 000.2)

# CSSセレクタの配列
CSS_selectors = [
    ('maker__results__title', 'text')
]


# アクセスエラー発生時の最大リトライ回数を設定
MAX_RETRIES = 10

# Mainスクレイピングのインスタンス化
from Main.Main.Main_alot_urls_scraping import alot_urls_scraping
scraping_func_instance = alot_urls_scraping
()
scraping_func_instance.scrape_url(url, CSS_selectors, delay_time_set)

# スクレイピングの進捗をログに記録する関数
def log_progress(completed_count, total_count):
    percentage_complete = (completed_count / total_count) * 100
    print(f'{round(percentage_complete, 2)} % 完了.... {completed_count} / {total_count}')

# 完了したURLの数
completed_count = 0

# CSVファイルを開き、ヘッダーとスクレイプしたデータを書き込み、ログを出力
from Main.Main.Main_CsvWrite import CsvWriter
# CsvWriterのインスタンス生成
csv_writer = CsvWriter(output_file, header_row, delimiter=csv_delimiter)
# CSV書き込み処理の呼び出し
csv_writer.write_to_csv(URLS, scraping_func_instance, CSS_selectors, delay_time_set, log_progress)
