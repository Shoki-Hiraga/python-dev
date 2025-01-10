from setting_file.header import *


# ファイルパス
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定 # file_path.py で定義したファイルディレクトリを指定
file_name = "scraped_data.csv"
output_file = os.path.join(file_directory, file_name)

# # スプレッドシート認証
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# credentials = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/STAFF1088/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/python-scrape.json", scope)
# gc = gspread.authorize(credentials)
# ヘッダー行の設定。ここではウェブページからスクレイプする項目名を列挙しています


header_row = ['URL', 'メーカー', '車種タイトル', '車輌本体価格(basePrice__content)', '走行距離', '年式(specList__jpYear)', '修復歴']

# パラメータの設定
parameter = "" # パラメーター無しの場合は空白
pagenation_min = 1
pagenation_max = 4

# # URLリストの生成
# base_url = "https://www.carsensor.net/usedcar/bNI/s054/index{}.html"
# urls = [base_url.format(i) + parameter for i in range(pagenation_min, pagenation_max + 1)]

# 個別URLリストインスタンス
urls = [
'https://www.qsha-oh.com/maker/nissan/silvia_s14/',
'https://www.qsha-oh.com/maker/nissan/cherry/',
'https://www.qsha-oh.com/maker/nissan/gloria_wagon/',
'https://www.qsha-oh.com/maker/nissan/leopard/',
'https://www.qsha-oh.com/maker/nissan/safari/',
'https://www.qsha-oh.com/maker/nissan/micra-c-c/',
'https://www.qsha-oh.com/maker/nissan/x-trail-t31/',
'https://www.qsha-oh.com/maker/nissan/nv200-vanetter-wagon/',
'https://www.qsha-oh.com/maker/nissan/lucino/',
'https://www.qsha-oh.com/maker/nissan/laurel-c-130/',
'https://www.qsha-oh.com/maker/nissan/figaro/',
'https://www.qsha-oh.com/maker/nissan/civilian/',
'https://www.qsha-oh.com/maker/nissan/pulsar/',
'https://www.qsha-oh.com/maker/nissan/180sx/',
'https://www.qsha-oh.com/maker/nissan/c33-laurel/',
'https://www.qsha-oh.com/maker/nissan/hakosuka/',
'https://www.qsha-oh.com/maker/nissan/y31-cima/',
'https://www.qsha-oh.com/maker/nissan/skyline_coupe/',
'https://www.qsha-oh.com/maker/nissan/fairladyz_z33/',
'https://www.qsha-oh.com/maker/nissan/caravan-e25/',
'https://www.qsha-oh.com/maker/nissan/cima-f50/',
'https://www.qsha-oh.com/maker/nissan/r33-skyline/',
'https://www.qsha-oh.com/maker/nissan/terrano-wd21/',
'https://www.qsha-oh.com/maker/nissan/murano-z51/',
'https://www.qsha-oh.com/maker/nissan/safari-y61/',
'https://www.qsha-oh.com/maker/nissan/r32-skyline/',
'https://www.qsha-oh.com/maker/nissan/fairladyz-z31/',
'https://www.qsha-oh.com/maker/nissan/silvia_s15/',
'https://www.qsha-oh.com/maker/nissan/stagea/',
'https://www.qsha-oh.com/maker/nissan/silvia-autech-version/',
'https://www.qsha-oh.com/maker/nissan/r33-skyline-gtr/',
'https://www.qsha-oh.com/maker/nissan/r34-skyline/',
'https://www.qsha-oh.com/maker/nissan/silvia_s13/',
'https://www.qsha-oh.com/maker/nissan/maxima/',
'https://www.qsha-oh.com/maker/nissan/nx_coupe/',
'https://www.qsha-oh.com/maker/nissan/primera/',
'https://www.qsha-oh.com/maker/nissan/safari-y60/',
'https://www.qsha-oh.com/maker/nissan/condor/',
'https://www.qsha-oh.com/maker/nissan/r32-skyline-gtr/',
'https://www.qsha-oh.com/maker/nissan/cedric-y31/',
'https://www.qsha-oh.com/maker/nissan/sunny-coupe/',
'https://www.qsha-oh.com/maker/nissan/fairladyz_z32/',
'https://www.qsha-oh.com/maker/nissan/r35-gt-r-nismo/',
'https://www.qsha-oh.com/maker/nissan/sunny/',
'https://www.qsha-oh.com/maker/nissan/stagea-autech-version-260rs/',
'https://www.qsha-oh.com/maker/nissan/cima/',
'https://www.qsha-oh.com/maker/nissan/exa/',
'https://www.qsha-oh.com/maker/nissan/skyline-coupe-ckv36/',
'https://www.qsha-oh.com/maker/nissan/cedric330/',
'https://www.qsha-oh.com/maker/nissan/fairladyz_z34/',
'https://www.qsha-oh.com/maker/nissan/infiniti-q45/',
'https://www.qsha-oh.com/maker/nissan/caravan/',
'https://www.qsha-oh.com/maker/nissan/kenmeri-yonmeri/',
'https://www.qsha-oh.com/maker/nissan/elgrand-e52/',
'https://www.qsha-oh.com/maker/nissan/430-cedric/',
'https://www.qsha-oh.com/maker/nissan/president/',
'https://www.qsha-oh.com/maker/nissan/r31-skyline-gts-r/',
'https://www.qsha-oh.com/maker/nissan/bluebird-sss/',
'https://www.qsha-oh.com/maker/nissan/vanette/',
'https://www.qsha-oh.com/maker/nissan/sunny-truck/',
'https://www.qsha-oh.com/maker/nissan/c35-laurel/',
'https://www.qsha-oh.com/maker/nissan/skyline-gts-t-type-m/',
'https://www.qsha-oh.com/maker/nissan/largo/',
'https://www.qsha-oh.com/maker/nissan/march-12sr/',
'https://www.qsha-oh.com/maker/nissan/r34-skyline-gtr/',
'https://www.qsha-oh.com/maker/nissan/hakosuka-gt-r/',
'https://www.qsha-oh.com/maker/nissan/nt100-clipper/',
'https://www.qsha-oh.com/maker/nissan/stagea-wc34/',
'https://www.qsha-oh.com/maker/nissan/gloria/',
'https://www.qsha-oh.com/maker/nissan/caravan-e24/',
'https://www.qsha-oh.com/maker/nissan/bluebird/',
'https://www.qsha-oh.com/maker/nissan/cedric_wagon/',
'https://www.qsha-oh.com/maker/nissan/nv200-vanette/',
'https://www.qsha-oh.com/maker/nissan/r35_gt-r/',
'https://www.qsha-oh.com/maker/nissan/r31-skyline/',
'https://www.qsha-oh.com/maker/nissan/cedric/',
'https://www.qsha-oh.com/maker/nissan/b310-sunny/',
'https://www.qsha-oh.com/maker/nissan/skyline-25gt-turbo/',
'https://www.qsha-oh.com/maker/nissan/fuga/',
'https://www.qsha-oh.com/maker/nissan/frontier/',
'https://www.qsha-oh.com/maker/nissan/x-trail/',
'https://www.qsha-oh.com/maker/nissan/rasheen/',
'https://www.qsha-oh.com/maker/nissan/silvia-csp311/',
'https://www.qsha-oh.com/maker/nissan/fairladyz/',
'https://www.qsha-oh.com/maker/nissan/primera-p10/',
'https://www.qsha-oh.com/maker/nissan/datsun-truck/',
'https://www.qsha-oh.com/maker/nissan/leaf/',
'https://www.qsha-oh.com/maker/nissan/x-trail-20gt/',
'https://www.qsha-oh.com/maker/nissan/180sx-type-x/',
'https://www.qsha-oh.com/maker/nissan/y30-gloria-brougham-turbo/',
'https://www.qsha-oh.com/maker/nissan/laurel-c130/',
'https://www.qsha-oh.com/maker/nissan/stagea-25t-rs-four-v/',
'https://www.qsha-oh.com/maker/nissan/kix/',
'https://www.qsha-oh.com/maker/nissan/f31-leopard/',
'https://www.qsha-oh.com/maker/nissan/y30-cedric-brougham-turbo/',
'https://www.qsha-oh.com/maker/nissan/fairladyz-z34-version-nismo/',
'https://www.qsha-oh.com/maker/nissan/elgrand-rider-e51-me51/',
'https://www.qsha-oh.com/maker/nissan/be-1/',
'https://www.qsha-oh.com/maker/nissan/r30-skyline/',
'https://www.qsha-oh.com/maker/nissan/silvia-varietta/',
'https://www.qsha-oh.com/maker/nissan/stanza/',
'https://www.qsha-oh.com/maker/nissan/230-cedric/',
'https://www.qsha-oh.com/maker/nissan/r33-skyline-gtr-autech-version/',
'https://www.qsha-oh.com/maker/nissan/fairladyz-z33-version-nismo/',
'https://www.qsha-oh.com/maker/nissan/pao/',
'https://www.qsha-oh.com/maker/nissan/vanette-truck/',
'https://www.qsha-oh.com/maker/nissan/terrano/',
'https://www.qsha-oh.com/maker/nissan/silvia/'
]
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
        ('#app > div.model > section.c-marketprice', 'text'),  
        ('#app > div.model > section.c-content', 'text')
        # ('.cassetteMain__carInfoContainer > p:nth-of-type(1)', 'text'),  
        # ('.cassetteMain__title a', 'text'),
        # # ('.cassetteMain__title a', 'link'),  # リンクを取得する場合
        # # ('.cassetteMain__title a', 'text', 'link'),  # リンクとテキストを同時に取得する場合
        # ('.basePrice__content', 'text'),  
        # ('div.cassetteWrap:nth-of-type(n+3) dt:-soup-contains("走行距離") + dd', 'text'),  
        # ('dt:-soup-contains("年式") + .specList__data span.specList__emphasisData', 'text'),  
        # ('.carListWrap dt:-soup-contains("修復歴") + dd', 'text')  
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
