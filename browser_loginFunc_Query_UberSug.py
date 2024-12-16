from setting_file.header import *
from setting_file.browser_login.login_id_password import id, password
from setting_file.scraping_KW.browser_scraping_login_Query import Query

# ヘッドレスモードの指定
headlessmode = False

# ファイル保存ディレクトリを指定
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定

# パラメータ設定
login_url = "https://app.neilpatel.com/ja/login"  # ログインURL
user_id_selector = "#root > div.sc-cDJyZ.kYIeNi > div > div > div > div > form > div:nth-child(1) > input"          # ユーザーID入力フィールドのCSSセレクタ
password_selector = "#root > div.sc-cDJyZ.kYIeNi > div > div > div > div > form > div:nth-child(2) > input"         # パスワード入力フィールドのCSSセレクタ
# ユーザーID
user_id = id
# パスワード
password = password

# ログイン後の操作URL
post_login_url = "https://app.neilpatel.com/ja/ubersuggest/overview/" 
# inputフィールドのCSSセレクタ
input_selector = "#root > div.sc-cDJyZ.kYIeNi > div.sc-eODrEC.jqOJAq > div.sc-gvvZcT.iDDjNW > div > div > div.sc-hHrewP.fmuwcY > div > form > div.sc-hrGSpw.cfTEvo > input"
input_data_list = Query

# ボタンのCSSセレクタ
# 検索ボタン
button1_selector = "#root > div.sc-cDJyZ.kYIeNi > div.sc-eODrEC.jqOJAq > div.sc-gvvZcT.iDDjNW > div > div > div.sc-hHrewP.fmuwcY > div > form > button"
# 全て見るリンク
button2_selector = "#root > div.sc-cDJyZ.kYIeNi > div.sc-eODrEC.jqOJAq > div.sc-gvvZcT.iDDjNW > div > div > div.sc-hMxIkD.eRppkS > div.sc-gVaSRo.hGbtHH > div:nth-child(1) > div > div.sc-fGQXPE.jvHNGa > div.sc-dErQpc.MzgTL > a"
# CSVで出力プルダウン
button3_selector = "#root > div.sc-cDJyZ.kYIeNi > div.sc-eODrEC.jqOJAq > div.sc-gvvZcT.iDDjNW > div > div > div.sc-hMxIkD.eRppkS > div.sc-eSfNbN.dRBNRG > div > div:nth-child(1) > div > div.sc-jwWbkn.gheJca > div > div:nth-child(1) > div > button"
# 全てをエクスポート
button4_selector = "#root > div.sc-cDJyZ.kYIeNi > div.sc-eODrEC.jqOJAq > div.sc-gvvZcT.iDDjNW > div > div > div.sc-hMxIkD.eRppkS > div.sc-eSfNbN.dRBNRG > div > div:nth-child(1) > div > div.sc-jwWbkn.gheJca > div > div:nth-child(1) > div.sc-cAXmzm.iwPgUw > div.sc-kTYlsj.bEUTMu > div"

# def process_element(page, selector, save_path=None):

def process_element(page, selector, save_path=None):
    """
    指定されたCSSセレクタの要素を自動判別し、適切なアクションを実行する。

    Parameters:
    - page: Playwrightのページインスタンス
    - selector: 対象要素のCSSセレクタ
    - save_path: file_directory
    """
    element = page.locator(selector)

    if not element.is_visible():
        print(f"要素が見つかりません: {selector}")
        return

    # 要素の属性を取得
    tag_name = element.evaluate("el => el.tagName.toLowerCase()")  # タグ名
    href = element.get_attribute("href")  # href属性
    download = element.get_attribute("download")  # download属性

    if tag_name == "a" and href:
        # リンクの場合
        if download or href.endswith(('.csv', '.pdf', '.zip', '.xlsx')):  # ファイル拡張子で判定
            with page.expect_download() as download_info:
                element.click()
                print(f"ダウンロードを開始: {href}")
            download_file = download_info.value
            if save_path:
                download_file.save_as(save_path)
                print(f"ダウンロード完了: {save_path}")
            else:
                print(f"ダウンロード完了: {download_file.path()}")
        else:
            # 通常のリンクを開く
            print(f"リンクを開きます: {href}")
            time.sleep(1.5)
            page.goto(href)

    elif tag_name == "button" or element.is_enabled():
        # ボタンの場合
        print("ボタンをクリックします")
        element.click()
        time.sleep(3)  # 必要に応じて待機

    else:
        # その他の要素（クリック可能でない場合）
        print("対応するアクションがありません")

def scrape_with_playwright(login_url, user_id_selector, password_selector, user_id, password,
                           post_login_url, input_selector, input_data_list, button1_selector,
                           button2_selector, button3_selector, button4_selector):
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
            time.sleep(3)
            page.goto(post_login_url)
            time.sleep(3)

            for data in input_data_list:
                time.sleep(3)
                # 入力
                print(f"データを入力: {data}")
                page.fill(input_selector, data)

                # ボタンをクリック
                process_element(page, button1_selector)
                process_element(page, button2_selector)
                process_element(page, button3_selector)
                process_element(page, button4_selector)

            print("処理が完了しました。")

        except Exception as e:
            print(f"エラーが発生しました: {e}")

        finally:
            # ブラウザを閉じる
            delay = 10
            time.sleep(delay)
            print(f"ブラウザ終了中...{delay}秒")
            browser.close()
            print("処理完了")

# 実行
scrape_with_playwright(login_url, 
                       user_id_selector, 
                       password_selector, 
                       user_id, 
                       password,
                       post_login_url, 
                       input_selector, 
                       input_data_list, 
                       button1_selector,
                       button2_selector, 
                       button3_selector,
                       button4_selector
                       )
