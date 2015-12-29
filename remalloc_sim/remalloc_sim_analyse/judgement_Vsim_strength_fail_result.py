import publicfunction.PublicJudgeFunction

def Vsim_strength_fail_main(xls_file_path):
   regular_key_sequence = r'cd+eb[fg]'
   Key_list = ['function', 'number', 'strength_in_percentage', 'service_availability', 'exception_id = 0x02000006', 'PushRemalloc', 'Power off']
   xls_file_name = 'remalloc_sim_Vsim_strength_fail_analyze'
   output_xls_file_name = '_remalloc_Vsim_strength_fail_result.xls'
   key_str_repalce = ['number', 'strength_in_percentage', 'service_availability']
   question_type = 'Vsim_strength_fail'
   ticks_limit_time = 600000
   malloc_sim_phenomenon = 'remalloc_sim'
   publicfunction.PublicJudgeFunction.analyze_path_all_file_judgement(xls_file_path, xls_file_name, output_xls_file_name, Key_list, key_str_repalce, regular_key_sequence, question_type, ticks_limit_time, malloc_sim_phenomenon)
