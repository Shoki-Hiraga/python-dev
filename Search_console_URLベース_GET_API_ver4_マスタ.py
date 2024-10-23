from setting_file.header import *

# # スプレッドシート認証
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# credentials = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/STAFF1088/AppData/Local/Programs/Python/python-scrape.json', scope)
# gc = gspread.authorize(credentials)

# # スプレッドシート設定
# worksheet = gc.open("Python_scrape_API").sheet1


# ファイルパス
csv_directory = csv_output_path.out_office
# csv_directory = csv_output_path.out_main
# csv_directory = csv_output_path.out_raytrek
csv_filename = "Search Console_API_URL.csv"
output_file = os.path.join(csv_directory, csv_filename)

# URLごとに出力するCSVファイルのファイル名
header_row = ['URL', '検索クエリ', '表示回数', 'クリック数', 'クリック率', '掲載順位']

# 対象のサイトURLを指定します
site_url = 'https://www.qsha-oh.com/'


# JSONファイルのパスを指定
SERVICE_ACCOUNT_FILE = api_json.qsha_oh

# Search Console APIの認証情報を指定
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/webmasters.readonly']
)

# Search Console APIのバージョンとプロジェクトIDを指定します
api_version = 'v3'
service = build('webmasters', api_version, credentials=credentials)

# 指定したURLに一致したデータを取得する関数を定義します
def get_search_url_data(site_url, page_url):
    request = {
        'startDate': '2024-08-01',
        'endDate': '2024-08-31',
        'dimensions': ['page', 'query'],  # 'query'を追加して検索クエリを取得するようにします
        'searchType': 'web',
        'dimensionFilterGroups': [{
            'filters': [{
                'dimension': 'page',
                'operator': 'equals',
                # 'operator': 'contains',
                'expression': page_url
            }]
        }]
    }

    try:
        response = service.searchanalytics().query(siteUrl=site_url, body=request).execute()
        return response.get('rows', []), page_url
    except Exception as e:
        print(f'Error retrieving data for URL {page_url}: {e}')
        return [], page_url


# 複数のURLを指定します
urls = [
"https://www.qsha-oh.com/aging-paintcar/",
"https://www.qsha-oh.com/amesha/",
"https://www.qsha-oh.com/classic-supercar/",
"https://www.qsha-oh.com/custom/",
"https://www.qsha-oh.com/damage/",
"https://www.qsha-oh.com/immobile/",
"https://www.qsha-oh.com/itasha/",
"https://www.qsha-oh.com/landcruiser/",
"https://www.qsha-oh.com/ninemania/",
"https://www.qsha-oh.com/other/",
"https://www.qsha-oh.com/repair/",
"https://www.qsha-oh.com/skyoh/",
"https://www.qsha-oh.com/souzoku/",
"https://www.qsha-oh.com/sportscar/",
"https://www.qsha-oh.com/submerged-car/"
]

try:
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # ヘッダー行を書き込む
        csv_writer.writerow(header_row)
        # # スプレッドシートにヘッダー行を書き込む
        # worksheet.append_row(header_row, value_input_option='USER_ENTERED')

        for url in urls:
            # URLの統計情報を取得
            search_url_data, original_url = get_search_url_data(site_url, url)

            # ランダムな遅延処理を追加
            delay = random.uniform(1.5, 2.5)
            print(f'遅延処理 {delay} 秒')
            time.sleep(delay)

            if not search_url_data:  # データがない場合
                csv_writer.writerow([original_url, '', '0', '0', '0', '0'])
                # worksheet.append_row([original_url, '', '0', '0', '0', '0'])
                print(f'URL: {original_url}, データがありません')
            else:
                for row in search_url_data:
                    page_url = row['keys'][0]
                    query = row['keys'][1]
                    impressions = row.get('impressions', '-')
                    clicks = row.get('clicks', '-')
                    ctr = row.get('ctr', '-')
                    position = row.get('position', '-')

                    # CSVファイルに書き込む
                    csv_writer.writerow([page_url, query, impressions, clicks, ctr, position])

                    # # スプレッドシートに書き込む
                    # worksheet.append_row([page_url, query, impressions, clicks, ctr, position])

                    print(f'URL: {page_url}, 検索クエリ: {query}, 表示回数: {impressions}, クリック数: {clicks}, クリック率: {ctr}, 平均掲載順位: {position}')

    print(f'CSVファイルを以下のディレクトリにエクスポートしました: {output_file}')

except Exception as err:
    print(f'An error occurred: {err}')
