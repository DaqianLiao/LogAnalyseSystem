# -*- coding:utf-8 -*-
import publicfunction.PublicJudgeFunction

def fight_model_connect_data_main(xls_file_path):
   regular_key_sequence = r'(be*([df]+c*)){4,}'
   Key_list = ['function', 'number', 'exception_id = 0x02000006', 'exception_id = 0x02000014','exception_id = 0x02000013', 'exception_id = 0x02000029']
   xls_file_name = 'remalloc_sim_fight_model_connect_data_analyze'
   output_xls_file_name = '_fight_model_connect_data_result.xls'
   key_str_repalce = ['number']
   question_type = 'fight_model_connect_data'
   ticks_limit_time = 0
   malloc_sim_phenomenon = 'unremalloc_sim'
   publicfunction.PublicJudgeFunction.analyze_path_all_file_judgement(xls_file_path, xls_file_name, output_xls_file_name, Key_list, key_str_repalce, regular_key_sequence, question_type, ticks_limit_time, malloc_sim_phenomenon)
