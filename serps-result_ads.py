from setting_file.header import *

def scrape_google_ads():
    base_url = "https://www.google.com"
    user_agent = random.choice(user_agents)
    search_query = "車 買取"
    headers = {'User-Agent': user_agent}

    csv_headers = ["URL", "Title"]
    csv_directory = csv_output_path.out_office
    # csv_directory = csv_output_path.out_main
    # csv_directory = csv_output_path.out_raytrek
    csv_filename = "ad_search_results.csv"
    output_file = os.path.join(csv_directory, csv_filename)

    with open(output_file, "w", encoding="utf-8", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(csv_headers)

        for page in range(1, 11):
            search_url = f"{base_url}/search?q={search_query}&adtest=on&start={page * 10}"
            delay = random.uniform(3, 10)
            # search_url = f"{base_url}/search?q={search_query}&adtest=on&start={page * 1}"
            # delay = random.uniform(0.1, 1)
            time.sleep(delay)
            response = requests.get(search_url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")

            # ステータスコードを表示
            print(f"検索URL: {search_url}")
            print(f"Status Code: {response.status_code}")
            print(f"----------遅延処理 {delay}----------")

            # 広告の親要素を抽出
            ad_blocks = soup.select("#taw div.vdQmEd")

            for ad_block in ad_blocks:
                url_tag = ad_block.select_one("#taw a.sVXRqc")
                title_tag = ad_block.select_one("#taw .CCgQ5 span")
                
                if url_tag and title_tag:
                    url = url_tag['href']
                    title = title_tag.text
                    csv_writer.writerow([url, title])
                    print(f"取得データ: {url} - {title}")
                else:
                    print("No valid ad block found.")

scrape_google_ads()
