from setting_file.header import *

# グローバル変数でページ範囲を指定
PAGE_START = 1  # 開始ページ
PAGE_END = 1   # 終了ページ
base_url = "https://www.google.com"
user_agent = random.choice(user_agents)
search_query = "車 買取"
headers = {'User-Agent': user_agent}

# スクレイピング遅延処理
delay_time_set = random.uniform(000.1, 000.2)

# ファイルパス
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定 # file_path.py で定義したファイルディレクトリを指定
file_name = "ad_search_results.csv"
output_file = os.path.join(file_directory, file_name)

csv_headers = [
    "URL",
    "Title"
    ]

# CSSセレクタの配列
url_selectors = ["#taw a.sVXRqc", "a.V0MxL"]
title_selectors = ["#taw .CCgQ5 span", "h3.zBAuLc"]


def scrape_google_ads():
    with open(output_file, "w", encoding="utf-8", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(csv_headers)

        for page in range(PAGE_START, PAGE_END + 1):
            search_url = f"{base_url}/search?q={search_query}&adtest=on&start={(page - 1) * 10}"
            delay = delay_time_set
            time.sleep(delay)
            response = requests.get(search_url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")

            # ステータスコードを表示
            print(f"検索URL: {search_url}")
            print(f"Status Code: {response.status_code}")
            print(f"----------遅延処理 {delay}----------")

            # 広告の親要素を抽出
            ad_blocks = soup.select("#taw div.vdQmEd")

            for ad_block in ad_blocks:
                url = None
                title = None

                # URLを取得
                for selector in url_selectors:
                    url_tag = ad_block.select_one(selector)
                    if url_tag:
                        url = url_tag.get('href')
                        break  # 最初に一致したセレクタを使用

                # タイトルを取得
                for selector in title_selectors:
                    title_tag = ad_block.select_one(selector)
                    if title_tag:
                        title = title_tag.text
                        break  # 最初に一致したセレクタを使用

                if url and title:
                    csv_writer.writerow([url, title])
                    print(f"取得データ: {url} - {title}")
                else:
                    print("No valid ad block found.")

scrape_google_ads()
