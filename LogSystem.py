import os.path
import time
import remalloc_sim.remalloc_sim_main
import unremalloc_sim.unremalloc_sim_main


def log_system_main(log_path):
    #分析自动换卡
    remalloc_sim.remalloc_sim_main.remalloc_main(log_path)
    #分析不自动换卡
    unremalloc_sim.unremalloc_sim_main.unremalloc_main(log_path)

