import sys
import os
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from setting_file.header import *

input_path = r"C:\Users\hiraga\Downloads\market_price_master3_31.sql"
output_path = r"C:\Users\hiraga\Downloads\market_price_master_after.sql"

filter_keyword = "https://autoc-one.jp/ullo/biddedCar"

with open(input_path, "r", encoding="utf-8") as infile:
    lines = infile.readlines()

output_lines = []
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

            filtered_records = []
            for rec in records:
                if filter_keyword in rec:
                    parts = rec.split(",", 1)  # 最初の1カンマだけ分割
                    rec_null_id = f"(NULL,{parts[1]}" if len(parts) > 1 else "(NULL)"
                    filtered_records.append(rec_null_id)

            if filtered_records:
                header = insert_lines[0].split("VALUES")[0] + "VALUES\n"
                values = ",\n".join(filtered_records) + ";\n"
                output_lines.append(header + values)

            inside_insert = False
            insert_lines = []
    else:
        output_lines.append(line)

with open(output_path, "w", encoding="utf-8") as outfile:
    outfile.writelines(output_lines)

print(f"✅ 完了しました: {output_path}")
