#-*-coding:utf-8 -*-
import os
import re
import xlwt 
import time
import publicfunction.PublicProcessFunction

date_time = r'\d{4}(-\d\d){2} \d{2}(:\d\d){2}'
date_time_name = 'date_time'
ticks = r'ticks:(\d+)'
malloc_number = r'number = \d+'
Vsim_Reg_server_fail = r'exception_id = 0x02000006'
model_restart = r'exception_id = 0x02000028'
PushRemalloc = r'PushRemalloc'
pown_on = r'Power off'


def analysFile(file_path):
    file_path_key = 'file_directory'
    file_SN = 'SN'
    sn_index = file_path.find('sky')
    sn_string = file_path[sn_index:sn_index + 16]
    file = open(file_path,errors='ignore')
    lines = file.readlines()
##    print('{%s}total line:%d'%(file_path,len(lines)))
    list_map1 = publicfunction.PublicProcessFunction.get_function_Unit(lines, date_time, ticks, malloc_number)
    list_map2 = publicfunction.PublicProcessFunction.get_function_Unit(lines, date_time, ticks, model_restart)
    list_map3 = publicfunction.PublicProcessFunction.get_function_Unit(lines, date_time, ticks, Vsim_Reg_server_fail)
    list_map4 = publicfunction.PublicProcessFunction.get_function_Unit(lines, date_time, ticks, pown_on)
    list_map5 = publicfunction.PublicProcessFunction.get_function_Unit(lines, date_time, ticks, PushRemalloc) 
    list_map = list_map1 + list_map2 + list_map3 + list_map4 + list_map5
   
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
           sStr1 = 'unremalloc_model_restart_analyze_' + time_str + '.xls'
           out_put_file=os.path.join(dirpath, sStr1)
           publicfunction.PublicProcessFunction.output_to_xlsx(TxtList,out_put_file)
    return TxtList

def model_restart_main(log_path):
    out_list = analys_txtfile_all(log_path)   

