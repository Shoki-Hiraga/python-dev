from setting_file.header import *
import concurrent.futures

class CsvWriter:
    def __init__(self, output_file, header_row, delimiter='★'):
        """
        コンストラクタでCSVファイルのパス、ヘッダー、区切り文字を指定
        """
        self.output_file = output_file
        self.header_row = header_row
        self.delimiter = delimiter

    def write_to_csv(self, urls, scraping_func, css_selectors, delay_time, log_progress):
        """
        CSVファイルにデータを書き込む処理
        """
        completed_count = 0

        with open(self.output_file, mode='w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=self.delimiter)
            # ヘッダー行を書き込む
            csv_writer.writerow(self.header_row)

            with concurrent.futures.ThreadPoolExecutor() as executor:
                for url in urls:
                    # スクレイピングを実行
                    result = scraping_func.scrape_url(url, css_selectors, delay_time)
                    url, scraped_data, status_code = result
                    max_length = max(len(data) for data in scraped_data)  # 最大の列数を取得

                    # データをCSVに書き込む
                    for i in range(max_length):
                        row_data = [url] + [data[i] if i < len(data) else '' for data in scraped_data] + [status_code]
                        csv_writer.writerow(row_data)

                    # 進捗をログ出力
                    completed_count += 1
                    log_progress(completed_count, len(urls))
                    
                    # 各URLごとの進捗ログ
                    print(f"{self.header_row[0]}: {url}")
                    print("--------------------------------------------")

        print("スクレイピングが完了しました。")
