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

# WebDriverのインスタンスを生成し、Chromeを起動
driver = webdriver.Chrome(service=service, options=options)

# ログインが必要かどうかを選択
login_required = input("ログインが必要な場合は '1' を、不要な場合は '2' を入力してください: ")

if login_required == '1':
    # ログイン処理
    driver.get("https://ssl.aucfan.com/member/login")
    try:
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "loginInputBlock"))
        )
        password_field = driver.find_element(By.CSS_SELECTOR, "loginInputBlock supBtn")
        username_field.send_keys("chaser.cb750@gmail.com")
        password_field.send_keys("78195090Cb")
        login_button = driver.find_element(By.CSS_SELECTOR, "btnType01 btnColor07 btnSize01 loginSubmitBtn")
        login_button.click()
    except Exception as e:
        print(f"ログイン処理中にエラーが発生しました: {e}")
        driver.quit()
        exit(1)

# 入力フィールドと検索ボタンのセレクタを指定
input_selector = input("検索ボックスのCSSセレクタを入力してください: ")
input_text = input("検索ボックスに入力するテキストを入力してください: ")
button_selector = input("検索ボタンのCSSセレクタを入力してください: ")

# 指定されたページに移動
url = input("スクレイピングを行うURLを入力してください: ")
driver.get(url)

try:
    # 入力フィールドにテキストを入力
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, input_selector))
    )
    input_field.clear()
    input_field.send_keys(input_text)

    # 検索ボタンをクリック
    search_button = driver.find_element(By.CSS_SELECTOR, button_selector)
    search_button.click()

    print("入力およびボタンのクリックが正常に行われました。")

except Exception as e:
    print(f"入力フォームの処理中にエラーが発生しました: {e}")

driver.quit()
