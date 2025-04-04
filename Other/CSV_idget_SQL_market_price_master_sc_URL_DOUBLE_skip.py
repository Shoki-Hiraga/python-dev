import sys
import os
import re
import csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting_file.header import *

input_paths = [
    r"C:\Users\hiraga\Downloads\SQL\market_price_master_2_14.sql",
    r"C:\Users\hiraga\Downloads\SQL\market_price_master3_22.sql",
    r"C:\Users\hiraga\Downloads\SQL\market_price_master3_31.sql",
    r"C:\Users\hiraga\Downloads\SQL\market_price_master4_4.sql",
    r"C:\Users\hiraga\Downloads\SQL\market_price_mota4_4.sql"
]

output_csv_path = r"C:\Users\hiraga\Downloads\SQL\market_price_master_after.csv"
filter_keyword = "https://autoc-one.jp/ullo/biddedCar"

seen_urls = set()
total_matched = 0
total_unique = 0
csv_rows = []

# ID 初期化（任意で1000001などにしてもOK）
new_id = 1

for path in input_paths:
    with open(path, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    inside_insert = False
    insert_lines = []

    for line in lines:
        if line.strip().startswith("INSERT INTO"):
            inside_insert = True
            insert_lines = [line]
        elif inside_insert:
            insert_lines.append(line)
            if line.strip().endswith(";"):
                insert_block = "".join(insert_lines)
                records = re.findall(r"\((.*?)\)", insert_block, re.DOTALL)

                for rec in records:
                    if filter_keyword in rec:
                        total_matched += 1

                        match = re.search(r"'(https://autoc-one\.jp/ullo/biddedCar/\d+/)'", rec)
                        if not match:
                            continue
                        sc_url = match.group(1)

                        if sc_url in seen_urls:
                            continue
                        seen_urls.add(sc_url)
                        total_unique += 1

                        fields = [f.strip().strip("'") for f in re.split(r",(?![^()]*\))", rec)]
                        if len(fields) < 11:
                            continue

                        # ID を連番で付与
                        fields[0] = str(new_id)
                        new_id += 1

                        csv_rows.append(fields)

                inside_insert = False
                insert_lines = []

# CSV ヘッダー
header = [
    "id", "maker_name_id", "model_name_id", "grade_name_id", "year",
    "mileage", "min_price", "max_price", "sc_url", "created_at", "updated_at"
]

# 書き出し
with open(output_csv_path, "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(csv_rows)

print(f"✅ CSV出力完了: {output_csv_path}")
print(f"🔍 フィルタに一致した全件数: {total_matched}")
print(f"📦 CSV出力件数（ユニークなsc_url）: {total_unique}")
