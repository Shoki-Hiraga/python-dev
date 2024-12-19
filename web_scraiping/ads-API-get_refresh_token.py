import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting_file.header import *
from googleapiclient.discovery import build
from google.oauth2 import service_account
from oauth2client.service_account import ServiceAccountCredentials


# クライアントIDとクライアントシークレットが含まれるJSONファイルを指定する
# CLIENT_SECRETS_FILE = "C:/Users/hiraga/Desktop/Python-dev/setting_file/json_file/ads-api_private_client_secret_827980945440-aalm2mrlqrsgkcrfvt90cegnbbg8l206.apps.googleusercontent.com.json"
CLIENT_SECRETS_FILE = "C:/Users/hiraga/Desktop/Python-dev/setting_file/json_file/ads-api_current_client_secret_938116253219-skvsisjd3ledggousef891dt075bmcd0.apps.googleusercontent.com.json"

# Google Ads APIのスコープ
SCOPES = ['https://www.googleapis.com/auth/adwords']

# OAuth 2.0認証フローを使用してリフレッシュトークンを取得
def get_refresh_token():
    # OAuth 2.0 フローのインスタンスを作成
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)

    # ユーザーに認証を求めるブラウザを開く
    credentials = flow.run_local_server(port=0)

    # リフレッシュトークンを取得
    print("Access token: ", credentials.token)
    print("Refresh token: ", credentials.refresh_token)
    print("Token expiry: ", credentials.expiry)

if __name__ == "__main__":
    get_refresh_token()
