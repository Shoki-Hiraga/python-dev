from setting_file.header import *
from setting_file.scraping_url.browser_scraping_url import URLS

# ファイル保存ディレクトリを指定
file_directory = file_path.file_directory

# ヘッドレスモードの指定
headlessmode = True

def take_full_page_screenshot(playwright, url, output_directory):
    """フルページスクリーンショットを取得"""
    browser = playwright.chromium.launch(headless=headlessmode)  # ヘッドレスモードでブラウザを起動
    context = browser.new_context(
        viewport={"width": 400, "height": 1000},  # ビューポートサイズを設定
        user_agent=(
            "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "Version/13.1.1 Mobile/15E148 Safari/604.1"
        )
    )
    page = context.new_page()

    # URLのドメイン名とパスを取得してファイル名を作成
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc.replace("www.", "")
    path_name = parsed_url.path.strip('/').replace('/', '-') or "home"
    output_image = f"{domain_name}_{path_name}_full.png"
    output_file = os.path.join(output_directory, output_image)

    try:
        print(f"Scraping {url}...")
        page.goto(url)  # ページにアクセス

        # 固定要素を非表示にする
        page.evaluate("""
        Array.from(document.querySelectorAll('*')).forEach(el => {
            const style = window.getComputedStyle(el);
            if (style.position === 'fixed' || style.position === 'sticky') {
                el.style.display = 'none';
            }
        });
        """)

        # フルページスクリーンショットを保存
        page.screenshot(path=output_file, full_page=True)
        print(f"スクリーンショットを保存: {output_file}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
    finally:
        browser.close()  # ブラウザを閉じる

# Playwrightのメイン処理
def main():
    with sync_playwright() as playwright:
        for url in URLS:
            take_full_page_screenshot(playwright, url, file_directory)

if __name__ == "__main__":
    main()
