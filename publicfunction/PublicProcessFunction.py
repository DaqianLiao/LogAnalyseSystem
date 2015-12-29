import os
import re
import xlwt 
import time


def linesContainKey(file_line,re_key):
    line_list=[]
    index=0
    for index in range(len(file_line)):
        searchObj=re.search(re_key,file_line[index])
        if searchObj:
            line_list.append(index)
    line_list.append(index+1)
    return line_list
def output_to_xlsx(card_switch_map_list, path):
    date_time_name = 'date_time'
    ticks_name = 'ticks'
    function_name = 'function'
    file_path_key='file_directory'
    sn = 'SN'
    keys = (date_time_name,ticks_name, function_name, file_path_key, sn)
    widths = (5000, 5000, 10000,20000, 5000)
    book=xlwt.Workbook()
    sheet=book.add_sheet('process');
    for index in range(len(keys)):
        sheet.col(index).width=widths[index]
        sheet.row(0).write(index,keys[index])
    for index in range(len(card_switch_map_list)):
        for key_index in range(len(keys)):
            sheet.row(index+1).write(key_index,card_switch_map_list[index][keys[key_index]])
    book.save(path)
    return

#分析function表达式
def get_function_Unit(file_line,*keys):
    date_time_name = 'date_time'
    ticks_name = 'ticks'
    function_name = 'function'
    lines=linesContainKey(file_line, keys[2])
    card_unit_map_list=[]
    for index in range(len(lines)-1):
        unit_map={}
        if (re.search(keys[0], file_line[lines[index]])) and (re.search(keys[1], file_line[lines[index]])):
            unit_map[date_time_name] = re.search(keys[0], file_line[lines[index]]).group(0)
            unit_map[ticks_name] = re.search(keys[1], file_line[lines[index]]).group(1)
            unit_map[function_name] = re.search(keys[2], file_line[lines[index]]).group(0)
            card_unit_map_list.append(unit_map)
    return card_unit_map_list
