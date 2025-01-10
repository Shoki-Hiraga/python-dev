import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting_file.header import *

# ファイルパス
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定  # file_path.pyで定義したファイルディレクトリを指定

# 個別URLリストインスタンス
urls = [
"https://www.qsha-oh.com/maker/nissan/skyline/",
"https://ucarpac.com/sell/m002/n027",
"https://autoc-one.jp/ullo/biddedCarList/ma35/mo1639/",
"https://s.kakaku.com/item/70100310105/kaitori/",
"https://www.goo-net.com/kaitori/maker_guide/show/1015/10151010/",
"https://kaitori.carsensor.net/NI/S030/",
"https://221616.com/satei/souba/nissan/skyline/",
"https://autoc-one.jp/catalog/nissan/skyline/kaitori/",
"https://kaitori.carview.co.jp/souba/nissan/skyline/",
"https://www.navikuru.jp/souba/nissan/skyline-sedan/",
"https://www.nextage.jp/kaitori/souba/nissan/skyline/",
"https://www.kurumaerabi.com/kaitori/marketprice/cartype/2/208/",
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
            # エラーが発生した場合、ログを記録
            logging.error(f"Error occurred while accessing {url}: {str(e)}")
            return None

    if response.status_code != 200:
        logging.error(f"Failed to retrieve URL: {url}")
        return None

    response.encoding = response.apparent_encoding
    return response.text

# URLからファイル名を生成する関数
def generate_filename(url):
    filename = url.replace('https://', '').replace('http://', '').replace('/', '-')
    return f"{filename}.html"

# スクレイピングの進捗をログに記録する関数
def log_progress(completed_count, total_count):
    percentage_complete = (completed_count / total_count) * 100
    print(f'{round(percentage_complete, 2)} % 完了.... {completed_count} / {total_count}')

# 完了したURLの数
completed_count = 0

# URLリストに対してスクレイピングを実行し、HTMLを保存
for url in urls:
    html_content = scrape_url(url)
    if html_content:
        filename = generate_filename(url)  # ファイル名を生成
        file_path.file_directory = os.path.join(file_directory, filename)

        # HTMLコンテンツをファイルに保存
        with open(file_path.file_directory, mode='w', encoding='utf-8') as file:
            file.write(html_content)
        
        print(f"Saved HTML content for {url} as {filename}")

    completed_count += 1
    log_progress(completed_count, len(urls))  # 進捗のログ

print('スクレイピングが完了しました。')  # 全てのスクレイピングが完了したことを通知
