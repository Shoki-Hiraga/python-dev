import os
import csv
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from setting_file.header import *

# CSV区切り文字を指定
csv_delimiter = '★'

# ファイルパス
file_directory = file_path.file_directory  # file_path.py で定義したファイルディレクトリを指定
file_name = "ad_search_results.csv"
output_file = os.path.join(file_directory, file_name)

# グローバル変数としてHTML要素を指定
html_elements = {
    'ad_container': 'uEierd',
    'ad_title': 'CCgQ5',
    'ad_url': 'a'
}

# CSVヘッダーをグローバル変数として定義
headers = ['keyword', 'title', 'url']

delay_seconds = 5

# 複数キーワードを指定
keywords = [
'旧車王',
'外車王',
'カレント自動車',
'オートプライム',
'ガレージカレント',
'ガレージカレント直販センタ',
'ガレージカレントCamp'
    ]

# CSVを初期化する関数
def initialize_csv():
    try:
        with open(output_file, mode='w', encoding='utf-8-sig', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers, delimiter=csv_delimiter)
            writer.writeheader()
        print(f"{output_file} を初期化しました。")
    except Exception as e:
        print(f"CSV初期化エラー: {e}")

class GoogleAdsScraper:
    def __init__(self, keyword):
        self.keyword = keyword
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.base_url = 'https://www.google.com/search'

    def get_search_results(self):
        params = {
            'q': self.keyword,
            'hl': 'ja',  # 日本語検索結果を取得
            'gl': 'jp'   # 日本のリージョンを指定
        }

        try:
            response = requests.get(self.base_url, params=params, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"エラーが発生しました: {e}")
            return None

    def parse_ads(self, html_content):
        if not html_content:
            return []

        soup = BeautifulSoup(html_content, 'html.parser')
        ads = []

        ad_elements = soup.find_all('div', {'class': html_elements['ad_container']})

        for ad in ad_elements:
            try:
                title = ad.find('div', {'class': html_elements['ad_title']}).text if ad.find('div', {'class': html_elements['ad_title']}) else ''
                url = ad.find(html_elements['ad_url'])['href'] if ad.find(html_elements['ad_url']) else ''

                ads.append({
                    'keyword': self.keyword,
                    'title': title,
                    'url': url,
                })
            except Exception as e:
                print(f"広告の解析中にエラーが発生しました: {e}")
                continue

        return ads

    def save_to_csv(self, ads):
        if not ads:
            print("保存する広告データがありません。")
            return

        try:
            df = pd.DataFrame(ads)
            # ヘッダーを追加し、追記モードで保存
            df.to_csv(output_file, mode='a', index=False, encoding='utf-8-sig', header=False, sep=csv_delimiter)
            print(f"データを {output_file} に保存しました。")
        except Exception as e:
            print(f"CSVファイル保存エラー: {e}")

    def run(self):
        print(f"キーワード '{self.keyword}' の広告を検索中...")
        time.sleep(delay_seconds)

        html_content = self.get_search_results()
        if html_content:
            ads = self.parse_ads(html_content)
            if ads:
                print(f"{len(ads)}件の広告")
                self.save_to_csv(ads)
            else:
                print("広告なし")
        else:
            print("検索結果の取得エラー")

def main():
    initialize_csv()  # プログラム起動時にCSVを初期化
    for keyword in keywords:
        scraper = GoogleAdsScraper(keyword)
        scraper.run()

if __name__ == "__main__":
    main()