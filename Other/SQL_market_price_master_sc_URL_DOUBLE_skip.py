import sys
import os
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting_file.header import *

input_paths = [
    r"C:\Users\hiraga\Downloads\SQL\market_price_master_2_14.sql",
    r"C:\Users\hiraga\Downloads\SQL\market_price_master3_22.sql",
    r"C:\Users\hiraga\Downloads\SQL\market_price_master3_31.sql"
]

output_path = r"C:\Users\hiraga\Downloads\SQL\market_price_master_after.sql"
filter_keyword = "https://autoc-one.jp/ullo/biddedCar"

output_lines = []
header_written = False
seen_urls = set()
total_matched = 0
total_unique = 0

for path in input_paths:
    with open(path, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    inside_insert = False
    insert_lines = []

    for line in lines:
        if not header_written:
            output_lines.append(line)
            if line.strip().startswith("INSERT INTO"):
                header_written = True
        elif line.strip().startswith("INSERT INTO"):
            inside_insert = True
            insert_lines = [line]
        elif inside_insert:
            insert_lines.append(line)
            if line.strip().endswith(";"):
                insert_block = "".join(insert_lines)
                records = re.findall(r"\((.*?)\)", insert_block, re.DOTALL)

                filtered_records = []
                for rec in records:
                    if filter_keyword in rec:
                        total_matched += 1

                        # sc_url を抽出（'https://.../biddedCar/数字/' 形式）
                        match = re.search(r"'(https://autoc-one\.jp/ullo/biddedCar/\d+/)'", rec)
                        if not match:
                            continue

                        sc_url = match.group(1)

                        if sc_url in seen_urls:
                            continue  # 重複
                        seen_urls.add(sc_url)
                        total_unique += 1

                        parts = rec.split(",", 1)
                        rec_null_id = f"(NULL,{parts[1]}" if len(parts) > 1 else "(NULL)"
                        filtered_records.append(rec_null_id)

                if filtered_records:
                    header = insert_lines[0].split("VALUES")[0] + "VALUES\n"
                    values = ",\n".join(filtered_records) + ";\n"
                    output_lines.append(header + values)

                inside_insert = False
                insert_lines = []

with open(output_path, "w", encoding="utf-8") as outfile:
    outfile.writelines(output_lines)

print(f"✅ 完了: {output_path}")
print(f"🔍 フィルタ条件にマッチした件数: {total_matched}")
print(f"📦 ユニークな sc_url 件数: {total_unique}")
