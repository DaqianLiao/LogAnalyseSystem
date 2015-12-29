import remalloc_sim.remalloc_sim_process.decompression
import remalloc_sim.remalloc_sim_process.func01model_restart
import remalloc_sim.remalloc_sim_process.func02SIM_Bug
import remalloc_sim.remalloc_sim_process.func03Vsim_potocol_fail
import remalloc_sim.remalloc_sim_process.func04Vsim_strength_fail
import remalloc_sim.remalloc_sim_process.func05token_exception
import remalloc_sim.remalloc_sim_process.func06fight_model_connect_data
import remalloc_sim.remalloc_sim_process.func07unknown
import remalloc_sim.remalloc_sim_process.func08no_subscription


import remalloc_sim.remalloc_sim_analyse.judgement_fight_model_connect_data_result
import remalloc_sim.remalloc_sim_analyse.judgement_model_restart_result
import remalloc_sim.remalloc_sim_analyse.judgement_SIM_Bug_result
import remalloc_sim.remalloc_sim_analyse.judgement_token_exception_result
import remalloc_sim.remalloc_sim_analyse.judgement_Vsim_strength_fail_result
import remalloc_sim.remalloc_sim_analyse.judgement_unknown
import remalloc_sim.remalloc_sim_analyse.judgement_no_subscription


def remalloc_main(log_path):
       #解压
       remalloc_sim.remalloc_sim_process.decompression.decompression_main(log_path)
       #80重启
##       remalloc_sim.remalloc_sim_process.func01model_restart.model_restart_main(log_path)
##       remalloc_sim.remalloc_sim_analyse.judgement_model_restart_result.model_restart_main(log_path)
       #SIM卡BUG
       remalloc_sim.remalloc_sim_process.func02SIM_Bug.SIM_Bug_main(log_path)
       remalloc_sim.remalloc_sim_analyse.judgement_SIM_Bug_result.SIM_Bug_main(log_path)       
       #信号强度不好，自动换卡
##       remalloc_sim.remalloc_sim_process.func04Vsim_strength_fail.Vsim_strength_fail_main(log_path)
##       remalloc_sim.remalloc_sim_analyse.judgement_Vsim_strength_fail_result.Vsim_strength_fail_main(log_path)
##       #token失效换卡
##       remalloc_sim.remalloc_sim_process.func05token_exception.token_exception_main(log_path)
##       remalloc_sim.remalloc_sim_analyse.judgement_token_exception_result.token_exception_main(log_path)
##       #飞行模式换卡
##       remalloc_sim.remalloc_sim_process.func06fight_model_connect_data.fight_model_connect_data_main(log_path)
##       remalloc_sim.remalloc_sim_analyse.judgement_fight_model_connect_data_result.fight_model_connect_data_main(log_path)
##
####       remalloc_sim.remalloc_sim_process.func03Vsim_potocol_fail.Vsim_potocol_fail_main(log_path)
##       ##未知原因换卡
##       remalloc_sim.remalloc_sim_process.func07unknown.unknown_main(log_path)
##       remalloc_sim.remalloc_sim_analyse.judgement_unknown.judgement_unknown_main(log_path)
##       ##未开通服务换卡
##       remalloc_sim.remalloc_sim_process.func08no_subscription.no_subscription_main(log_path)
##       remalloc_sim.remalloc_sim_analyse.judgement_no_subscription.judgement_no_subscription_main(log_path)
##       

    
