from setting_file.header import *


class alot_urls_scraping:
    # ウェブページの情報をスクレイプする関数
    def scrape_url(url, CSS_selectors, delay_time_set):
        # アクセスエラー発生時の最大リトライ回数を設定
        MAX_RETRIES = 10
        delay_time = delay_time_set  # リクエスト間のランダムな遅延時間を設定
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
        selectors = CSS_selectors

        scraped_data = [[] for _ in range(len(selectors))]
        
        # 各セレクターに対してスクレイピングを実行し、結果を保存
        for index, (selector, *data_types) in enumerate(selectors):
            elements = soup.select(selector)
            if elements:
                if 'link' in data_types:
                    # リンクのテキストとURLを抽出
                    scraped_data[index] = [
                        (element.get('href', ''), element.get_text(strip=True)) for element in elements
                    ]
                elif 'content' in data_types:
                    # content 属性を抽出
                    scraped_data[index] = [
                        element.get('content', '') for element in elements
                    ]
                else:
                    # テキストのみを抽出
                    scraped_data[index] = [
                        element.get_text(strip=True).encode('utf-8').decode('utf-8') for element in elements
                    ]
            else:
                # セレクタに該当する要素が無い場合は空文字列を追加
                scraped_data[index] = ['nodata']

        time.sleep(delay_time)  # さらに遅延を挟む
        print(f'{delay_time}秒の遅延処理 / status code {response.status_code} {scraped_data}')
        return url, scraped_data, response.status_code
