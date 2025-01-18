from setting_file.header import *

# CSVを初期化する関数
class csv_init:
    def __init__(self, output_file, headers, csv_delimiter):
        self.output_file = output_file
        self.headers = headers
        self.csv_delimiter = csv_delimiter

    def initialize_csv(self):
        try:
            with open(self.output_file, mode='w', encoding='utf-8-sig', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.headers, delimiter=self.csv_delimiter)
                writer.writeheader()
            print(f"{self.output_file} を初期化しました。")
        except Exception as e:
            print(f"CSV初期化エラー: {e}")


class GoogleAdsScraper:
    def __init__(self, keyword, output_file, csv_delimiter, html_elements, delay_seconds):
        self.keyword = keyword
        self.output_file = output_file
        self.csv_delimiter = csv_delimiter
        self.html_elements = html_elements
        self.delay_seconds = delay_seconds
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

        ad_elements = soup.find_all('div', {'class': self.html_elements['ad_container']})

        for ad in ad_elements:
            try:
                title = ad.find('div', {'class': self.html_elements['ad_title']}).text if ad.find('div', {'class': self.html_elements['ad_title']}) else ''
                url = ad.find(self.html_elements['ad_url'])['href'] if ad.find(self.html_elements['ad_url']) else ''

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
            df.to_csv(self.output_file, mode='a', index=False, encoding='utf-8-sig', header=False, sep=self.csv_delimiter)
            print(f"データを {self.output_file} に保存しました。")
        except Exception as e:
            print(f"CSVファイル保存エラー: {e}")

    def run(self):
        print(f"キーワード '{self.keyword}' の広告を検索中...")
        time.sleep(self.delay_seconds)

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
