# -*- coding:utf-8 -*-
import publicfunction.PublicJudgeFunction

def model_restart_main(xls_file_path):
   regular_key_sequence = r'd(ec){4,}[dbcf]'
   Key_list = ['function','Power off', 'number', 'exception_id = 0x02000028', 'exception_id = 0x02000006', 'PushRemalloc', 'simo_local_rev_channel_payload']
   xls_file_name = 'remalloc_sim_model_restart_analyze'
   output_xls_file_name = '_log_model_restart_result.xls'
   key_str_repalce = ['number']
   question_type = 'model_restart'
   ticks_limit_time = 900000
   malloc_sim_phenomenon = 'remalloc_sim'
   publicfunction.PublicJudgeFunction.analyze_path_all_file_judgement(xls_file_path, xls_file_name, output_xls_file_name, Key_list, key_str_repalce, regular_key_sequence, question_type, ticks_limit_time, malloc_sim_phenomenon)
