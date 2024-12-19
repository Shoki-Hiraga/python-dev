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
                futures = []
                for url in urls:
                    # スクレイピングタスクを非同期で実行
                    futures.append(
                        executor.submit(scraping_func.scrape_url, url, css_selectors, delay_time)
                    )

                for future in concurrent.futures.as_completed(futures):
                    try:
                        result = future.result()  # スクレイピング結果を取得
                        url, scraped_data, status_code = result

                        # ステータスコードをチェック
                        if status_code != 200:
                            logging.error(f"Failed to retrieve URL: {url} (Status code: {status_code})")
                            # 各列にエラーコードを記録
                            row_data = [url] + [str(status_code) for _ in self.header_row[1:]]
                            csv_writer.writerow(row_data)
                            continue

                        # データが空の場合の処理
                        if not scraped_data:
                            logging.warning(f"No data scraped from URL: {url}")
                            # 各列に空のデータとステータスコードを記録
                            row_data = [url] + ['' for _ in self.header_row[1:]]
                            csv_writer.writerow(row_data)
                            continue

                        # 最大列数を取得（エラー回避のため安全に実行）
                        max_length = max((len(data) for data in scraped_data), default=0)

                        # データをCSVに書き込む
                        for i in range(max_length):
                            row_data = [url] + [data[i] if i < len(data) else '' for data in scraped_data]
                            csv_writer.writerow(row_data)

                    except Exception as e:
                        logging.error(f"Error processing URL: {future}, {e}", exc_info=True)
                        # 例外発生時も各列にエラーコードを記録
                        row_data = [url] + [str(e)] * len(self.header_row[1:])
                        csv_writer.writerow(row_data)

                    # 進捗をログ出力
                    completed_count += 1
                    log_progress(completed_count, len(urls))

                    # 各URLごとの進捗ログ
                    print(f"{self.header_row[0]}: {url}")
                    print("--------------------------------------------")

        print("スクレイピングが完了しました。")
