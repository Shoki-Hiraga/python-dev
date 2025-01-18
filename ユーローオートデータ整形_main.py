import csv
import re
import os
from setting_file import csv_output_path, api_json  # 設定ファイルからCSVの出力パスとAPIのJSONをインポート
os.chdir(os.path.dirname(os.path.abspath(__file__)))# スクリプトが存在するディレクトリを作業ディレクトリとして設定

# ユーローオートデータ整形_main.pyの内容

# Pythonスクリプトファイルを実行する関数を定義
def run_script(filename):
    with open(filename, 'rb') as file:
        exec(compile(file.read(), filename, 'exec'))

if __name__ == "__main__":
    # 順番にスクリプトを実行
    run_script('in非対応車種_重複整理_括弧除外_out対応車種車種_配列ver2.py')
    run_script('指定列データ置換.py')
    run_script('シリーズ_のカンマ区切り.py')
    run_script('重複データのみ_削除_整理_uniqe.py')
