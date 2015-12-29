import os.path
import re
import xlrd
import xlwt
import time

def is_xls_file(xls_path_fname ,xls_file_name): #判断是否是需要的xls文件
   targe = xls_file_name in xls_path_fname
   return targe

def get_analyze_xls_data(xls_file_path):
   xls_file = xlrd.open_workbook(xls_file_path)
   sheet_name = xls_file.sheet_names()[0]        #获取sheet名字   print(sheet_name)
   xls_file_content_matrix = xls_file.sheet_by_name(sheet_name)  #获取内容的矩阵维度信息   print(content.nrows)   print(content.ncols)
   #按列获取内容
   datatime_sequence = xls_file_content_matrix.col_values(0)   #获取时间戳
   ticks_sequence = xls_file_content_matrix.col_values(1)   #获取ticks
   function_sequence = xls_file_content_matrix.col_values(2)   #获取function
   file_path_sequence = xls_file_content_matrix.col_values(3)   #获取file_path
   sn_sequence = xls_file_content_matrix.col_values(4)   #获取sn
   return datatime_sequence, ticks_sequence, function_sequence, file_path_sequence, sn_sequence


def sequence_mapping_letter_dict(key_word_sequence):  #根据关键字，构建转换字典
   key_word_len = len(key_word_sequence)
   list_sequense = []
   dirlist = {}
   for index in range(key_word_len):
       list_sequense.append(chr(index + 97))
       dirlist[key_word_sequence[index]] = list_sequense[index]
   return dirlist

def sequence_according_dict_to_string(function_sequence, dirlist):   #利用字典将原始function数据，转化成对应的字母字符串
   dict_sequence = [dirlist[i] for i in function_sequence]
   dict_sequence = ''.join(dict_sequence)
   return dict_sequence

def replace_number_sequence(function_sequence, key_str_repalce):#将number = \d+ 转化成 number  因为电话号码不定，因此不好匹配
   for index_key_str in key_str_repalce:
      for index in range(len(function_sequence)):
          if index_key_str in function_sequence[index]:
             function_sequence[index] = index_key_str
   return function_sequence

def accord_regular_get_substring_sequence(data_find_string, sequence, regular_key):#给定判定表达式，得到判定字串
    find_result = re.search(regular_key,sequence)
    if find_result:
        data_find_string.append(find_result.group(0))
        lastindex = find_result.span()[1]
        sequence = sequence[lastindex:]
        accord_regular_get_substring_sequence(data_find_string , sequence, regular_key)
    return data_find_string

def list_unique(old_list):
    new_List = []
    for x in old_list:
        if x not in new_List :
            new_List.append(x)
    return new_List

def find_substr_index(index_list, start_data, data_str, sub_str):   #查找所有的子串在母串中出现sub_str的index，index_list保存所有的结果，start_data默认为0 
    find_answer = data_str.find(sub_str)
    if not find_answer == -1:
       index_list.append(start_data + find_answer)

       start_data = start_data + find_answer + len(sub_str)
       data_str = data_str[find_answer + len(sub_str):]
       answer = find_substr_index(index_list, start_data, data_str, sub_str)
    return index_list

def expend_str_list(index_list, sub_str):
    len_list = len(index_list)
    str_list = []
    str_len_list = []
    index_str_len_list =[]
    for index in range(len_list):
        str_list.append(sub_str)
        str_len_list.append(len(sub_str))
    return str_list, str_len_list
    
def list_append(first_list, second_list):   #多个list追加成一个list
    for index in second_list:
        first_list.append(index)
    return first_list
	
def get_final_sequence(sequence, list_seq): #生成一个二维三列的list，第一行为index，第二行为子字符串list，第三行为子字符串长度
    result_list = []
    index_list = []
    str_list = []
    str_len_list = []
    start_data = 0
    new_list_seq = list_unique(list_seq)
    if new_list_seq:
       for index in new_list_seq:
          indexlist=[]
          indexlist = find_substr_index(indexlist, start_data, sequence, index)
          strlist, strlenlist = expend_str_list(indexlist, index)
          for subindex in range(len(indexlist)):
              if not indexlist[subindex] in index_list:
                 index_list.append(indexlist[subindex])
                 str_list.append(strlist[subindex])
                 str_len_list.append(strlenlist[subindex])
          result_list = [index_list, str_list, str_len_list]
    else:
       result_list = [index_list, str_list, str_len_list]
    return result_list



# 获取单次序列字串记录的时间间隔序列
def one_record_ticks_limit(ticks, str_index, strlen):
    time_gap_sequence = []
    for index in range(strlen - 1):
        first_index = str_index + index
        last_index = first_index + 1
        time_gap = int(ticks[last_index]) - int(ticks[first_index]) #异常信息，读入的数据可能是str格式，所以需要强制转换为int类型
        time_gap_sequence.append(time_gap)
    return time_gap_sequence

def time_limit_function(time_gap_sequence, time_limit):
   bool_value = True
   index = 0
   while index < len(time_gap_sequence) and bool_value:
       if 0 < time_gap_sequence[index] and time_gap_sequence[index] < time_limit:  #limit 单位为毫秒 
           index = index + 1
           continue
       else:
           bool_value = False
   return bool_value

