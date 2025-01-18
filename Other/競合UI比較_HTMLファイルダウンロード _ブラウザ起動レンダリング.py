import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting_file.header import *

# Chromeドライバーの設定
options = Options()
# options.add_argument('--headless')  # ヘッドレスモード
user_agent = random.choice(user_agents)  # ランダムにUser-Agentを選択
options.add_argument(f'user-agent={user_agent}')  # User-Agentを設定
driver = webdriver.Chrome(options=options)

# ファイルパス
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定

# 個別URLリストインスタンス
urls = [
"https://www.qsha-oh.com/maker/nissan/skyline/",
"https://ucarpac.com/sell/m002/n027",
"https://autoc-one.jp/ullo/biddedCarList/ma35/mo1639/",
"https://s.kakaku.com/item/70100310105/kaitori/",
"https://www.goo-net.com/kaitori/maker_guide/show/1015/10151010/",
"https://kaitori.carsensor.net/NI/S030/",
"https://221616.com/satei/souba/nissan/skyline/",
"https://autoc-one.jp/catalog/nissan/skyline/kaitori/",
"https://kaitori.carview.co.jp/souba/nissan/skyline/",
"https://www.navikuru.jp/souba/nissan/skyline-sedan/",
"https://www.nextage.jp/kaitori/souba/nissan/skyline/",
"https://www.kurumaerabi.com/kaitori/marketprice/cartype/2/208/",
]

# URLからファイル名を生成する関数
def generate_filename(url):
    filename = url.replace('https://', '').replace('http://', '').replace('/', '-')
    return f"{filename}.html"

# URLリストに対してスクレイピングを実行し、JavaScriptレンダリング後のHTMLを保存
for url in urls:
    driver.get(url)
    time.sleep(5)  # JavaScriptのレンダリング待機時間
    
    # ページのHTMLを取得
    html_content = driver.page_source

    # ファイル名とパスを設定
    filename = generate_filename(url)
    file_path.file_directory = os.path.join(file_directory, filename)

    # HTMLコンテンツをファイルに保存
    with open(file_path.file_directory, mode='w', encoding='utf-8') as file:
        file.write(html_content)
    
    print(f"Saved rendered HTML content for {url} as {filename}")

driver.quit()
print('全てのページのレンダリング完了および保存が完了しました。')
