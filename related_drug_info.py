# -*- coding: utf-8 -*-

import json


def find_adjacent_medicines(medicines, current_index, location_info):
    # 查找相邻药品
    adjacent_medicines = []
    for i, med in enumerate(medicines):
        if i != current_index:
            med_location_info = {
                '货架号': med.get('货架号', ''),
                '组': med.get('组', ''),
                '行': med.get('行', ''),
                '列': med.get('列', ''),
            }

            # 仅在药品拥有货架号、行、列、组等属性时再进行比较
            if all(med_location_info.values()):
                if (
                    med_location_info['货架号'] == location_info['货架号'] and
                    med_location_info['组'] == location_info['组'] and
                    (med_location_info['行'] == location_info['行'] or med_location_info['列'] == location_info['列'])
                ):
                    adjacent_medicines.append(med)

    return adjacent_medicines


def add_adjacent_medicine_info(medicines):
    # 为每个药品添加相邻药品信息
    for i, medicine in enumerate(medicines):
        location_info = {
            '货架号': medicine.get('货架号', ''),
            '组': medicine.get('组', ''),
            '行': medicine.get('行', ''),
            '列': medicine.get('列', ''),
        }

        # 仅在药品拥有货架号、行、列、组等属性时才查找相邻药品
        if all(location_info.values()):
            # 查找相邻药品
            adjacent_medicines = find_adjacent_medicines(medicines, i, location_info)
            if adjacent_medicines:
                medicine['相邻药品信息'] = [adj_med['药品名称'] for adj_med in adjacent_medicines]

    return medicines


