from setting_file.header import *
from setting_file.scraping_url.browser_scraping_url import URLS


# ChromeDriverのパスを指定
driver_path = "C:/chromedriver.exe"  # 実際のパスに置き換えてください
service = Service(executable_path=driver_path)

# Chromeのオプションを設定
options = Options()

# モバイルエミュレーション設定
mobile_emulation = {
    "deviceMetrics": { "width": 400, "height": 812, "pixelRatio": 1.0 },  # pixelRatio=1.0 に設定
    "userAgent": (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
        "Version/13.1.1 Mobile/15E148 Safari/604.1"
    )
}
options.add_experimental_option("mobileEmulation", mobile_emulation)

# 必要に応じてヘッドレスモードを有効にする
# options.add_argument("--headless")
# options.add_argument('--disable-gpu')

# WebDriverを起動
driver = webdriver.Chrome(service=service, options=options)

# 非表示にしたいCSSセレクタを配列として定義
fixed_elements_selectors = [
    '#sp-bottom-cta',
    '#sell > div.wrapper > div.sp-fixed-banner'
]

def hide_fixed_and_sticky_elements(driver):
    """固定された要素を強制的に非表示にする"""
    driver.execute_script("""
        function hideElements() {
            var allElements = document.querySelectorAll('*');
            for (var i = 0; i < allElements.length; i++) {
                var style = window.getComputedStyle(allElements[i]);
                if (style.position === 'fixed' || style.position === 'sticky') {
                    allElements[i].style.setProperty('display', 'none', 'important');
                }
            }
        }
        
        // ページロード時に一度実行
        hideElements();

        // スクロールイベントにフックして非表示処理を再実行
        window.addEventListener('scroll', function() {
            hideElements();
        });
    """)

def take_full_page_screenshot(url, output_directory):
    # URLのドメイン名とパスを取得してファイル名を作成
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc.replace("www.", "")
    path_name = parsed_url.path.strip('/').replace('/', '-') or "home"
    output_image = f"{domain_name}_{path_name}_full.png"

    # 指定したURLにアクセス
    driver.get(url)

    # ページの読み込みが完了するまで待機
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
    except Exception as e:
        print(f"ページの読み込みに失敗しました: {url}\nエラー: {e}")
        return

    # 固定要素（ヘッダーやフッター）を非表示にする
    hide_fixed_and_sticky_elements(driver)

    # ページ全体の高さを取得
    total_height = driver.execute_script("""
        return Math.max(
            document.body.scrollHeight,
            document.body.offsetHeight,
            document.documentElement.scrollHeight,
            document.documentElement.offsetHeight,
            document.documentElement.clientHeight
        );
    """)

    # ビューポートの高さを取得
    viewport_height = driver.execute_script("return window.innerHeight;")
    viewport_width = driver.execute_script("return window.innerWidth;")

    # スクリーンショットの回数を計算
    num_screenshots = int(total_height / viewport_height) + 1

    # 連結画像の初期化
    stitched_width = viewport_width
    stitched_height = total_height
    stitched_image = Image.new('RGB', (stitched_width, stitched_height))

    for i in range(num_screenshots):
        # 必要な位置までスクロール
        scroll_position = i * viewport_height
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(1)  # スクロールとコンテンツ読み込みを待機

        # スクリーンショットを取得
        screenshot = driver.get_screenshot_as_png()
        screenshot_image = Image.open(BytesIO(screenshot))

        # 貼り付け位置を計算
        y_position = scroll_position

        # 最後のスクリーンショットの場合、高さを調整
        if i == num_screenshots - 1:
            remaining_height = stitched_height - y_position
            if remaining_height < screenshot_image.height:
                screenshot_image = screenshot_image.crop((0, screenshot_image.height - remaining_height, stitched_width, screenshot_image.height))

        # スクリーンショットを連結画像に貼り付け
        stitched_image.paste(screenshot_image, (0, y_position))

        print(f"スクリーンショット {i+1}/{num_screenshots} を取得しました。")

    # 画像を保存
    output_file = os.path.join(output_directory, output_image)
    stitched_image.save(output_file)

    print(f"フルページスクリーンショットを保存しました: {output_file}")

# ファイル保存ディレクトリを指定
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定

# スクリーンショットを取得するURLのリスト
for url in URLS:
    # URLを使った処理
    print(f"Scraping {url}...")


# 各URLに対してスクリーンショットを取得
for url in URLS:
    take_full_page_screenshot(url, file_directory)

# WebDriverを終了
driver.quit()
