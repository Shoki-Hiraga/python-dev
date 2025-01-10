import requests
from bs4 import BeautifulSoup
import time
import csv
import os
import concurrent.futures
import random
import logging
from user_agent import user_agents


# # Configure logging
# logging.basicConfig(filename='log/scraping.log', level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s')

urls = [
'https://www.realoem.com/bmw/ja/partxref?q=51647227926'
]

urls = list(set(urls))

MAX_RETRIES = 3

# Function to scrape a URL
def scrape_url(url):
    delay_time = random.uniform(4, 8) 
    user_agent = random.choice(user_agents)
    retry_count = 0

    while retry_count < MAX_RETRIES:
        try:
            response = requests.get(url, headers={'User-Agent': user_agent})

            if response.status_code == 200:
                time.sleep(delay_time)
                break
            else:
                retry_count += 1
                continue
        except requests.RequestException as e:
            logging.error(f"Error occurred while accessing {url}: {str(e)}")
            return url, [], response.status_code

    else:
        logging.error(f"Failed to retrieve URL: {url}")
        return url, [], response.status_code

    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")
    
    selectors = [
        ('title', 'text')
        # ('li a', 'text'),
        # ('dt a', 'text')
    ]

    scraped_data = [[] for _ in range(len(selectors))]
    
    for index, (selector, *data_types) in enumerate(selectors):
        elements = soup.select(selector)
        if 'link' in data_types:
            scraped_data[index] = [(element.get('href', ''), element.get_text(strip=True)) for element in elements]
        else:
            scraped_data[index] = [element.get_text(strip=True).encode('utf-8').decode('utf-8') for element in elements] 
    
    time.sleep(delay_time)  
    logging.info(f'Delay: {delay_time}, URL: {url}, User Agent: {user_agent}, Response Code: Not tested')
    return url, scraped_data, response.status_code

# Function to log progress
def log_progress(completed_count, total_count):
    percentage_complete = (completed_count / total_count) * 100
    print(f'{percentage_complete} completed.... {completed_count} / {total_count}')
    logging.info(f'Progress: {completed_count}/{total_count} URLs processed ({percentage_complete:.2f}% complete)')

csv_directory = 'C:/Users/STAFF1088/Downloads'
csv_filename = "scraped_data.csv"
csv_filepath = os.path.join(csv_directory, csv_filename)

# Count of completed URLs
completed_count = 0

with open(csv_filepath, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    header_row = ['URL', 'テキスト 1', 'Status Code']
    csv_writer.writerow(header_row)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for url in urls:
            result = scrape_url(url)
            url, scraped_data, status_code = result
            max_length = max(len(data) for data in scraped_data)
            
            for i in range(max_length):
                row_data = [url] + [data[i] if i < len(data) else '' for data in scraped_data] + [status_code]
                csv_writer.writerow(row_data)

            completed_count += 1
            log_progress(completed_count, len(urls))

print('スクレイピングが完了しました。')
