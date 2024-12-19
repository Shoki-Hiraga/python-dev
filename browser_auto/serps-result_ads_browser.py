import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting_file.header import *

# Seleniumの設定
service = Service("C:/chromedriver.exe")  # ChromeDriverのパスを指定
driver = webdriver.Chrome(service=service)

# グローバル変数でページ範囲を指定
PAGE_START = 1  # 開始ページ
PAGE_END = 1   # 終了ページ
base_url = "https://www.google.com"

user_agent = random.choice(user_agents)
search_query = "車 買取"
# headers = {'User-Agent': user_agent}
headers = {
    'User-Agent': user_agent,
    'Accept-Language': 'ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7',
    'Referer': 'https://www.google.com/'
}


# スクレイピング遅延処理
delay_time_set = random.uniform(000.1, 000.2)

# ファイルパス
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定
file_name = "ad_search_results.csv"
output_file = os.path.join(file_directory, file_name)

csv_headers = [
    "URL",
    "Title"
    ]

# CSSセレクタの配列
url_selectors = ["#taw a.sVXRqc", "a.V0MxL"]
title_selectors = ["#taw .CCgQ5 span", "h3.zBAuLc"]

def scrape_google_ads_with_selenium():
    driver.get(f"https://www.google.com/search?q={search_query}&adtest=on")
    time.sleep(5)  # ページが完全に読み込まれるまで待機

    soup = BeautifulSoup(driver.page_source, "html.parser")

    ad_blocks = soup.select("#taw div.vdQmEd")
    with open(output_file, "w", encoding="utf-8", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(csv_headers)

        for ad_block in ad_blocks:
            url = None
            title = None

            # URLを取得
            for selector in url_selectors:
                url_tag = ad_block.select_one(selector)
                if url_tag:
                    url = url_tag.get('href')
                    break

            # タイトルを取得
            for selector in title_selectors:
                title_tag = ad_block.select_one(selector)
                if title_tag:
                    title = title_tag.text
                    break

            if url and title:
                csv_writer.writerow([url, title])
                print(f"取得データ: {url} - {title}")
            else:
                print("No valid ad block found.")

    driver.quit()

scrape_google_ads_with_selenium()
