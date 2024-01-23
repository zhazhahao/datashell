# -*- coding: utf-8 -*-

import re


def extract_location_code(location):
    # 使用正则表达式匹配字母加六位数字的模式
    match = re.match(r'([A-Za-z])(\d{2})(\d{2})(\d{2})', location)
    if match:
        shelf, group, row, column = match.groups()
        return {
            '货架号': shelf,
            '组': group,
            '行': row,
            '列': column,
        }
    else:
        return None


def extract_location_code_4(location):
    # 使用正则表达式匹配字母加四位数字的模式
    match = re.match(r'([A-Za-z])(\d{2})(\d{2})', location)
    if match:
        shelf, row, column = match.groups()
        return {
            '货架号': shelf,
            '行': row,
            '列': column,
        }
    else:
        return None


def process_medicine_data(medicines):
    # 处理每个药品的数据
    for medicine in medicines:
        location = medicine.get('货位号', '')
        location_info = extract_location_code(location)

        # 如果货位号符合要求，则添加属性
        if location_info:
            medicine.update(location_info)
        else:
            location_info4 = extract_location_code_4(location)
        if location_info4:
            medicine.update(location_info4)
    return medicines
