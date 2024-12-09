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
from setting_file.scraping_url.Qcarpage_all_contents_url_copy1 import URLS
for url in URLS:
    # URLを使った処理
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
from Main_alot_urls_scraping import alot_urls_scraping
scraping_func_instance = alot_urls_scraping
()
scraping_func_instance.scrape_url(url, CSS_selectors, delay_time_set)

# スクレイピングの進捗をログに記録する関数
def log_progress(completed_count, total_count):
    percentage_complete = (completed_count / total_count) * 100
    print(f'{round(percentage_complete, 2)} % 完了.... {completed_count} / {total_count}')

# 完了したURLの数
completed_count = 0

# CSVファイルを開き、ヘッダーとスクレイプしたデータを書き込む
with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter = csv_delimiter)
    csv_writer.writerow(header_row)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # URLリストに対して並行してスクレイピングを実行
        for url in URLS:
            result = scraping_func_instance.scrape_url(url, CSS_selectors, delay_time_set)  # 各URLに対してスクレイピングを実行
            url, scraped_data, status_code = result
            max_length = max(len(data) for data in scraped_data)  # 最大の列数を取得
            
            # スクレイプしたデータを行としてCSVに書き込む
            for i in range(max_length):
                row_data = [url] + [data[i] if i < len(data) else '' for data in scraped_data] + [status_code]
                csv_writer.writerow(row_data)

            completed_count += 1  # 完了したURLの数を更新
            log_progress(completed_count, len(URLS))  # 進捗のログ

            print(f'{header_row[0]}: {url}')  # 完了したURLを表示
            print(' ')
            print('--------------------------------------------')

print('スクレイピングが完了しました。')  # 全てのスクレイピングが完了したことを通知
