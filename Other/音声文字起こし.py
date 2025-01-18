import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting_file.header import *
import whisper

# ファイルパス
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定

model = whisper.load_model("large")
# result = model.transcribe("準備したファイル名を指定") # 今回の記事ではtest.m4aを用います。
result = model.transcribe("C:/Users/hiraga/Downloads/LANY_MTG.m4a")
print(result["text"])
