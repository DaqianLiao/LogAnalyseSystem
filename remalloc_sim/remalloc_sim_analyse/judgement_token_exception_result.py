import publicfunction.PublicJudgeFunction

def token_exception_main(xls_file_path):
   regular_key_sequence = r'd(ec){4,}b'
   Key_list = ['function','Power off', 'number', 'exception_id = 0x04000002', 'exception_id = 0x02000006']
   xls_file_name = 'remalloc_sim_token_exception_analyze'
   output_xls_file_name = '_log_token_exception_result.xls'
   key_str_repalce = ['number']
   question_type = 'token_exception'
   ticks_limit_time = 0
   malloc_sim_phenomenon = 'remalloc_sim'
   publicfunction.PublicJudgeFunction.analyze_path_all_file_judgement(xls_file_path, xls_file_name, output_xls_file_name, Key_list, key_str_repalce, regular_key_sequence, question_type, ticks_limit_time, malloc_sim_phenomenon)
