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
csv_filename = "summary_data.csv"
output_file = os.path.join(csv_directory, csv_filename)

header_row = ['URL', '合計表示回数', '合計クリック数', '平均CTR', '平均掲載順位']


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
        'startDate': '2023-04-01',
        'endDate': '2023-07-31',
        'dimensions': ['page'],
        'searchType': 'web',
        'dimensionFilterGroups': [{
            'filters': [{
                'dimension': 'page',
                # 完全一致
                'operator': 'equals',
                # 部分一致
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
'https://www.qsha-oh.com/'
# 'https://www.qsha-oh.com/maker/toyota/',
# 'https://www.qsha-oh.com/maker/nissan/',
# 'https://www.qsha-oh.com/maker/honda/',
# 'https://www.qsha-oh.com/maker/mazda/',
# 'https://www.qsha-oh.com/maker/subaru/',
# 'https://www.qsha-oh.com/maker/mitsubishi/',
# 'https://www.qsha-oh.com/maker/lexus/',
# 'https://www.qsha-oh.com/maker/datsun/',
# 'https://www.qsha-oh.com/maker/prince/',
# 'https://www.qsha-oh.com/maker/eunos/',
# 'https://www.qsha-oh.com/maker/tommy-kaira/',
# 'https://www.qsha-oh.com/maker/mitsuoka/',
# 'https://www.qsha-oh.com/maker/daihatsu/',
# 'https://www.qsha-oh.com/maker/dome/',
# 'https://www.qsha-oh.com/maker/hino/',
# 'https://www.qsha-oh.com/maker/isuzu/',
# 'https://www.qsha-oh.com/maker/suzuki/',
# 'https://www.qsha-oh.com/maker/porsche/',
# 'https://www.qsha-oh.com/maker/ruf/',
# 'https://www.qsha-oh.com/maker/benz/',
# 'https://www.qsha-oh.com/maker/brabus/',
# 'https://www.qsha-oh.com/maker/alpina/',
# 'https://www.qsha-oh.com/maker/bmw/',
# 'https://www.qsha-oh.com/maker/amg/',
# 'https://www.qsha-oh.com/maker/gemballa/',
# 'https://www.qsha-oh.com/maker/audi/',
# 'https://www.qsha-oh.com/maker/volkswagen/',
# 'https://www.qsha-oh.com/maker/opel/',
# 'https://www.qsha-oh.com/maker/bmw-mini/',
# 'https://www.qsha-oh.com/maker/maybach/',
# 'https://www.qsha-oh.com/maker/rolls-royce/',
# 'https://www.qsha-oh.com/maker/astonmartin/',
# 'https://www.qsha-oh.com/maker/bentley/',
# 'https://www.qsha-oh.com/maker/caterham/',
# 'https://www.qsha-oh.com/maker/rover/',
# 'https://www.qsha-oh.com/maker/jaguar-cars/',
# 'https://www.qsha-oh.com/maker/lotus/',
# 'https://www.qsha-oh.com/maker/mclaren/',
# 'https://www.qsha-oh.com/maker/triumph/',
# 'https://www.qsha-oh.com/maker/tvr/',
# 'https://www.qsha-oh.com/maker/bristol-cars/',
# 'https://www.qsha-oh.com/maker/land-rover/',
# 'https://www.qsha-oh.com/maker/vandenplas/',
# 'https://www.qsha-oh.com/maker/ginetta/',
# 'https://www.qsha-oh.com/maker/morgan/',
# 'https://www.qsha-oh.com/maker/mg/',
# 'https://www.qsha-oh.com/maker/sunbeam/',
# 'https://www.qsha-oh.com/maker/daimler/',
# 'https://www.qsha-oh.com/maker/morris/',
# 'https://www.qsha-oh.com/maker/austin/',
# 'https://www.qsha-oh.com/maker/riley/',
# 'https://www.qsha-oh.com/maker/bl/',
# 'https://www.qsha-oh.com/maker/innocenti/',
# 'https://www.qsha-oh.com/maker/panther/',
# 'https://www.qsha-oh.com/maker/westfield/',
# 'https://www.qsha-oh.com/maker/dodge/',
# 'https://www.qsha-oh.com/maker/ford/',
# 'https://www.qsha-oh.com/maker/chevrolet/',
# 'https://www.qsha-oh.com/maker/ac-cars/',
# 'https://www.qsha-oh.com/maker/chrysler/',
# 'https://www.qsha-oh.com/maker/gmc/',
# 'https://www.qsha-oh.com/maker/cadillac/',
# 'https://www.qsha-oh.com/maker/jeep/',
# 'https://www.qsha-oh.com/maker/hummer/',
# 'https://www.qsha-oh.com/maker/mercury/',
# 'https://www.qsha-oh.com/maker/pontiac/',
# 'https://www.qsha-oh.com/maker/shelby-american/',
# 'https://www.qsha-oh.com/maker/buick/',
# 'https://www.qsha-oh.com/maker/lincoln/',
# 'https://www.qsha-oh.com/maker/oldsmobile/',
# 'https://www.qsha-oh.com/maker/dmc/',
# 'https://www.qsha-oh.com/maker/excalibur/',
# 'https://www.qsha-oh.com/maker/us-toyota/',
# 'https://www.qsha-oh.com/maker/acura/',
# 'https://www.qsha-oh.com/maker/us-nissan/',
# 'https://www.qsha-oh.com/maker/us-lexus/',
# 'https://www.qsha-oh.com/maker/tesla/',
# 'https://www.qsha-oh.com/maker/us-honda/',
# 'https://www.qsha-oh.com/maker/plymouth/',
# 'https://www.qsha-oh.com/maker/us-mazda/',
# 'https://www.qsha-oh.com/maker/us-suzuki/',
# 'https://www.qsha-oh.com/maker/amc/',
# 'https://www.qsha-oh.com/maker/amc-jeep/',
# 'https://www.qsha-oh.com/maker/willys/',
# 'https://www.qsha-oh.com/maker/lamborghini/',
# 'https://www.qsha-oh.com/maker/ferrari/',
# 'https://www.qsha-oh.com/maker/alfaromeo/',
# 'https://www.qsha-oh.com/maker/fiat/',
# 'https://www.qsha-oh.com/maker/maserati/',
# 'https://www.qsha-oh.com/maker/lancia/',
# 'https://www.qsha-oh.com/maker/abarth/',
# 'https://www.qsha-oh.com/maker/de-tomaso/',
# 'https://www.qsha-oh.com/maker/italdesign/',
# 'https://www.qsha-oh.com/maker/autobianchi/',
# 'https://www.qsha-oh.com/maker/citroen/',
# 'https://www.qsha-oh.com/maker/peugeot/',
# 'https://www.qsha-oh.com/maker/renault/',
# 'https://www.qsha-oh.com/maker/mvs/',
# 'https://www.qsha-oh.com/maker/bugatti/',
# 'https://www.qsha-oh.com/maker/matra/',
# 'https://www.qsha-oh.com/maker/alpine/',
# 'https://www.qsha-oh.com/maker/volvo/',
# 'https://www.qsha-oh.com/maker/saab/',
# 'https://www.qsha-oh.com/maker/birkin/',
# 'https://www.qsha-oh.com/maker/lada/',
# 'https://www.qsha-oh.com/maker/campingcar/',
# 'https://www.qsha-oh.com/maker/welfare-vehicle/',
# 'https://www.qsha-oh.com/maker/uaz/',
# 'https://www.qsha-oh.com/maker/tuning-car/',
# 'https://www.qsha-oh.com/maker/donkervoort/'
]

try:
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # ヘッダー行を書き込む
        csv_writer.writerow(header_row)

        for url in urls:
            # URLの統計情報を取得
            search_url_data, original_url = get_search_url_data(site_url, url)

            # ランダムな遅延処理を追加
            delay = random.uniform(1.0, 2.0)
            print(f'遅延処理 {delay} 秒')
            time.sleep(delay)

            total_impressions = 0
            total_clicks = 0
            total_ctr = 0
            total_position = 0

            count = 0  # データの数を数える

            for row in search_url_data:
                impressions = row.get('impressions', 0)
                clicks = row.get('clicks', 0)
                ctr = row.get('ctr', 0)
                position = row.get('position', 0)

                total_impressions += impressions
                total_clicks += clicks
                total_ctr += ctr
                total_position += position

                count += 1

            if count > 0:
                avg_ctr = total_ctr / count
                avg_position = total_position / count
            else:
                avg_ctr = 0
                avg_position = 0

            # CSVファイルに書き込む
            csv_writer.writerow([original_url, total_impressions, total_clicks, avg_ctr, avg_position])

            print(f'URL: {original_url}, 合計表示回数: {total_impressions}, 合計クリック数: {total_clicks}, 平均CTR: {avg_ctr}, 平均掲載順位: {avg_position}')

    print(f'CSVファイルを以下のディレクトリにエクスポートしました: {output_file}')

except Exception as err:
    print(f'An error occurred: {err}')
