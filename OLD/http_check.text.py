import requests
from bs4 import BeautifulSoup
from user_agent import user_agents
import random

user_agent = random.choice(user_agents)

def check_response(url, output_path):
    try:
        response = requests.get(url, headers={'User-Agent': user_agent})  # ユーザーエージェントをリクエストに追加
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("HTTPステータスコード: {}\n".format(response.status_code))
            f.write("レスポンスヘッダー:\n")
            for key, value in response.headers.items():
                f.write("{}: {}\n".format(key, value))
            # f.write("レスポンスボディ:\n")
            # f.write(response.text)
            f.write("\nユーザーエージェント:\n")
            f.write(user_agent)  # 選択されたユーザーエージェントを書き込む
        print("出力が完了しました。")
    except requests.exceptions.RequestException as e:
        print("エラー:", e)

# URLと出力パスを指定してHTTPリクエストを送信し、結果をファイルに出力
url = 'https://www.realoem.com/bmw/ja/partxref?q=11000493886'
output_path = r"C:\Users\STAFF1088\Downloads\http_check.txt"
check_response(url, output_path)
