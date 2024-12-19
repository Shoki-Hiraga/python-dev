from setting_file.header import *
from Main_ads_scraping import GoogleAdsScraper, csv_init
from setting_file.scraping_KW.ads_KW_ import search_keywords_list

# CSV区切り文字を指定
csv_delimiter = ','

# ファイルパス
file_directory = file_path.file_directory  # file_path.py で定義したファイルディレクトリを指定
file_name = "ad_search_results.csv"
output_file = os.path.join(file_directory, file_name)

# グローバル変数としてHTML要素を指定
html_elements = {
    'ad_container': 'uEierd',
    'ad_title': 'CCgQ5',
    'ad_url': 'a'
}

# CSVヘッダーをグローバル変数として定義
headers = ['keyword', 'title', 'url']

delay_seconds = 5

# 複数キーワードを指定
keywords = search_keywords_list

# CSV初期化
csv_initializer = csv_init(output_file, headers, csv_delimiter)
csv_initializer.initialize_csv()

# キーワードごとにスクレイパーを実行
for keyword in keywords:
    scraper = GoogleAdsScraper(keyword, output_file, csv_delimiter, html_elements, delay_seconds)
    scraper.run()
