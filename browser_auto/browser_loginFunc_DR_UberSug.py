from setting_file.header import *
from setting_file.browser_login.login_id_password import id, password
from setting_file.scraping_url.browser_scraping_login_Url import URLS

# ヘッドレスモードの指定
headlessmode = False

# ファイル保存ディレクトリを指定
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定
file_name = "domain_rank_uber.csv"
output_file = os.path.join(file_directory, file_name)


# パラメータ設定
login_url = "https://app.neilpatel.com/ja/login"  # ログインURL
user_id_selector = "#root > div.sc-cDJyZ.kYIeNi > div > div > div > div > form > div:nth-child(1) > input"          # ユーザーID入力フィールドのCSSセレクタ
password_selector = "#root > div.sc-cDJyZ.kYIeNi > div > div > div > div > form > div:nth-child(2) > input"         # パスワード入力フィールドのCSSセレクタ
user_id = id                   # ユーザーID
password = password              # パスワード

time.sleep(3)

# ログイン後の操作URL
post_login_url = "https://app.neilpatel.com/ja/seo_analyzer/backlinks/" 
input_selector = "#root > div.sc-cDJyZ.kYIeNi > div.sc-eODrEC.jqOJAq > div.sc-gvvZcT.iDDjNW > div > div > div.sc-ctluuY.kXMBUa > form > div.sc-hqUaMi.bmEEnm > input"                  # inputフィールドのCSSセレクタ
input_data_list = URLS

# ボタンのCSSセレクタ
button_selector = "#root > div.sc-cDJyZ.kYIeNi > div.sc-eODrEC.jqOJAq > div.sc-gvvZcT.iDDjNW > div > div > div.sc-ctluuY.kXMBUa > form > button"

# 取得したいデータのCSSセレクタ
data_selectors = [
    "div.sc-iBUNwL:nth-of-type(1) div:nth-of-type(2)",
    "div.sc-iBUNwL:nth-of-type(2) div:nth-of-type(2)",
    "div.sc-iBUNwL:nth-of-type(3) div:nth-of-type(2)"
]



def scrape_with_playwright(login_url, user_id_selector, password_selector, user_id, password,
                           post_login_url, input_selector, input_data_list, button_selector,
                           data_selectors, output_file):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headlessmode)  # ヘッドレスで実行
        context = browser.new_context()
        page = context.new_page()

        try:
            # ログイン処理
            print("ログイン処理を開始...")
            page.goto(login_url)
            page.fill(user_id_selector, user_id)
            page.fill(password_selector, password)
            time.sleep(2)
            page.press(password_selector, "Enter")  # Enterキーを押す
            time.sleep(1)
            print("ログイン完了")

            # 操作処理
            print("操作処理を実行します...")
            page.goto(post_login_url)
            time.sleep(3)
            results = []

            for data in input_data_list:
                time.sleep(3)
                # 入力
                print(f"データを入力: {data}")
                page.fill(input_selector, data)
                # ボタンをクリック
                page.click(button_selector)
                print("ボタンをクリック、処理を待機中...")
                time.sleep(5)

                # データ取得
                row = [data]  # 入力データを含む
                for selector in data_selectors:
                    try:
                        element = page.query_selector(selector)
                        text = element.inner_text() if element else "N/A"
                        row.append(text)
                        print(f"データ取得成功: {text}")
                    except Exception as e:
                        row.append(f"Error: {str(e)}")
                        print(f"データ取得エラー: {e}")
                results.append(row)

            # CSVにデータを保存
            print("CSVファイルにデータを保存します...")
            with open(output_file, mode='w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                header = ["Input Data"] + [f"Data Selector {i+1}" for i in range(len(data_selectors))]
                writer.writerow(header)
                writer.writerows(results)

            print(f"処理が完了しました。データは {output_file} に保存されています。")

        except Exception as e:
            print(f"エラーが発生しました: {e}")

        finally:
            # ブラウザを閉じる
            # browser.close()
            print("処理完了")

        # CSVにデータを保存
        print("CSVファイルにデータを保存します...")
        with open(output_file, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            # ヘッダー作成
            header = ["Input Data"] + [f"Data Selector {i+1}" for i in range(len(data_selectors))]
            writer.writerow(header)
            # データを書き込み
            writer.writerows(results)

        print(f"処理が完了しました。データは {output_file} に保存されています。")


# 実行
scrape_with_playwright(login_url, 
                       user_id_selector, 
                       password_selector, 
                       user_id, 
                       password,
                       post_login_url, 
                       input_selector, 
                       input_data_list, 
                       button_selector,
                       data_selectors, 
                       output_file
                       )
