import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting_file.header import *

# 画像フォルダのパス
image_folder = "C:/Users/hiraga/Downloads/旧車王画像"
# 結果を保存するCSVファイルのパス

# ファイル保存ディレクトリを指定
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定
file_name = "image_search.csv"
output_file = os.path.join(file_directory, file_name)

# Selenium WebDriverの設定
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
# GPUアクセラレータ無効
options.add_argument("--disable-gpu")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
# 画像検索のセレクタ
image_selector = "div[jscontroller='lpsUAf']"
# ファイル選択のセレクタ
file_selector = "input[type='file']"
# リンクの取得セレクタ
link_selector = "a.GZrdsf"

# 検索結果を保存するリスト
results = []

try:
    # フォルダ内の画像を取得
    images = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    if not images:
        print("指定したフォルダに画像が見つかりません。")
        exit()

    for image_path in images:
        print(f"検索中の画像: {image_path}")

        # Google画像検索を開く
        driver.get("https://www.google.com/imghp")

        wait = WebDriverWait(driver, 10)

        # カメラアイコンをクリック
        try:
            camera_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, image_selector)))
            camera_icon.click()
        except Exception as e:
            print(f"カメラアイコンのクリック中にエラーが発生しました: {e}")
            continue

        # ファイル選択のダイアログを表示する（"画像をアップロード"は自動で選択される）
        try:
            file_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, file_selector)))
            file_input.send_keys(image_path)
        except Exception as e:
            print(f"画像アップロード中にエラーが発生しました: {e}")
            continue

        # 検索結果が表示されるまで待機 (3秒)
        time.sleep(3)

        # 上位3件のリンクを取得
        links = []
        try:
            search_results = driver.find_elements(By.CSS_SELECTOR, link_selector)[:3]
            for result in search_results:
                links.append(result.get_attribute("href"))
        except Exception as e:
            print(f"リンクの取得中にエラーが発生しました: {e}")

        # 検索結果をリストに保存
        results.append({"image": os.path.basename(image_path), "links": links})
        print(f"取得したリンク: {links}")

        # 少し待機して次の検索へ
        time.sleep(3)

finally:
    # ブラウザを閉じる
    driver.quit()

# 結果をCSVにエクスポート
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["image", "links"])
    writer.writeheader()
    for result in results:
        # リンクリストを文字列に変換して保存
        writer.writerow({"image": result["image"], "links": " | ".join(result["links"])})

print(f"検索結果を {output_file} に保存しました。")
