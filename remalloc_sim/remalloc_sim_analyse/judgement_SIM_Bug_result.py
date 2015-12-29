import publicfunction.PublicJudgeFunction

def SIM_Bug_main(xls_file_path):
   regular_key_sequence = r'(bc+([ef]+){1,}d*)'#超过2次以上出现SIM卡bug的，才认为是问题
   Key_list = ['function', 'number', 'card_type = 0', 'exception_id = 0x02000006', 'exception_id = 0x02000013', 'exception_id = 0x02000014']
   xls_file_name = 'remalloc_sim_SIM_Bug_analyze'
   output_xls_file_name = '_log_SIM_Bug_result.xls'
   key_str_repalce = ['number']
   question_type = 'SIM_Bug'
   ticks_limit_time = 1800000
   malloc_sim_phenomenon = 'remalloc_sim'
   publicfunction.PublicJudgeFunction.analyze_path_all_file_judgement(xls_file_path, xls_file_name, output_xls_file_name, Key_list, key_str_repalce, regular_key_sequence, question_type, ticks_limit_time, malloc_sim_phenomenon)
