import requests
from bs4 import BeautifulSoup
import time
import csv
import os
import concurrent.futures
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sys
import random

# # スプレッドシート認証
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# credentials = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/STAFF1088/AppData/Local/Programs/Python/python-scrape.json', scope)
# gc = gspread.authorize(credentials)



# スクレイピング対象の複数のURLをリストで定義  URL設定 URLリスト生成とセット のどちらか一方
urls = [
'https://www.qsha-oh.com/maker/toyota/80_supra/',
'https://www.qsha-oh.com/maker/nissan/silvia_s13/',
'https://www.qsha-oh.com/maker/nissan/silvia_s14/',
'https://www.qsha-oh.com/maker/nissan/silvia_s15/',
'https://www.qsha-oh.com/maker/toyota/mr2_aw11/',
'https://www.qsha-oh.com/maker/toyota/mr2/',
'https://www.qsha-oh.com/maker/honda/s2000_ap1/',
'https://www.qsha-oh.com/maker/honda/s2000_ap2/',
'https://www.qsha-oh.com/maker/nissan/180sx/',
'https://www.qsha-oh.com/maker/nissan/180sx-type-x/',
'https://www.qsha-oh.com/maker/nissan/180sx-type-x//',
'https://www.qsha-oh.com/maker/nissan/180sx//',
'https://www.qsha-oh.com/maker/nissan/r32-skyline-gtr/',
'https://www.qsha-oh.com/maker/nissan/r34-skyline-gtr/',
'https://www.qsha-oh.com/maker/toyota/86-2/',
'https://www.qsha-oh.com/maker/subaru/impreza_wrx-sti_gc8/',
'https://www.qsha-oh.com/maker/honda/integra_type-r_dc2/',
'https://www.qsha-oh.com/maker/honda/civic_type-r_ek9/',
'https://www.qsha-oh.com/maker/honda/civic_type-r_fd2/',
'https://www.qsha-oh.com/maker/honda/mugen-rr/',
'https://www.qsha-oh.com/maker/honda/civic-type-r-ep3/',
'https://www.qsha-oh.com/maker/honda/civic-type-r-euro/',
'https://www.qsha-oh.com/maker/honda/civic-type-r-fk8/',
'https://www.qsha-oh.com/maker/nissan/r34-skyline/',
'https://www.qsha-oh.com/maker/mitsubishi/lancer_evolution_6/',
'https://www.qsha-oh.com/maker/mitsubishi/lancer_evolution_9/',
'https://www.qsha-oh.com/maker/mitsubishi/lancer_wagon_evolution/',
'https://www.qsha-oh.com/maker/mitsubishi/jeep/',
'https://www.qsha-oh.com/maker/mitsubishi/colt_ralliart_version-r/',
'https://www.qsha-oh.com/maker/mitsubishi/lancer-evolution-5/',
'https://www.qsha-oh.com/maker/mitsubishi/lancer-evolution-4/',
'https://www.qsha-oh.com/maker/mitsubishi/lancer-evolution-3/',
'https://www.qsha-oh.com/maker/mitsubishi/lancer_evolution_finaledition/',
'https://www.qsha-oh.com/maker/mitsubishi/lancer_evolution_10/',
'https://www.qsha-oh.com/maker/mitsubishi/lancer_evolution_8/',
'https://www.qsha-oh.com/maker/mitsubishi/lancer_evolution_7/',
'https://www.qsha-oh.com/maker/mitsubishi/lancer-evolution-2/',
'https://www.qsha-oh.com/maker/nissan/silvia-autech-version/',
'https://www.qsha-oh.com/maker/nissan/silvia-varietta/',
'https://www.qsha-oh.com/maker/nissan/silvia-csp311/',
'https://www.qsha-oh.com/maker/eunos/eunos-roadster/',
'https://www.qsha-oh.com/maker/subaru/impreza_wrx-sti_gdb/',
'https://www.qsha-oh.com/maker/subaru/impreza_22b-sti_version/',
'https://www.qsha-oh.com/maker/bmw/z4-e89/',
'https://www.qsha-oh.com/maker/nissan/fairladyz_z32/',
'https://www.qsha-oh.com/maker/nissan/fairladyz-z33-version-nismo/',
'https://www.qsha-oh.com/maker/nissan/fairladyz-z34-version-nismo/',
'https://www.qsha-oh.com/maker/nissan/r33-skyline-gtr/',
'https://www.qsha-oh.com/maker/nissan/r33-skyline-gtr-autech-version/',
'https://www.qsha-oh.com/maker/honda/nsx/',
'https://www.qsha-oh.com/maker/honda/nsx-type-r/',
'https://www.qsha-oh.com/maker/toyota/70-supra/',
'https://www.qsha-oh.com/maker/nissan/fairladyz_z33/',
'https://www.qsha-oh.com/maker/nissan/fairladyz_z34/',
'https://www.qsha-oh.com/maker/nissan/s30z/',
'https://www.qsha-oh.com/maker/nissan/fairlady-z-gs30/',
'https://www.qsha-oh.com/maker/nissan/fairladyz-130z/',
'https://www.qsha-oh.com/maker/mazda/rx-7/',
'https://www.qsha-oh.com/maker/mazda/rx-8/',
'https://www.qsha-oh.com/maker/mazda/rx-8-spirit-r/',
'https://www.qsha-oh.com/maker/honda/integra-type-r-db8/',
'https://www.qsha-oh.com/maker/toyota/sprinter_trueno/',
'https://www.qsha-oh.com/maker/toyota/altezza/',
'https://www.qsha-oh.com/maker/nissan/fairladyz-z31/'
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



# ヘッダー行
header_row = ['URL', 'テキスト1','テキスト2']

# ファイルパス
csv_directory = 'C:/Users/STAFF1088/Downloads'
csv_filename = "sobakehai.csv"
csv_filepath = os.path.join(csv_directory, csv_filename)

# # スプレッドシート設定
# worksheet = gc.open("sobakehai_scrape").sheet1

# スクレイピング関数
def scrape_url(url):
    response = requests.get(url)
    response.encoding = response.apparent_encoding  # サイトのエンコーディングを自動検出
    delay_time = random.uniform(10.6, 40.8)
    time.sleep(delay_time)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # CSSセレクタの配列
    selectors = [
        ('div.c-marketprice-v2__table__body__item__cell:nth-of-type(2)', 'text'),  
        ('div.c-marketprice-v2__table__body__item__cell:nth-of-type(1)', 'text')

    ]
    
    # スクレイピングデータのリストを初期化
    scraped_data = [[] for _ in range(len(selectors))]
    
    # セレクタごとにデータを取得
    for index, (selector, *data_types) in enumerate(selectors):
        elements = soup.select(selector)
        if 'link' in data_types:
            # リンクを取得する場合
            scraped_data[index] = [(element.get('href', ''), element.get_text(strip=True)) for element in elements]
        else:
            # テキストを取得する場合
            # UTF-8にエンコードしてからデコード
            scraped_data[index] = [element.get_text(strip=True).encode('utf-8').decode('utf-8') for element in elements] 
    
    # データを返す
    return url, scraped_data


# タブ区切りCSVファイルとスプレッドシートに書き込み
with open(csv_filepath, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # ヘッダー行を書き込む
    csv_writer.writerow(header_row)

    # # スプレッドシートにヘッダー行を書き込む
    # worksheet.append_row(header_row, value_input_option='USER_ENTERED')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(scrape_url, urls)

        for result in results:
            url, scraped_data = result
            max_length = max(len(data) for data in scraped_data)

            for i in range(max_length):
                row_data = [url] + [data[i] if i < len(data) else '' for data in scraped_data]
                csv_writer.writerow(row_data)
                # worksheet.append_row(row_data, value_input_option='USER_ENTERED')

                # ターミナル出力
                print(f'{header_row[0]}: {url}')
                for i, column in enumerate(header_row[1:], start=1):
                    print(f'{column}: {scraped_data[i-1]}')
                print('--------------------------------------------')
                sys.stdout.flush()  # バッファリングを無効にして即座に出力を表示

print('スクレイピングが完了しました。')


