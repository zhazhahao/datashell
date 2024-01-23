# -*- coding: utf-8 -*-

import json


def find_medicine_by_name(medicines, target_name):
    # 查找药品信息
    matching_medicines = [med for med in medicines if med.get('药品名称') == target_name]
    return matching_medicines


# 读取本地JSON文件
file_path = 'drug_v3.json'
with open(file_path, 'r', encoding='utf-8') as file:
    try:
        data = json.load(file)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        exit()

# 接入ocr识别结果
target_medicine_name = input("请输入要查找的药品名称：")

# 查找药品信息
matching_medicines = find_medicine_by_name(data, target_medicine_name)

# 输出结果
if matching_medicines:
    print(f"找到药品'{target_medicine_name}'的信息：")
    for medicine in matching_medicines:
        print(json.dumps(medicine, ensure_ascii=False, indent=2))
else:
    print(f"未找到药品'{target_medicine_name}'的信息。")
