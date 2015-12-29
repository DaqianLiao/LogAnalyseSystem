# -*- coding:utf-8 -*-
import publicfunction.PublicJudgeFunction

def VSIM_ok_but_data_fail_main(xls_file_path):
   regular_key_sequence = r'b[cd]{5,}'
   Key_list = ['function', 'number', 'exception_id = 0x02000008', 'exception_id = 0x0200000a', 'PushRemalloc']
   xls_file_name = 'unremalloc_VSIM_ok_but_data_fail_anaylse'
   output_xls_file_name = '_unremalloc_VSIM_ok_but_data_fail_result.xls'
   key_str_repalce = ['number']
   question_type = 'VSIM_ok_but_data_fail'
   ticks_limit_time = 0
   malloc_sim_phenomenon = 'unremalloc_sim'
   publicfunction.PublicJudgeFunction.analyze_path_all_file_judgement(xls_file_path, xls_file_name, output_xls_file_name, Key_list, key_str_repalce, regular_key_sequence, question_type, ticks_limit_time, malloc_sim_phenomenon)
