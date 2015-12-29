import xlwt
import xlrd
import os.path

def get_xls_data(xls_file_path):
   xls_file = xlrd.open_workbook(xls_file_path)
   sheet_name = xls_file.sheet_names()[0]        #获取sheet名字   print(sheet_name)
   xls_file_content_matrix = xls_file.sheet_by_name(sheet_name)  #获取内容的矩阵维度信息   print(content.nrows)   print(content.ncols)
   #按列获取内容
   sn_sequence = xls_file_content_matrix.col_values(0)   #获取sn
   sn_sequence = sn_sequence[1:]
   datatime_sequence = xls_file_content_matrix.col_values(1)   #获取时间戳
   datatime_sequence = datatime_sequence[1:]
   ticks_sequence = xls_file_content_matrix.col_values(2)   #获取ticks
   ticks_sequence = ticks_sequence[1:]
   phenomenon_sequence = xls_file_content_matrix.col_values(3)   #获取phenomenon
   phenomenon_sequence = phenomenon_sequence[1:]
   reason_sequence = xls_file_content_matrix.col_values(4)   #获取reason
   reason_sequence = reason_sequence[1:]
   file_path_sequence = xls_file_content_matrix.col_values(5)   #获取file_path
   file_path_sequence = file_path_sequence[1:]

   return sn_sequence, datatime_sequence, ticks_sequence, phenomenon_sequence, reason_sequence, file_path_sequence

def answerfile():
    sn_sequence_list = []
    datatime_sequence_list = []
    ticks_sequence_list = []
    phenomenon_sequence_list = []
    reason_sequence_list = []
    file_path_sequence_list = []
    maplist = []
    return sn_sequence_list, datatime_sequence_list, ticks_sequence_list, phenomenon_sequence_list, reason_sequence_list, file_path_sequence_list, maplist

def TargetFolder(targetpath, datetime):
    outputname = 'loganalyse' + datetime + '.txt'    
    targetfile = os.path.join(targetpath, outputname)
    return targetfile

def list_append(first_list, second_list):   #多个list追加成一个list
    for index in second_list:
        first_list.append(index)
    return first_list

#将文件写到xls
def output_write_to_txt(card_switch_map_list, output_filepath):
   sn = 'SN'
   date_time_name = 'date_time'
   ticks_name = 'ticks'
   phenomenon = 'phenomenon'
   reason = 'reason'
   file_path = 'file_path'
   tab =  '\t'
   enter = '\n'
   if not os.path.exists(output_filepath):
      file = open(output_filepath, 'a')   
      title_string = sn + tab + date_time_name + tab + ticks_name + tab + phenomenon + tab + reason + tab  + file_path + enter
      file.write(title_string)
   else:
      file = open(output_filepath, 'a')
   for index in range(len(card_switch_map_list)):
      content_string = ''
      for key_index in range(len(card_switch_map_list[0])):
         content_string = content_string + card_switch_map_list[index][key_index] + tab
      content_string = content_string + enter
      file.write(content_string)
   file.close()

def conbinedatatomap(log_path):
   file_key = 'answer_log_analyse'
   sn_sequence_list, datatime_sequence_list, ticks_sequence_list, phenomenon_sequence_list, reason_sequence_list, file_path_sequence_list, maplist = answerfile()
   for dirpaths, dirnames, filenames in os.walk(log_path):
      for filename in filenames:
         if os.path.splitext(filename)[1] == '.xls' and file_key in filename:
            xlsfilepath = os.path.join(dirpaths, filename)
            sn_sequence, datatime_sequence, ticks_sequence, phenomenon_sequence, reason_sequence, file_path_sequence = get_xls_data(xlsfilepath)
            os.remove(xlsfilepath)
            list_append(sn_sequence_list, sn_sequence)
            list_append(datatime_sequence_list, datatime_sequence)
            list_append(ticks_sequence_list, ticks_sequence)
            list_append(phenomenon_sequence_list, phenomenon_sequence)
            list_append(reason_sequence_list, reason_sequence)
            list_append(file_path_sequence_list, file_path_sequence)

      for index in range(len(sn_sequence_list)):
         index_list = []
         index_list.append(sn_sequence_list[index])
         index_list.append(datatime_sequence_list[index])
         index_list.append(ticks_sequence_list[index])
         index_list.append(phenomenon_sequence_list[index])
         index_list.append(reason_sequence_list[index])
         index_list.append(file_path_sequence_list[index])
         maplist.append(index_list)
      maplist.sort(key = lambda map_item:(map_item[0],map_item[1]))

      return maplist

def LogFileAnalyse(log_path,datetime):
    if os.path.exists(log_path):
       maplist = conbinedatatomap(log_path)
       targetfile = TargetFolder(log_path, datetime)
       output_write_to_txt(maplist, targetfile)

