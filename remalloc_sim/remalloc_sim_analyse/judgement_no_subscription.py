import publicfunction.PublicJudgeFunction

def judgement_no_subscription_main(xls_file_path):
   regular_key_sequence = r'bd{4,}c'
   Key_list = ['function', 'number', 'exception_id = 0x02000029','cause value = 21']
   xls_file_name = 'remalloc_no_subscription_analyze'
   output_xls_file_name = '_remalloc_no_subscription_result.xls'
   key_str_repalce = ['number']
   question_type = 'no_subscription'
   ticks_limit_time = 0
   malloc_sim_phenomenon = 'remalloc_sim'
   publicfunction.PublicJudgeFunction.analyze_path_all_file_judgement(xls_file_path, xls_file_name, output_xls_file_name, Key_list, key_str_repalce, regular_key_sequence, question_type, ticks_limit_time, malloc_sim_phenomenon)
