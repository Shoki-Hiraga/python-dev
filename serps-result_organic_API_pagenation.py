from setting_file.header import *
from setting_file.scraping_KW.organic_KW_pagenation import search_keywords_list

# APIキーの選択
api_key_index = 1 # 使用するAPIキーのインデックス番号
api_keys = {
    1: gcp_api.custom_search_API_KEY_current,
    2: gcp_api.custom_search_API_KEY_332r,
    3: gcp_api.custom_search_API_KEY_idea,
    4: gcp_api.custom_search_API_KEY_shotest,
    5: gcp_api.custom_search_API_KEY_2sho,
    6: gcp_api.custom_search_API_KEY_seohira
}

google_api_key = api_keys[api_key_index] # APIキーの取得

# カスタムサーチエンジンID
# CUSTOM_SEARCH_ENGINE_ID = gcp_api.custom_search_ENGINE_ID_332r
CUSTOM_SEARCH_ENGINE_ID = gcp_api.custom_search_ENGINE_ID_current

# リクエストの遅延時間を定義
delaytime = 2.000002


# ファイルパス
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定
file_name = "site_search_results_pagenation5.csv"
output_file = os.path.join(file_directory, file_name)

# 1ページあたりの検索件数
results_per_page = 10
# ページネーションを何ページ取得するか指定
max_pages_to_fetch = 1

# Google Custom Search APIサービスの構築
service = build("customsearch", "v1", developerKey=google_api_key)

# CSVファイルの初期化
if not os.path.exists(file_directory):
    os.makedirs(file_directory)

with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Keyword", "URL", "Meta Title"])

# 検索とCSV出力
def search_and_write_to_csv(keyword):
    try:
        search_results = []
        for page in range(max_pages_to_fetch):
            start_index = page * results_per_page + 1

            res = service.cse().list(
                q=keyword,
                cx=CUSTOM_SEARCH_ENGINE_ID,
                num=results_per_page,
                start=start_index
            ).execute()

            items = res.get("items", [])
            if not items:
                break

            for item in items:
                url = item.get("link")
                title = item.get("title")
                search_results.append([keyword, url, title])

            time.sleep(delaytime)
            print(f"{delaytime}秒の遅延が完了しました")

        with open(output_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(search_results)

        print(f"Keyword '{keyword}' processed successfully. Found {len(search_results)} results.")

    except Exception as e:
        print(f"このKWでエラーが発生しました '{keyword}': {e}")

# 各キーワードに対して検索を実行
for keyword in search_keywords_list:
    search_and_write_to_csv(keyword)
