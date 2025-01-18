from setting_file.header import *

# Chromeのオプションを設定
options = Options()
user_data_dir = 'C:/Users/hiraga/AppData/Local/Google/Chrome/User Data'
profile_name = 'Profile 1'
options.add_argument(f"user-data-dir={user_data_dir}")
options.add_argument(f'--profile-directory={profile_name}')

# ChromeDriverのパスを指定
driver_path = "C:/chromedriver.exe"
service = Service(executable_path=driver_path)

# ファイルパスの設定
# ファイルパス
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定 # file_path.py で定義したファイルディレクトリを指定

input_file = os.path.join(file_directory, 'part_numbers.csv')
output_file = os.path.join(file_directory, 'search_results.csv')
processed_file_name = os.path.join(file_directory, 'processed_part_numbers.txt')

header_low = ['品番', '検索結果']

# WebDriverのインスタンスを生成し、Chromeを起動
driver = webdriver.Chrome(service=service, options=options)

# 処理済み品番の読み込み
processed_part_numbers = set()
if os.path.exists(processed_file_name):
    with open(processed_file_name, 'r') as file:
        processed_part_numbers = {line.strip() for line in file}

# ログイン処理
driver.get("https://auto.tohoweb.co.jp/auth/")
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "X9Kev4ZL2Ox5MhWk8q7JL"))
)
password_field = driver.find_element(By.CLASS_NAME, "_1-3GUaSrfxHOFBNsIIi_kh")
username_field.send_keys("017505")
password_field.send_keys("x7d7ks")
login_button = driver.find_element(By.CLASS_NAME, "_2dH6SOPfO3q7yTMX8kDKus")
login_button.click()

# CSVファイルの読み込みと検索処理
with open(input_file, newline='') as csvfile, \
     open(output_file, 'a', newline='', encoding='utf-8') as resultfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(resultfile)

    # 結果ファイルが空の場合、ヘッダーを書き込む
    if os.stat(output_file).st_size == 0:
        writer.writerow(header_low)

    for row in reader:
        part_number = row[0]
        if part_number in processed_part_numbers:
            continue  # 処理済み品番はスキップ

        driver.get("https://auto.tohoweb.co.jp/estimate/editor/code/new/")
        time.sleep(random.uniform(5, 13))
        
        try:
            input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input._3-jCtq7uP8OrLqK0rRiO15"))
            )
            input_field.clear()
            input_field.send_keys(part_number)
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//button[contains(.,'削除')]"))
            )

            data_elements = driver.find_elements(By.XPATH, "//tr[.//td[contains(@class, '_2Bz-OAc-KH9uZRvx3B4o1J')]]//td")
            result_data = [element.text for element in data_elements]
            writer.writerow([part_number] + result_data)
        except Exception as e:
            print(f"品番 {part_number} の処理中にエラーが発生しました: {e}")
            writer.writerow([part_number, 'エラーまたはデータなし'])

        # 処理済み品番の追加と記録
        with open(processed_file_name, 'a') as processed_file:
            processed_file.write(part_number + '\n')
        processed_part_numbers.add(part_number)

driver.quit()
