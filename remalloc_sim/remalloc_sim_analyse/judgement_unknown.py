import publicfunction.PublicJudgeFunction

def judgement_unknown_main(xls_file_path):
   regular_key_sequence = r'(bc){2,}'
   Key_list = ['function', 'number', 'exception_id = 0x02000006', 'exception_id = 0x02000014','exception_id = 0x02000013', 'exception_id = 0x02000028', 'exception_id = 0x02000029','card_type = 0']
   xls_file_name = 'remalloc_unknown_analyze'
   output_xls_file_name = '_remalloc_unknown_result.xls'
   key_str_repalce = ['number']
   question_type = 'unknown'
   ticks_limit_time = 0
   malloc_sim_phenomenon = 'remalloc_sim'
   publicfunction.PublicJudgeFunction.analyze_path_all_file_judgement(xls_file_path, xls_file_name, output_xls_file_name, Key_list, key_str_repalce, regular_key_sequence, question_type, ticks_limit_time, malloc_sim_phenomenon)
