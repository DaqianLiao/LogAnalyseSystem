# -*- coding:utf-8 -*-
import publicfunction.PublicJudgeFunction

def All_ok_but_push_main(xls_file_path):
   regular_key_sequence = r'be*([cd]+e{3,}f*){1,}g'
   Key_list = ['function','number', 'service_availability', 'dn_status', 'simo_local_rev_channel_payload', 'exception_id', 'PushRemalloc']
   xls_file_name = 'unremalloc_All_ok_but_push_analyze'
   output_xls_file_name = 'unremalloc_All_ok_but_push_result.xls'
   key_str_repalce = ['number', 'service_availability', 'dn_status', 'simo_local_rev_channel_payload', 'exception_id']

   question_type = 'all_ok_but_pushremalloc'
   ticks_limit_time = 0
   malloc_sim_phenomenon = 'unremalloc_sim'
   publicfunction.PublicJudgeFunction.analyze_path_all_file_judgement(xls_file_path, xls_file_name, output_xls_file_name, Key_list, key_str_repalce, regular_key_sequence, question_type, ticks_limit_time, malloc_sim_phenomenon)
