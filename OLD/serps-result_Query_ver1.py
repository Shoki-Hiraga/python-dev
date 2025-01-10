import requests
from bs4 import BeautifulSoup
import csv
import os
import random
import time
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
from setting_file.user_agent import user_agents  
from setting_file import csv_output_path  
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ファイルパスの設定
csv_directory = csv_output_path.out_office
csv_filename = "Google-serps-result_Query.csv"
output_file = os.path.join(csv_directory, csv_filename)

keywords_set = ["allintitle: 外車王","allintitle: 旧車王"]
domain_set = "www.google.com"


def google_search(query, domain_filter=None, delay_time=5):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
    attempt = 0
    rank_count = 0
    while attempt < 3:
        try:
            print(f"リクエスト: {query}")  # リクエスト送信のデバッグ出力
            response = requests.get(f"https://www.google.com/search?q={query}", headers=headers)
            response.raise_for_status()  # ステータスチェック
            print(f"レスポンス: {query}")  # レスポンス受信のデバッグ出力
            soup = BeautifulSoup(response.text, 'html.parser')
            results = []
            for index, result in enumerate(soup.find_all('div', class_='tF2Cxc'), start=1):
                rank_count += 1
                print(f"{rank_count}")
                link = result.find('a')['href']
                title = result.find('h3').text
                if domain_filter is None or domain_filter in link:
                    results.append((link, title, index))
                    print(f"KW: [{query}] Rank: {index}, URL: {link}, Title: {title}")
                time.sleep(delay_time)
            return results
        except (HTTPError, ConnectionError, Timeout, RequestException) as e:
            print(f"Request error: {e}, retrying...")
            time.sleep(10)
            attempt += 1
    return []

def write_to_csv(results, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['URL', 'Title', 'Rank'])
        writer.writerows(results)

def main():
    keywords = keywords_set
    domain = domain_set
    all_results = []
    for keyword in keywords:
        results = google_search(keyword, domain, delay_time=2)
        all_results.extend(results)
    write_to_csv(all_results, output_file)
    print("===============処理完了===============")

if __name__ == '__main__':
    main()
