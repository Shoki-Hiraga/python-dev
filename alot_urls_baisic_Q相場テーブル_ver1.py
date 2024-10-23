from setting_file.header import *

# ファイルパス
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定
file_name = "Qscraped_data.csv"
output_file = os.path.join(file_directory, file_name)

# # スプレッドシート認証
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# credentials = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/STAFF1088/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/python-scrape.json", scope)
# gc = gspread.authorize(credentials)
# ヘッダー行の設定。ここではウェブページからスクレイプする項目名を列挙しています


header_row = ['URL', 'メーカー', '車種タイトル', '車輌本体価格(basePrice__content)', '走行距離', '年式(specList__jpYear)', '修復歴']

urls = [
'https://www.qsha-oh.com/maker/excalibur',
'https://www.qsha-oh.com/maker/mitsuoka',
'https://www.qsha-oh.com/maker/honda/civic',
'https://www.qsha-oh.com/maker/campingcar/atlas',
'https://www.qsha-oh.com/maker/honda/city_cabriolet',
'https://www.qsha-oh.com/maker/mitsubishi/pajero',
'https://www.qsha-oh.com/maker/ford/ford_gt',
'https://www.qsha-oh.com/maker/ferrari/type360_modena',
'https://www.qsha-oh.com/maker/vandenplas',
'https://www.qsha-oh.com/maker/lexus/lfa',
'https://www.qsha-oh.com/maker/ginetta/g12',
'https://www.qsha-oh.com/maker/toyota/dyna',
'https://www.qsha-oh.com/maker/toyota/zzt231_celica',
'https://www.qsha-oh.com/maker/datsun/truck/',
'https://www.qsha-oh.com/maker/nissan/r35_gt-r',
'https://www.qsha-oh.com/maker/nissan/langley',
'https://www.qsha-oh.com/maker/ferrari/458-italia',
'https://www.qsha-oh.com/maker/lincoln/mark4',
'https://www.qsha-oh.com/maker/de-tomaso/mangusta',
'https://www.qsha-oh.com/maker/subaru/impreza_xv',
'https://www.qsha-oh.com/maker',
'https://www.qsha-oh.com/maker/toyota/mark2-jzx100',
'https://www.qsha-oh.com/maker/benz/r231',
'https://www.qsha-oh.com/maker/alpina/b10biturbo',
'https://www.qsha-oh.com/maker/eunos',
'https://www.qsha-oh.com/maker/campingcar/fiat-ducato',
'https://www.qsha-oh.com/maker/isuzu/117coupe',
'https://www.qsha-oh.com/maker/toyota/crown_stationwagon',
'https://www.qsha-oh.com/maker/honda/integra-type-r',
'https://www.qsha-oh.com/maker/isuzu/bighorn',
'https://www.qsha-oh.com/maker/nissan/silvia-csp311',
'https://www.qsha-oh.com/maker/toyota/altezza',
'https://www.qsha-oh.com/maker/honda/inspire',
'https://www.qsha-oh.com/maker/chevrolet/camaro_convertible',
'https://www.qsha-oh.com/maker/ferrari/type348',
'https://www.qsha-oh.com/maker/toyota/land_cruiser_prado_90',
'https://www.qsha-oh.com/maker/toyota/corona',
'https://www.qsha-oh.com/maker/mitsubishi/mirage',
'https://www.qsha-oh.com/maker/honda/element',
'https://www.qsha-oh.com/maker/matra/jet',
'https://www.qsha-oh.com/maker/honda/prelude',
'https://www.qsha-oh.com/maker/audi/90-2',
'https://www.qsha-oh.com/maker/rolls-royce',
'https://www.qsha-oh.com/maker/nissan/gloria',
'https://www.qsha-oh.com/maker/volvo/940',
'https://www.qsha-oh.com/maker/plymouth/duster',
'https://www.qsha-oh.com/maker/lotus/elise',
'https://www.qsha-oh.com/maker/rolls-royce/silver-wraith',
'https://www.qsha-oh.com/maker/mitsubishi/legnum',
'https://www.qsha-oh.com/maker/toyota/ae86',
'https://www.qsha-oh.com/maker/honda/civic-type-r-fk8',
'https://www.qsha-oh.com/maker/toyota/hilux-surf-215',
'https://www.qsha-oh.com/maker/subaru/impreza_wrx-sti_gc8',
'https://www.qsha-oh.com/maker/nissan/silvia_s13',
'https://www.qsha-oh.com/maker/mitsubishi/lancer_evolution_6',
'https://www.qsha-oh.com/maker/toyota/v8crown-uzs131',
'https://www.qsha-oh.com/maker/ac-cars',
'https://www.qsha-oh.com/maker/jeep/wrangler-unlimited',
'https://www.qsha-oh.com/maker/ferrari/california-t',
'https://www.qsha-oh.com/maker/honda/n3_360',
'https://www.qsha-oh.com/maker/renault/alpine-a110/',
'https://www.qsha-oh.com/maker/italdesign',
'https://www.qsha-oh.com/maker/lexus/sc430',
'https://www.qsha-oh.com/maker/mazda/nd_roadster',
'https://www.qsha-oh.com/maker/bmw/i8',
'https://www.qsha-oh.com/maker/nissan/sunny-truck',
'https://www.qsha-oh.com/maker/volvo/140-2',
'https://www.qsha-oh.com/maker/lancia/montecarlo',
'https://www.qsha-oh.com/maker/lamborghini/murcielago',
'https://www.qsha-oh.com/maker/mitsubishi/galant-coupe-fto',
'https://www.qsha-oh.com/maker/rover/mini_cooper',
'https://www.qsha-oh.com/maker/jaguar-cars',
'https://www.qsha-oh.com/maker/maserati/shamal',
'https://www.qsha-oh.com/maker/toyota/landcruiser-70',
'https://www.qsha-oh.com/maker/subaru/impreza_sportwagon_wrx-sti-version-5-6',
'https://www.qsha-oh.com/maker/hino/ranger',
'https://www.qsha-oh.com/maker/astonmartin/db1',
'https://www.qsha-oh.com/maker/subaru/legacy-touringwagon',
'https://www.qsha-oh.com/maker/isuzu/gemini-pf50-pf60-pfd60',
'https://www.qsha-oh.com/maker/nissan/cedric330',
'https://www.qsha-oh.com/maker/dodge',
'https://www.qsha-oh.com/maker/volkswagen/golf-2',
'https://www.qsha-oh.com/maker/honda/s600',
'https://www.qsha-oh.com/maker/alpina/b3s-33cabrio',
'https://www.qsha-oh.com/maker/mitsubishi/pajeroevolution',
'https://www.qsha-oh.com/maker/datsun/280z',
'https://www.qsha-oh.com/maker/us-toyota/t100',
'https://www.qsha-oh.com/maker/ferrari/512bb-512bblm',
'https://www.qsha-oh.com/maker/dodge/ram',
'https://www.qsha-oh.com/maker/volkswagen',
'https://www.qsha-oh.com/maker/volkswagen/corrado',
'https://www.qsha-oh.com/maker/toyota/mr2',
'https://www.qsha-oh.com/maker/citroen/2cv',
'https://www.qsha-oh.com/maker/renault/alpine-a110',
'https://www.qsha-oh.com/maker/toyota/landcruiser-55',
'https://www.qsha-oh.com/maker/mazda/cosmo-2',
'https://www.qsha-oh.com/maker/mitsubishi/delica-star-wagon',
'https://www.qsha-oh.com/maker/alpina/e30',
'https://www.qsha-oh.com/maker/jeep/cherokee',
'https://www.qsha-oh.com/maker/ford/thunderbird',
'https://www.qsha-oh.com/maker/toyota/daruma-selica',
'https://www.qsha-oh.com/maker/suzuki/escudo',
'https://www.qsha-oh.com/maker/ferrari/type328',
'https://www.qsha-oh.com/maker/toyota',
'https://www.qsha-oh.com/maker/us-lexus/lx470',
'https://www.qsha-oh.com/maker/ferrari/f8-tributo',
'https://www.qsha-oh.com/maker/gemballa/avalanche',
'https://www.qsha-oh.com/maker/isuzu/mu-wizard',
'https://www.qsha-oh.com/maker/nissan/laurel',
'https://www.qsha-oh.com/maker/tommy-kaira/zz',
'https://www.qsha-oh.com/maker/mitsubishi/lancer-evolution',
'https://www.qsha-oh.com/maker/campingcar/vantech-atom',
'https://www.qsha-oh.com/maker/nissan/gazelle',
'https://www.qsha-oh.com/maker/alfaromeo/2000gtv',
'https://www.qsha-oh.com/maker/alpina/c1',
'https://www.qsha-oh.com/maker/nissan/maxima',
'https://www.qsha-oh.com/maker/morris',
'https://www.qsha-oh.com/maker/eunos/eunos-roadster',
'https://www.qsha-oh.com/maker/nissan/y30-gloria-brougham-turbo',
'https://www.qsha-oh.com/maker/daihatsu/charmant',
'https://www.qsha-oh.com/maker/bugatti/eb110',
'https://www.qsha-oh.com/maker/nissan/hakosuka',
'https://www.qsha-oh.com/maker/cadillac/deville',
'https://www.qsha-oh.com/maker/dome/zero',
'https://www.qsha-oh.com/maker/mitsubishi/colt_ralliart_version-r',
'https://www.qsha-oh.com/maker/nissan/silvia',
'https://www.qsha-oh.com/maker/tesla',
'https://www.qsha-oh.com/maker/alfaromeo/1600gtjunior',
'https://www.qsha-oh.com/maker/tvr/chimaera',
'https://www.qsha-oh.com/maker/mitsubishi/lancer_evolution_finaledition',
'https://www.qsha-oh.com/maker/nissan/nv200-vanette',
'https://www.qsha-oh.com/maker/subaru/wrx-s4',
'https://www.qsha-oh.com/maker/alpina/b5_touring',
'https://www.qsha-oh.com/maker/tvr/grantura',
'https://www.qsha-oh.com/maker/ruf/rct-evo',
'https://www.qsha-oh.com/maker/renault/4_quatre',
'https://www.qsha-oh.com/maker/toyota/chaser-jzx90',
'https://www.qsha-oh.com/maker/us-nissan/titan',
'https://www.qsha-oh.com/maker/mazda',
'https://www.qsha-oh.com/maker/acura',
'https://www.qsha-oh.com/maker/audi',
'https://www.qsha-oh.com/maker/maserati/indy',
'https://www.qsha-oh.com/maker/mitsuoka/zero1',
'https://www.qsha-oh.com/maker/oldsmobile',
'https://www.qsha-oh.com/maker/nissan/skyline_coupe',
'https://www.qsha-oh.com/maker/alfaromeo/105-system',
'https://www.qsha-oh.com/maker/mitsubishi/delica-d5',
'https://www.qsha-oh.com/maker/toyota/windom',
'https://www.qsha-oh.com/maker/nissan/r33-skyline-gtr-autech-version',
'https://www.qsha-oh.com/maker/toyota/grand-hiace',
'https://www.qsha-oh.com/maker/land-rover/discovery',
'https://www.qsha-oh.com/maker/honda/torneo',
'https://www.qsha-oh.com/maker/toyota/kp61',
'https://www.qsha-oh.com/maker/toyota/vitz_rs',
'https://www.qsha-oh.com/maker/peugeot',
'https://www.qsha-oh.com/maker/amg/c36',
'https://www.qsha-oh.com/maker/peugeot/type205',
'https://www.qsha-oh.com/maker/mazda/sentia',
'https://www.qsha-oh.com/maker/toyota/vellfire',
'https://www.qsha-oh.com/maker/mvs',
'https://www.qsha-oh.com/maker/mazda/eunos-roadster',
'https://www.qsha-oh.com/maker/mazda/eunos-roadster/',
'https://www.qsha-oh.com/maker/ferrari/365gt2-2',
'https://www.qsha-oh.com/maker/astonmartin/db2',
'https://www.qsha-oh.com/maker/lamborghini/aventador',
'https://www.qsha-oh.com/maker/subaru/forester-sg9-sti-version',
'https://www.qsha-oh.com/maker/ferrari/fxx',
'https://www.qsha-oh.com/maker/benz',
'https://www.qsha-oh.com/maker/benz/r230',
'https://www.qsha-oh.com/maker/fiat/coupefiat',
'https://www.qsha-oh.com/maker/fiat/coupe-fiat',
'https://www.qsha-oh.com/maker/mazda/roadpacer',
'https://www.qsha-oh.com/maker/renault/alpine',
'https://www.qsha-oh.com/maker/mitsubishi/minicab-miev',
'https://www.qsha-oh.com/maker/lamborghini/diablo',
'https://www.qsha-oh.com/maker/ford/escoat',
'https://www.qsha-oh.com/maker/lamborghini/gallardo',
'https://www.qsha-oh.com/maker/mitsubishi/starion',
'https://www.qsha-oh.com/maker/benz/g320',
'https://www.qsha-oh.com/maker/citroen/mehari',
'https://www.qsha-oh.com/maker/ruf/btr',
'https://www.qsha-oh.com/maker/subaru/impreza_wrx-sti_gdb',
'https://www.qsha-oh.com/maker/porsche/air-cooling',
'https://www.qsha-oh.com/maker/isuzu/piazza_nero',
'https://www.qsha-oh.com/maker/daihatsu/mira',
'https://www.qsha-oh.com/maker/us-toyota/sequoia',
'https://www.qsha-oh.com/maker/toyota/sera',
'https://www.qsha-oh.com/maker/mitsubishi/lancer_evolution_10',
'https://www.qsha-oh.com/maker/campingcar/van-conversion-b',
'https://www.qsha-oh.com/maker/ferrari/456-m-gt',
'https://www.qsha-oh.com/maker/renault/alpine_v6turbo/',
'https://www.qsha-oh.com/maker/shelby-american',
'https://www.qsha-oh.com/maker/austin/mini-van',
'https://www.qsha-oh.com/maker/toyota/70-supra',
'https://www.qsha-oh.com/maker/nissan/skyline-25gt-turbo',
'https://www.qsha-oh.com/maker/ford',
'https://www.qsha-oh.com/maker/honda/s500',
'https://www.qsha-oh.com/maker/datsun/truck',
'https://www.qsha-oh.com/maker/jeep/cherokee-xj-7mx',
'https://www.qsha-oh.com/maker/maserati',
'https://www.qsha-oh.com/maker/astonmartin/db6',
'https://www.qsha-oh.com/maker/porsche/911-narrow',
'https://www.qsha-oh.com/maker/austin',
'https://www.qsha-oh.com/maker/benz/w126',
'https://www.qsha-oh.com/maker/toyota/mark2_tourer-v',
'https://www.qsha-oh.com/maker/jaguar-cars/mk2',
'https://www.qsha-oh.com/maker/mitsubishi/lancer_wagon_evolution',
'https://www.qsha-oh.com/maker/bentley/continental-gt',
'https://www.qsha-oh.com/maker/chevrolet/fleetline',
'https://www.qsha-oh.com/maker/porsche/type964',
'https://www.qsha-oh.com/maker/alpina/b3_touring',
'https://www.qsha-oh.com/maker/mitsuoka/rock-star',
'https://www.qsha-oh.com/maker/lada/niva',
'https://www.qsha-oh.com/maker/daihatsu/compagno',
'https://www.qsha-oh.com/maker/rover/mini-cooper-40th-anniversary-ltd',
'https://www.qsha-oh.com/maker/amg/c55',
'https://www.qsha-oh.com/maker/mitsubishi/galant',
'https://www.qsha-oh.com/maker/ferrari/f430',
'https://www.qsha-oh.com/maker/volkswagen/new-beetle',
'https://www.qsha-oh.com/maker/volvo/volvo-trucks-fh',
'https://www.qsha-oh.com/maker/ferrari/458-speciale',
'https://www.qsha-oh.com/maker/toyota/crown_athletev',
'https://www.qsha-oh.com/maker/chevrolet/corvette-c8',
'https://www.qsha-oh.com/maker/ferrari/type360_spider',
'https://www.qsha-oh.com/maker/mazda/rx-7fd',
'https://www.qsha-oh.com/maker/chevrolet/biscayne',
'https://www.qsha-oh.com/maker/ferrari',
'https://www.qsha-oh.com/maker/bmw',
'https://www.qsha-oh.com/maker/audi/100-c1-c2-c3',
'https://www.qsha-oh.com/maker/volkswagen/sp2',
'https://www.qsha-oh.com/maker/nissan/fairladyz-z31',
'https://www.qsha-oh.com/maker/nissan/r32-skyline-gtr',
'https://www.qsha-oh.com/maker/nissan/silvia_s15',
'https://www.qsha-oh.com/maker/plymouth/belvedere',
'https://www.qsha-oh.com/maker/jeep/tj-wrangler',
'https://www.qsha-oh.com/maker/dodge/ram_van',
'https://www.qsha-oh.com/maker/toyota/2000gt',
'https://www.qsha-oh.com/maker/fiat/croma',
'https://www.qsha-oh.com/maker/porsche',
'https://www.qsha-oh.com/maker/benz/sl-class',
'https://www.qsha-oh.com/maker/mitsubishi/galant_vr-4',
'https://www.qsha-oh.com/maker/astonmartin/lagonda',
'https://www.qsha-oh.com/maker/lamborghini/espada',
'https://www.qsha-oh.com/maker/mitsuoka/viewt'
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
        ('#app > div.model > section.c-marketprice > div.c-marketprice__inner', 'text')

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

# CSVファイルを開き、ヘッダーとスクレイプしたデータを書き込む
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
