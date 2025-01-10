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
header_row = ['URL', 'テキスト1', 'テキスト2', 'テキスト3', 'テキスト4', 'テキスト5']

# スプレッドシート設定
# worksheet = gc.open("pythonscrape").sheet1


# スクレイピング対象の複数のURLをリストで定義  URL設定 URLリスト生成とセット のどちらか一方
urls = [
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501076/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501074/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501073/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501035/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501034/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501075/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501033/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501032/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501086/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501058/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501070/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501080/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501072/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502770/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502771/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502773/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502774/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502775/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502772/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502776/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502777/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502778/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502779/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502781/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502780/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502782/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502783/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502394/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502390/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502391/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502569/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502568/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502563/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502562/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502567/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502561/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502566/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502565/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502564/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502560/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502559/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502558/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502556/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502557/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502555/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502107/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502108/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501077/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501082/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501081/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501079/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501078/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502070/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502072/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502082/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502084/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502074/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502085/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502075/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502077/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502079/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502088/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502089/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502090/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502092/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502091/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502093/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502140/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502141/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502142/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502143/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502136/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502137/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502138/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502139/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502156/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502157/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502192/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502193/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502194/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501069/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502195/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501052/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501087/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501089/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501094/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501099/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501095/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501103/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501090/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501092/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501107/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501091/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501088/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501100/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501096/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501104/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501108/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501059/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501005/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501093/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501062/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501065/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502298/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502299/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502300/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502301/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502173/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502172/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502171/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502170/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501017/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501014/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501105/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501106/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501010/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501071/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501054/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501109/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501098/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501085/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501060/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501061/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501111/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501110/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501063/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501097/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501101/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501064/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501102/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501066/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501068/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501067/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501083/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501021/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501084/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502232/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502231/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502219/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502218/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502212/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502214/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502217/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502215/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502210/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502209/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501055/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501056/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501045/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501015/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501020/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501006/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501030/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501019/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501007/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501016/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501008/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501025/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501026/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501009/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501027/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501011/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501012/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501028/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501029/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501013/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501018/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501023/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501024/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502230/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502229/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502228/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502227/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502223/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502222/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502221/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4502220/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/10000078/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501036/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501046/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501047/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501048/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501049/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501038/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501050/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501051/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501039/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501040/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501022/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501041/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501053/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501042/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501043/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501057/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501044/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501031/',
'https://www.goo-net.com/catalog/SUBARU/LEGACY/4501037/'
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
        ('#main > div.hl.tit_first > h2', 'text'),
        ('#main > div:nth-child(4) > div > div > div > div.newCar > div > p', 'text'),
        ('#main > div:nth-child(5) > div > div > div > div.newCar > div > p', 'text'),
        ('.box_presentSpec th', 'text'),
        ('.box_presentSpec td', 'text')
        # ('.box_spec table:nth-of-type(1) th', 'text'),
        # ('.box_spec table:nth-of-type(1) td', 'text')
    ]
    
    # スクレイピングデータのリストを初期化
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
