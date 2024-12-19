from setting_file.header import *
# ＝＝＝＝＝＝＝＝＝＝個別URLでスクレイピングする時＝＝＝＝＝＝＝＝＝＝
# 個別URLリストインスタンス
from setting_file.scraping_url.basic_scraping_url import URLS

# ファイルパス
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定 # file_path.py で定義したファイルディレクトリを指定
file_name = "scraped_data.csv"
output_file = os.path.join(file_directory, file_name)

# # スプレッドシート認証
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# credentials = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/STAFF1088/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/python-scrape.json", scope)
# gc = gspread.authorize(credentials)
# ヘッダー行の設定。ここではウェブページからスクレイプする項目名を列挙しています

# CSVヘッダー行の設定
header_row = ['URL', 'メーカー', '車種タイトル', '車輌本体価格(basePrice__content)', '走行距離', '年式(specList__jpYear)', '修復歴']
    
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



for url in URLS:
    # URLを使った処理
    print(f"Scraping {url}...")


# CSSセレクタの配列
CSS_selectors = [
    ('#app > div.model > section.c-marketprice', 'text'),  
    ('#app > div.model > section.c-content', 'text'),  
    # ('.cassetteMain__title a', 'text'),
    # # ('.cassetteMain__title a', 'link'),  # リンクを取得する場合
    # # ('.cassetteMain__title a', 'text', 'link'),  # リンクとテキストを同時に取得する場合
    # ('.basePrice__content', 'text'),  
    # ('div.cassetteWrap:nth-of-type(n+3) dt:-soup-contains("走行距離") + dd', 'text'),  
    # ('dt:-soup-contains("年式") + .specList__data span.specList__emphasisData', 'text'),  
    # ('.carListWrap dt:-soup-contains("修復歴") + dd', 'text')  
]

# アクセスエラー発生時の最大リトライ回数を設定
MAX_RETRIES = 10

# ウェブページの情報をスクレイプする関数
def scrape_url(url):
    delay_time = random.uniform(0.001, 0.005)  # リクエスト間のランダムな遅延時間を設定
    user_agent = random.choice(user_agents)  # リクエスト用のランダムなユーザーエージェントを選択
    retry_count = 0  # リトライ回数のカウンター

    while retry_count < MAX_RETRIES:
        try:
            # ユーザーエージェントを指定してURLにリクエストを送信
            response = requests.get(url, headers={'User-Agent': user_agent})

            if response.status_code == 200:
                # 正常にアクセスできた場合は遅延を挟んでループを抜ける
                time.sleep(delay_time)
                break
            else:
                # アクセスに失敗した場合はリトライ回数を増やして再度試行
                retry_count += 1
                continue
        except requests.RequestException as e:
            # アクセス中に例外が発生した場合、エラーメッセージをログに記録し、失敗を返す
            logging.error(f"Error occurred while accessing {url}: {str(e)}")
            return url, [], response.status_code

    else:
        # 最大リトライ回数に達した場合、失敗をログに記録し、失敗を返す
        logging.error(f"Failed to retrieve URL: {url}")
        return url, [], response.status_code

    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")
    
    # CSSセレクタの配列
    selectors = CSS_selectors

    scraped_data = [[] for _ in range(len(selectors))]
    
    # 各セレクターに対してスクレイピングを実行し、結果を保存
    for index, (selector, *data_types) in enumerate(selectors):
        elements = soup.select(selector)
        if elements:
            if 'link' in data_types:
                # リンクのテキストとURLを抽出
                scraped_data[index] = [(element.get('href', ''), element.get_text(strip=True)) for element in elements]
            else:
                # テキストのみを抽出
                scraped_data[index] = [element.get_text(strip=True).encode('utf-8').decode('utf-8') for element in elements]
        else:
            # セレクタに該当する要素が無い場合は空文字列を追加
            scraped_data[index] = ['nodata']

    time.sleep(delay_time)  # さらに遅延を挟む
    print(f'{delay_time}秒の遅延処理 / status code {response.status_code} {scraped_data}')
    return url, scraped_data, response.status_code

# スクレイピングの進捗をログに記録する関数
def log_progress(completed_count, total_count):
    percentage_complete = (completed_count / total_count) * 100
    print(f'{round(percentage_complete, 2)} % 完了.... {completed_count} / {total_count}')

# 完了したURLの数
completed_count = 0

# CSVファイルを開き、ヘッダーとスクレイプしたデータを書き込み、ログを出力
with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter = csv_delimiter)
    csv_writer.writerow(header_row)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # URLリストに対して並行してスクレイピングを実行
        for url in URLS:
            result = scrape_url(url)  # 各URLに対してスクレイピングを実行
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
