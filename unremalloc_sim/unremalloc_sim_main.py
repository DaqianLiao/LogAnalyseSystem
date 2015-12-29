
import unremalloc_sim.unremalloc_sim_process.decompression
import unremalloc_sim.unremalloc_sim_process.func01_DP_pass
import unremalloc_sim.unremalloc_sim_process.func02_model_restart
import unremalloc_sim.unremalloc_sim_process.func03_all_ok_but_pushremalloc
import unremalloc_sim.unremalloc_sim_process.func04_VSIM_ok_but_data_fail
import unremalloc_sim.unremalloc_sim_process.func05_Vsim_strength_fail
import unremalloc_sim.unremalloc_sim_process.func06_Vsim_potocol_fail

import unremalloc_sim.unremalloc_sim_analyse.judgement_All_ok_but_push_result
import unremalloc_sim.unremalloc_sim_analyse.judgement_DP_Pass_result
import unremalloc_sim.unremalloc_sim_analyse.judgement_model_restart_result
import unremalloc_sim.unremalloc_sim_analyse.judgement_VSIM_ok_but_data_fail_result
import unremalloc_sim.unremalloc_sim_analyse.judgement_Vsim_strength_fail_result


import time

def unremalloc_main(log_path):
##       #解压
##       unremalloc_sim.unremalloc_sim_process.decompression.decompression_main(log_path)
       #DP过期
       unremalloc_sim.unremalloc_sim_process.func01_DP_pass.DP_pass_main(log_path)
       unremalloc_sim.unremalloc_sim_analyse.judgement_DP_Pass_result.DP_Pass_main(log_path)
       #80重启
       unremalloc_sim.unremalloc_sim_process.func02_model_restart.model_restart_main(log_path)
       unremalloc_sim.unremalloc_sim_analyse.judgement_model_restart_result.model_restart_main(log_path)
       #所有正常客服push
       unremalloc_sim.unremalloc_sim_process.func03_all_ok_but_pushremalloc.all_ok_but_pushremalloc_main(log_path)
       unremalloc_sim.unremalloc_sim_analyse.judgement_All_ok_but_push_result.All_ok_but_push_main(log_path)
       #数据不通
       unremalloc_sim.unremalloc_sim_process.func04_VSIM_ok_but_data_fail.VSIM_ok_but_data_fail_main(log_path)
       unremalloc_sim.unremalloc_sim_analyse.judgement_VSIM_ok_but_data_fail_result.VSIM_ok_but_data_fail_main(log_path)
       #信号问题
       unremalloc_sim.unremalloc_sim_process.func05_Vsim_strength_fail.Vsim_strength_fail_main(log_path)
       unremalloc_sim.unremalloc_sim_analyse.judgement_Vsim_strength_fail_result.Vsim_strength_fail_main(log_path)
       
       unremalloc_sim.unremalloc_sim_process.func06_Vsim_potocol_fail.Vsim_potocol_fail_main(log_path)
   
