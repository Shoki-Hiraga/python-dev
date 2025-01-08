import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting_file.header import *

# スクレイピング遅延処理
delay_time_set = random.uniform(000.1, 000.2)

# ファイルパス
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定
file_name = "scraped_data2.csv"
output_file = os.path.join(file_directory, file_name)

# CSVヘッダー行の設定
header_row = ['URL', '買取実績', '買取相場', 'テキストコンテンツ', 'お客様の声', 'indexチェック']
    
# CSVファイルの区切り文字を指定（デフォルトはカンマ）
csv_delimiter='★'


# URL設定のインポート
from setting_file.scraping_url_Param_or_page.Page_Param import PageParamUrlGenerator
from setting_file.scraping_url.Qcarpage_all_contents_url_copy1 import URLS as IndividualURLS

# URL設定を選択する変数（1: ページネーション, 2: 個別URL）
url_setting_index = 2  # 1 または 2 に変更して切り替え

# ページネーション用URLの生成関数
def generate_pagination_urls():
    base_url = "https://www.carsensor.net/usedcar/bNI/s054/index{}.html"
    parameter = ""  # パラメーター無し
    pagenation_min = 1
    pagenation_max = 4
    url_generator = PageParamUrlGenerator(base_url, parameter, pagenation_min, pagenation_max)
    return url_generator.generate_urls()

# URL設定
url_Settings = {
    1: generate_pagination_urls,  # ページネーション用URL生成関数
    2: lambda: IndividualURLS      # 個別URLリスト
}

# URLリストの取得（関数呼び出しで取得）
URLS = url_Settings[url_setting_index]()  

# URLリストの処理
for url in URLS:
    print(f"Scraping {url}...")

# CSSセレクタの配列
CSS_selectors = [
    ('p.maker__results__description', 'text'),  
    ('h2.c-marketprice__title', 'text'),  
    ('div.c-content__inner', 'text'),
    ('h2.c-reviews__title', 'text'),
    ('meta[name="robots"]', 'attr', 'content')
    # ('.cassetteMain__title a', 'text', 'link'),  # リンクとテキストを同時に取得する場合
    # ('div.cassetteWrap:nth-of-type(n+3) dt:-soup-contains("走行距離") + dd', 'text'),  
    # ('dt:-soup-contains("年式") + .specList__data span.specList__emphasisData', 'text'),  
    # ('.carListWrap dt:-soup-contains("修復歴") + dd', 'text')  
]

# アクセスエラー発生時の最大リトライ回数を設定
MAX_RETRIES = 10

# Mainスクレイピングのインスタンス化
from Main.Main_alot_urls_scraping import alot_urls_scraping
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
from Main.Main_CsvWrite import CsvWriter
# CsvWriterのインスタンス生成
csv_writer = CsvWriter(output_file, header_row, delimiter=csv_delimiter)
# CSV書き込み処理の呼び出し
csv_writer.write_to_csv(URLS, scraping_func_instance, CSS_selectors, delay_time_set, log_progress)