#-*-coding:utf-8 -*-
import os
import re
import xlwt
import time
import publicfunction.PublicProcessFunction

date_time = r'\d{4}(-\d\d){2} \d{2}(:\d\d){2}'
date_time_name = 'date_time'
ticks = r'ticks:(\d+)'
ticks_name = 'ticks'
Vsim_strength = r'_simo_nw_info_trace_check.*strength_in_percentage = (0|10)\b'
Vsim_service_availability = r'_simo_nw_info_trace_check.*service_availability = \d'
malloc_number = r'number = \d+'
Vsim_data_success = r'simo_local_rev_channel_payload'
PushRemalloc = r'PushRemalloc'
power_off = r'Power off'
function_name = 'function'


def analysFile(file_path):
    file_path_key = 'file_directory'
    file_SN = 'SN'
    sn_index = file_path.find('sky')
    sn_string = file_path[sn_index:sn_index + 16]
    file = open(file_path,errors='ignore')
    lines = file.readlines()
##    print('{%s}total line:%d'%(file_path,len(lines)))
    list_map1 = publicfunction.PublicProcessFunction.get_function_Unit(lines, date_time, ticks, Vsim_strength)
    list_map2 = publicfunction.PublicProcessFunction.get_function_Unit(lines, date_time, ticks, Vsim_service_availability)
    list_map3 = publicfunction.PublicProcessFunction.get_function_Unit(lines, date_time, ticks, malloc_number)
    list_map4 = publicfunction.PublicProcessFunction.get_function_Unit(lines, date_time, ticks, PushRemalloc)
    list_map5 = publicfunction.PublicProcessFunction.get_function_Unit(lines, date_time, ticks, power_off)
    list_map6 = publicfunction.PublicProcessFunction.get_function_Unit(lines, date_time, ticks, Vsim_data_success) 
    list_map = list_map1 + list_map2 + list_map3  + list_map4 + list_map5 + list_map6
   
    for map_item in list_map:
        map_item[file_path_key]=file_path
        map_item[file_SN] = sn_string
    list_map.sort(key = lambda map_item:(map_item[date_time_name]))
    file.close()
    return list_map

#分析指定路径下的所有文件
def  analys_txtfile_all(log_path):    
    for dirpath, dirnames, filenames in os.walk(log_path):
        TxtList = []
        for filename in filenames:
            if os.path.splitext(filename)[1] == '.txt':
               txtfilepath = os.path.join(dirpath, filename)
               outlist = analysFile(txtfilepath)
               TxtList = TxtList + outlist
##            else:
##                print(dirpath + ':  There is no txt file')
        if TxtList:
           TxtList.sort(key = lambda map_item:(map_item[date_time_name]))
           time_str = time.strftime('%Y%m%d%X', time.localtime())
           time_str = time_str.replace(':','')
           sStr1 = 'unremalloc_Vsim_strength_fail_analyze_' + time_str + '.xls'
           out_put_file = os.path.join(dirpath, sStr1)
           publicfunction.PublicProcessFunction.output_to_xlsx(TxtList,out_put_file)
    return TxtList

def Vsim_strength_fail_main(log_path):
    out_list = analys_txtfile_all(log_path)       

