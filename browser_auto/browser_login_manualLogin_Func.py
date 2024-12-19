import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting_file.header import *

# 最小限の設定
options = Options()

# ChromeDriverManagerを使って、ChromeDriverを管理
service = Service(ChromeDriverManager().install())

# WebDriverを起動
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com/")

# Googleにアクセスして、手動でログイン
driver.get("https://www.google.com/")
print("ログイン後に手動で操作を完了してください。")

# 手動でログインした後に次の操作をプログラムで実行
input("ログイン完了後、Enterキーを押して次のステップへ進んでください...")

# 次の自動操作を行う
driver.find_element(By.XPATH, "//*[@id='gb']/div/div[2]/div[2]/div/a").click()
time.sleep(3)

# 最後にブラウザを閉じる
driver.quit()
