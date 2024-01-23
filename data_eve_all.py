import json
from Parse_spatial_information import process_medicine_data
from related_drug_info import add_adjacent_medicine_info

file_path = 'drug_v3.json'
with open(file_path, 'r', encoding='utf-8') as file:
    try:
        json_data = json.load(file)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        exit()

output = process_medicine_data(json_data)
result = add_adjacent_medicine_info(output)
formatted_output = json.dumps(result, ensure_ascii=False, indent=2)

# 将修改后的数据写回原始文件
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(formatted_output)

print(f"修改后的 JSON 数据已成功写回文件: {file_path}")
