# -*- coding:utf-8 -*-
import publicfunction.PublicJudgeFunction

def DP_Pass_main(xls_file_path):
   regular_key_sequence = r'[bc]+g'
   Key_list = ['function','PushDaypassExpired', '_action_excute_a7_result',  '_action_excute_a18_result', 'simo_order_user_package_req', 'simo_order_user_package_req', 'PushRemalloc']
   xls_file_name = 'unremalloc_DP_Pass_analyze'
   output_xls_file_name = 'unremalloc_DP_Pass_result.xls'
   key_str_repalce = ['_action_excute_a7_result', '_action_excute_a18_result']
   question_type = 'DP_Pass'
   ticks_limit_time = 0
   malloc_sim_phenomenon = 'unremalloc_sim'
   publicfunction.PublicJudgeFunction.analyze_path_all_file_judgement(xls_file_path, xls_file_name, output_xls_file_name, Key_list, key_str_repalce, regular_key_sequence, question_type, ticks_limit_time, malloc_sim_phenomenon)
