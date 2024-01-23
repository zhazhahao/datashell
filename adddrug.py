# -*- coding: utf-8 -*-

import json


def add_medicine(medicines, new_medicine):
    # 添加新药品信息
    medicines.append(new_medicine)
    return medicines


# 读取本地JSON文件
file_path = 'drug_v3.json'
with open(file_path, 'r', encoding='utf-8') as file:
    try:
        data = json.load(file)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        exit()

# 用户输入新药品信息
new_medicine = {
    '货位号': input("请输入新药品的货位号："),
    '药品代码': input("请输入新药品的药品代码："),
    '药品名称': input("请输入新药品的药品名称："),
    '药品规格': input("请输入新药品的药品规格："),
    '库存量': input("请输入新药品的库存量："),
    '厂家': input("请输入新药品的厂家："),
    '大包装量': input("请输入新药品的大包装量："),
    '大包装规格': input("请输入新药品的大包装规格："),
}

# 添加新药品信息
updated_data = add_medicine(data, new_medicine)

# 将更新后的数据写回文件
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(updated_data, file, ensure_ascii=False, indent=2)

print("药品信息已成功添加。")