#将文件写到xls
def output_write_to_xlsx(card_switch_map_list, output_filepath, question_type):
   date_time_name = 'date_time'
   ticks_name = 'ticks'
   phenomenon = 'phenomenon'
   reason = 'reason'
   file_path_key='file_directory'
   sn = 'SN'
   keys = (sn, date_time_name, ticks_name, phenomenon, reason, file_path_key)
   widths = (5000, 5000, 3500, 5000, 5000, 20000)
   book=xlwt.Workbook()
   sheet=book.add_sheet(question_type);
   for index in range(len(keys)):
     sheet.col(index).width=widths[index]
     sheet.row(0).write(index,keys[index])   
   for index in range(len(card_switch_map_list)):
      for key_index in range(len(keys)):
         sheet.row(index+1).write(key_index,card_switch_map_list[index][key_index])
   book.save(output_filepath)

def get_xls_answer_file(item_map, output_xls_file_path, output_xls_file_name, question_type):
   #输出到xls
   if item_map:
      time_str = time.strftime('%Y%m%d%X', time.localtime())
      time_str = time_str.replace(':','')
      sStr1 ='answer_log_analyse_' + time_str + output_xls_file_name
      out_put_file=os.path.join(output_xls_file_path, sStr1)
      output_write_to_xlsx(item_map, out_put_file, question_type)

def get_answer_report(key_index_result, datatime_sequence, ticks_sequence,file_path_sequence,sn_sequence, question_type, malloc_sim_phenomenon):
   item_map =[]   
   for index in key_index_result:
      date_time_name_list = []
      ticks_name_list = []
      phenomenon_list = []
      reason_list = []
      file_path_key_list = []
      sn_list = []
      date_time_name_list.append(datatime_sequence[index])
      ticks_name_list.append(ticks_sequence[index])
      phenomenon_list.append(malloc_sim_phenomenon)
      reason_list.append(question_type)
      file_path_key_list.append(file_path_sequence[index])
      sn_list.append(sn_sequence[index])
      item_map_temp = sn_list + date_time_name_list + ticks_name_list + phenomenon_list + reason_list + file_path_key_list
      item_map.append(item_map_temp)
   return item_map
      

#分析单个xls文件满足判断准侧的序列
def single_file_judgement(xls_file_path, xls_file_name, Key_list, key_str_repalce, regular_key_sequence, question_type, ticks_limit_time, malloc_sim_phenomenon):
   datatime_sequence, ticks_sequence, function_sequence, file_path_sequence, sn_sequence = get_analyze_xls_data(xls_file_path)	#从xls文件中获取时间戳，ticks，function序列
   dirlist = sequence_mapping_letter_dict(Key_list)	#根据关键字，构建转换字典
   function_sequence = replace_number_sequence(function_sequence, key_str_repalce)	#将number = \d+ 等类型的数据转化成 number字符
   final_sequence = sequence_according_dict_to_string(function_sequence, dirlist)	#根据字典，将sequence映射成字母型字符串
   data_find_string = []
   data_find_string = accord_regular_get_substring_sequence(data_find_string, final_sequence, regular_key_sequence)		#根据正则表达式逻辑式，查到得到满足要求的子序列
   result_list = get_final_sequence(final_sequence, data_find_string)	#生成正则结果的最终序列list
   
   #判断是否满足时间限制 ticks_limit_time = 0 表示不需要时间判断，else 需要添加时间判断
   if ticks_limit_time:      
      key_index_result = sequence_final_result_function(ticks_sequence, result_list, ticks_limit_time)
   else:
      key_index_result = list_unique(result_list[0])
   key_index_result.sort()
   item_map = get_answer_report(key_index_result, datatime_sequence, ticks_sequence,file_path_sequence, sn_sequence, question_type, malloc_sim_phenomenon)
   return item_map
   
# 写时间判断函数
def sequence_final_result_function(ticks_sequence, result_list, ticks_limit_time):
   key_index_result = []
   sub_sequence_result = []
   sub_sequence_len_result = []
   key_index_init = result_list[0]
   sub_sequence_init = result_list[1]
   sub_sequence_len_init = result_list[2]
   for col_index in range(len(key_index_init)):
      time_gap_sequence = one_record_ticks_limit(ticks_sequence, key_index_init[col_index], sub_sequence_len_init[col_index])
      bool_value = time_limit_function(time_gap_sequence, ticks_limit_time)
      if bool_value:         
         key_index_result.append(key_index_init[col_index])
         sub_sequence_result.append(sub_sequence_init[col_index])
         sub_sequence_len_result.append(sub_sequence_len_init[col_index])

   return key_index_result
   
#分析单路径下满足判断准侧的xls文件序列
def single_path_judgement(xls_file_path, xls_file_name, output_xls_file_name, Key_list, key_str_repalce, regular_key_sequence, question_type, ticks_limit_time, malloc_sim_phenomenon):   
   Listdir = os.listdir(xls_file_path)
   for index in Listdir:      
      if is_xls_file(index, xls_file_name):         
         file_path = os.path.join(xls_file_path,index)
         item_map = single_file_judgement(file_path, xls_file_name, Key_list, key_str_repalce, regular_key_sequence, question_type, ticks_limit_time, malloc_sim_phenomenon)
         get_xls_answer_file(item_map, xls_file_path, output_xls_file_name, question_type)
   
#分析某一路径下所有子路径的xls文件
def analyze_path_all_file_judgement(xls_file_path, xls_file_name, output_xls_file_name, Key_list, key_str_repalce, regular_key_sequence, question_type, ticks_limit_time, malloc_sim_phenomenon):
   for dirpath, dirnames, filenames in os.walk(xls_file_path):
      single_path_judgement(dirpath, xls_file_name, output_xls_file_name, Key_list, key_str_repalce, regular_key_sequence, question_type, ticks_limit_time, malloc_sim_phenomenon)
     
