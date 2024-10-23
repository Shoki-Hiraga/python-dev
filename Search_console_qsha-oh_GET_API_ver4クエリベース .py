from setting_file.header import *

# # スプレッドシート認証
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# credentials = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/STAFF1088/AppData/Local/Programs/Python/python-scrape.json', scope)
# gc = gspread.authorize(credentials)

# # スプレッドシート設定
# worksheet = gc.open("Python_scrape_API").sheet1


# ファイルパス
# csv_directory = csv_output_path.out_office
csv_directory = csv_output_path.out_main
# csv_directory = csv_output_path.out_raytrek
csv_filename = "Camp定点観測.csv"
output_file = os.path.join(csv_directory, csv_filename)


# JSONファイルのパスを指定
SERVICE_ACCOUNT_FILE = api_json.camp

# Search Console APIの認証情報を指定
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/webmasters.readonly']
)

# Search Console APIのバージョンとプロジェクトIDを指定します
api_version = 'v3'
service = build('webmasters', api_version, credentials=credentials)

# 検索クエリに一致したデータを取得する関数を定義します
def get_search_query_data(site_url, query):
    request = {
        'startDate': '2023-12-01',
        'endDate': '2024-01-01',
        'dimensions': ['query'],
        'searchType': 'web',
        'dimensionFilterGroups': [{
            'filters': [{
                'dimension': 'query',
                # 'operator': 'equals',  # 完全一致
                'operator': 'contains',  # 部分一致
                # 'operator': 'notcontains',  # 部分未一致
                'expression': query
            }]
        }]
    }

    try:
        response = service.searchanalytics().query(siteUrl=site_url, body=request).execute()
        return response.get('rows', []), query
    except Exception as e:
        print(f'Error retrieving data for query {query}: {e}')
        return [], query

header_row = ['検索クエリ', '表示回数', 'クリック数', 'クリック率', '掲載順位']
# # スプレッドシート設定
# worksheet = gc.open("Python_scrape_API").sheet1
# 対象のサイトURLを指定します
site_url = 'https://camp.garagecurrent.com/'

# 複数の検索クエリを指定します
queries = [
'アドリア 評判',
'ケイワークス 評判',
'atoz 評判',
'カトーモーター 評判',
'セキソーボディ 評判',
'アネックス 評判',
'ドリーム・エーティー 評判',
'バンテック 評判',
'ファンルーチェ 評判',
'インディアナRV 評判',
'キャンパー厚木 評判',
'バンショップミカミ 評判'
    ]

# 全体の結果を格納するリストを作成
all_results = []

# CSVファイルのヘッダー行を書き込む
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header_row)
    # # スプレッドシートにヘッダー行を書き込む
    # worksheet.append_row(header_row, value_input_option='USER_ENTERED')

try:
    for query in queries:
        # クエリの統計情報を取得
        search_query_data, original_query = get_search_query_data(site_url, query)

        # ランダムな遅延処理を追加
        delay = random.uniform(1.5, 3.5)
        print(f'遅延処理 {delay} 秒')
        time.sleep(delay)

        # 結果をCSVファイルに追加
        with open(output_file, 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)

            if not search_query_data:  # データがない場合
                csv_writer.writerow([original_query, '0', '0', '0', '0'])
                # worksheet.append_row([original_query, '0', '0', '0', '0'])

                print(f'検索クエリ: {original_query}, データがありません')
            else:
                for row in search_query_data:
                    query = row['keys'][0]
                    impressions = row.get('impressions', '-')
                    clicks = row.get('clicks', '-')
                    ctr = row.get('ctr', '-')
                    position = row.get('position', '-')
                    csv_writer.writerow([query, impressions, clicks, ctr, position])
                    # worksheet.append_row([query, impressions, clicks, ctr, position])
                    print(f'検索クエリ: {query}, 表示回数: {impressions}, クリック数: {clicks}, クリック率: {ctr}, 掲載順位: {position}')

    print(f'CSVファイルを以下のディレクトリにエクスポートしました: {output_file}')

except Exception as err:
    print(f'An error occurred: {err}')
