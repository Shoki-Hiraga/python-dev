import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting_file.header import *
import subprocess


# Chromeの実行ファイルパス
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # 必要に応じてパスを調整

# Chromeをデバッグモードで起動
subprocess.Popen([chrome_path, "--remote-debugging-port=9222"])

# 少し待機してChromeが起動するのを待つ
time.sleep(3)

# Seleniumでデバッグモードで起動したChromeに接続
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Chromeのブラウザを制御するためにWebDriverを起動
driver = webdriver.Chrome(options=chrome_options)

# 現在のページのタイトルを表示
print(driver.title)

# 任意の操作を実行
driver.get("https://www.example.com")

# 終了する場合は以下を使ってブラウザを閉じる
# driver.quit()
