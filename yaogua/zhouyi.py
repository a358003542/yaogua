#!/usr/bin/env python
# -*-coding:utf-8-*-

from random import randint
from pkg_resources import resource_filename, resource_string
import json

LIUSHISIGUA = {(1, 1, 1, 1, 1, 1): '乾', (0, 0, 0, 0, 0, 0): '坤',
               (0, 1, 0, 0, 0, 1): '屯', (1, 0, 0, 0, 1, 0): '蒙',
               (0, 1, 0, 1, 1, 1): '需', (1, 1, 1, 0, 1, 0): '讼',
               (0, 0, 0, 0, 1, 0): '师', (0, 1, 0, 0, 0, 0): '比',
               (1, 1, 0, 1, 1, 1): '小畜', (1, 1, 1, 0, 1, 1): '履',
               (0, 0, 0, 1, 1, 1): '泰', (1, 1, 1, 0, 0, 0): '否',
               (1, 1, 1, 1, 0, 1): '同人', (1, 0, 1, 1, 1, 1): '大有',
               (0, 0, 0, 1, 0, 0): '谦', (0, 0, 1, 0, 0, 0): '豫',
               (0, 1, 1, 0, 0, 1): '随', (1, 0, 0, 1, 1, 0): '蛊',
               (0, 0, 0, 0, 1, 1): '临', (1, 1, 0, 0, 0, 0): '观',
               (1, 0, 1, 0, 0, 1): '噬嗑', (1, 0, 0, 1, 0, 1): '贲',
               (1, 0, 0, 0, 0, 0): '剥', (0, 0, 0, 0, 0, 1): '复',
               (1, 1, 1, 0, 0, 1): '无妄', (1, 0, 0, 1, 1, 1): '大畜',
               (1, 0, 0, 0, 0, 1): '颐', (0, 1, 1, 1, 1, 0): '大过',
               (0, 1, 0, 0, 1, 0): '坎', (1, 0, 1, 1, 0, 1): '离',
               (0, 1, 1, 1, 0, 0): '咸', (0, 0, 1, 1, 1, 0): '恒',
               (1, 1, 1, 1, 0, 0): '遁', (0, 0, 1, 1, 1, 1): '大壮',
               (1, 0, 1, 0, 0, 0): '晋', (0, 0, 0, 1, 0, 1): '明夷',
               (1, 1, 0, 1, 0, 1): '家人', (1, 0, 1, 0, 1, 1): '睽',
               (0, 1, 0, 1, 0, 0): '蹇', (0, 0, 1, 0, 1, 0): '解',
               (1, 0, 0, 0, 1, 1): '损', (1, 1, 0, 0, 0, 1): '益',
               (0, 1, 1, 1, 1, 1): '夬', (1, 1, 1, 1, 1, 0): '姤',
               (0, 1, 1, 0, 0, 0): '萃', (0, 0, 0, 1, 1, 0): '升',
               (0, 1, 1, 0, 1, 0): '困', (0, 1, 0, 1, 1, 0): '井',
               (0, 1, 1, 1, 0, 1): '革', (1, 0, 1, 1, 1, 0): '鼎',
               (0, 0, 1, 0, 0, 1): '震', (1, 0, 0, 1, 0, 0): '艮',
               (1, 1, 0, 1, 0, 0): '渐', (0, 0, 1, 0, 1, 1): '归妹',
               (0, 0, 1, 1, 0, 1): '丰', (1, 0, 1, 1, 0, 0): '旅',
               (1, 1, 0, 1, 1, 0): '巽', (0, 1, 1, 0, 1, 1): '兑',
               (1, 1, 0, 0, 1, 0): '涣', (0, 1, 0, 0, 1, 1): '节',
               (1, 1, 0, 0, 1, 1): '中孚', (0, 0, 1, 1, 0, 0): '小过',
               (0, 1, 0, 1, 0, 1): '既济', (1, 0, 1, 0, 1, 0): '未济'}


def get_gua_name(gua):
    if not isinstance(gua, (list, tuple)):
        raise Exception('wrong gua type.')

    if isinstance(gua, list):
        gua = tuple(gua)

    return LIUSHISIGUA[gua]


def zhouyi_yaogua():
    """
    进行一次周易摇卦
    """
    zhugua = []
    biangua = []

    for i in range(0, 6):
        temp_array = []

        for x in range(0, 3):
            n = randint(0, 1)
            temp_array.append(n)

        sum_result = sum(temp_array)

        if sum_result == 3:
            zhugua.append(1)
            biangua.append(0)
        elif sum_result == 2:
            zhugua.append(1)
            biangua.append(1)
        elif sum_result == 1:
            zhugua.append(0)
            biangua.append(0)
        elif sum_result == 0:
            zhugua.append(0)
            biangua.append(1)

    return {
        'zhugua': zhugua,
        'biangua': biangua
    }


def load_yaogua_json_data():
    f = open(resource_filename("yaogua", "yaogua.json"),
             encoding='utf8')

    data = json.load(f)

    return data


def explain_gua(gua):
    """
    获得目标gua的周易原文
    :param gua:
    :return:
    """
    gua_name = get_gua_name(gua)
    data = load_yaogua_json_data()

    def _find_target_gua_in_json(name, data):
        for item in data:
            if item['name'] == name:
                return item

    target = _find_target_gua_in_json(gua_name, data)

    string = f"""{target['name']} {target['symbol']}
    经 {target['jing']}
    彖 {target['tuan']}
    象 {target['xiang']}"""

    return string


def explain_all(data):
    zhugua = data['zhugua']
    biangua = data['biangua']

    zhugua_string = explain_gua(zhugua)
    biangua_string = explain_gua(biangua)

    string = f"""
    主卦
    --------
    {zhugua_string}

    变卦
    --------
    {biangua_string}
"""
    return string
