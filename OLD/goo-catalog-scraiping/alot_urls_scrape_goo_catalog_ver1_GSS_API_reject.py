from setting_file.header import *

# ファイルパス
csv_directory = csv_output_path.out_office
# csv_directory = csv_output_path.out_main
# csv_directory = csv_output_path.out_raytrek
csv_filename = "scraped_data.csv"
output_file = os.path.join(csv_directory, csv_filename)

# # スプレッドシート認証
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# credentials = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/STAFF1088/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/python-scrape.json", scope)
# gc = gspread.authorize(credentials)


# ヘッダー行
header_row = ['URL', 'テキスト1', 'テキスト2', 'テキスト3', 'テキスト4']

# スクレイピング対象の複数のURLをリストで定義  URL設定 URLリスト生成とセット のどちらか一方
urls = [
"https://www.goo-net.com/catalog/TOYOTA/PRIUS/10147875/",
"https://www.goo-net.com/catalog/TOYOTA/COROLLA_LEVIN/1002383/"
]


# # URL設定 URLリスト生成とセット
# base_url = 'https://www.carsensor.net/catalog/toyota/page'
# start_page = '1'
# end_page = '2'
# additional_directory = '/'
# query_params_template = ''  # パラメーターページ番号の際はページ番号部分{}とする (?p={}&o=t1)
# # パラメーターページ番号
# query_start_page = ''
# query_end_page = ''

# # URLリスト生成
# urls = []

# # URL内ページに対応
# if start_page and end_page:
#     urls.extend([f'{base_url}{page_num}{additional_directory}{query_params_template.format(page_num)}' for page_num in range(int(start_page), int(end_page) + 1)])
# else:
#     urls.extend([f'{base_url}{additional_directory}{query_params_template.format("")}'])

# # パラメーター内ページに対応
# if query_start_page and query_end_page:
#     urls.extend([f'{base_url}{query_params_template.format(page_num)}' for page_num in range(int(query_start_page), int(query_end_page) + 1)])
# else:
#     urls.extend([f'{base_url}{query_params_template.format("")}'])


# スプレッドシート設定
# worksheet = gc.open("pythonscrape").sheet1

# アクセスエラー発生時の最大リトライ回数を設定
MAX_RETRIES = 10

# ウェブページの情報をスクレイプする関数
def scrape_url(url):
    delay_time = random.uniform(1, 5)  # リクエスト間のランダムな遅延時間を設定
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
    selectors = [
        ('.box_presentSpec th', 'text'),
        ('.box_presentSpec td', 'text'),
        ('.box_spec table:nth-of-type(1) th', 'text'),
        ('.box_spec table:nth-of-type(1) td', 'text')
    ]

    scraped_data = [[] for _ in range(len(selectors))]
    
    # 各セレクターに対してスクレイピングを実行し、結果を保存
    for index, (selector, *data_types) in enumerate(selectors):
        elements = soup.select(selector)
        if 'link' in data_types:
            # リンクのテキストとURLを抽出
            scraped_data[index] = [(element.get('href', ''), element.get_text(strip=True)) for element in elements]
        else:
            # テキストのみを抽出
            scraped_data[index] = [element.get_text(strip=True).encode('utf-8').decode('utf-8') for element in elements]
    
    time.sleep(delay_time)  # さらに遅延を挟む
    print(f'{delay_time}秒の遅延処理 / status code{response.status_code} {scraped_data}')
    return url, scraped_data, response.status_code



# スクレイピングの進捗をログに記録する関数
def log_progress(completed_count, total_count):
    percentage_complete = (completed_count / total_count) * 100
    print(f'{round(percentage_complete, 2)} % 完了.... {completed_count} / {total_count}')

# 完了したURLの数
completed_count = 0

# CSVファイルを開き、ヘッダーとスクレイプしたデータを書き込み、ログを出力
with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header_row)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # URLリストに対して並行してスクレイピングを実行
        for url in urls:
            result = scrape_url(url)  # 各URLに対してスクレイピングを実行
            url, scraped_data, status_code = result
            max_length = max(len(data) for data in scraped_data)  # 最大の列数を取得
            
            # スクレイプしたデータを行としてCSVに書き込む
            for i in range(max_length):
                row_data = [url] + [data[i] if i < len(data) else '' for data in scraped_data] + [status_code]
                csv_writer.writerow(row_data)

            completed_count += 1  # 完了したURLの数を更新
            log_progress(completed_count, len(urls))  # 進捗のログ

            print(f'{header_row[0]}: {url}')  # 完了したURLを表示
            print(' ')
            print('--------------------------------------------')

print('スクレイピングが完了しました。')  # 全てのスクレイピングが完了したことを通知
