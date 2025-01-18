import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting_file.header import *
# 個別URLリストインスタンス
from setting_file.scraping_url.image_get import URLS

# URLリストとセレクタ
url_list = URLS
selector = None  # セレクタが不要な場合は None

# ファイルパス
file_directory = file_path.file_directory  # file_path.py で定義

def download_image(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        print(f"Saving image to: {save_path}")
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {url} -> {save_path}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def process_urls(url_list, selector, file_directory):
    if not os.path.exists(file_directory):
        print(f"Creating directory: {file_directory}")
        os.makedirs(file_directory)
    
    for url in url_list:
        print(f"ダウンロードURL: {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            if selector:  # セレクタが指定されている場合
                soup = BeautifulSoup(response.content, 'html.parser')
                images = soup.select(selector)
                if images:
                    for img in images:
                        img_url = img.get('src') or img.get('data-src')
                        if img_url:
                            full_img_url = urljoin(url, img_url)
                            filename = os.path.basename(full_img_url.split('?')[0])
                            save_path = os.path.join(file_directory, filename)
                            download_image(full_img_url, save_path)
            else:  # セレクタが不要な場合
                filename = os.path.basename(url.split('?')[0])
                save_path = os.path.join(file_directory, filename)
                download_image(url, save_path)
        
        except Exception as e:
            print(f"Error processing {url}: {e}")

# 実行
process_urls(url_list, selector, file_directory)
