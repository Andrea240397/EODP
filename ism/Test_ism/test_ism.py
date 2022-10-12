from common.io.writeToa import readToa
from config.globalConfig import globalConfig
import numpy as np
import matplotlib.pyplot as plt


for band in globalConfig.bands:
    # PASS FAIL CRITERIA

      # 1. check for all the bands that the difference is less than 0.01% for at least 3-sigma
    #compare if this is not right, check for 3-sigma --> TOA_isrf
    toa_mine_isrf = readToa("/home/luss/my_shared_folder/ism_out', ism_toa_isrf_VNIR-0",".nc")  #my ouput toa
    toa_her_isrf = readToa("/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-ISM/output/', ism_toa_isrf_VNIR-0", ".nc")
    max_rel_dif_isrf = np.max(np.abs(toa_mine_isrf-toa_her_isrf))
    print("Max rel diff", max_rel_dif_isrf, "band", band)

    # 2. check for all the bands that the difference is less than 0.01% for at least 3-sigma
            #compare if this is not right, check for 3-sigma --> TOA_optical
    toa_mine_opt = readToa("/home/luss/my_shared_folder/ism_out', ism_toa_optical_VNIR-0",".nc")  #my ouput toa
    toa_her_opt = readToa("/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-ISM/output/', ism_toa_optical_VNIR-0", ".nc")
    max_rel_dif_opt = np.max(np.abs(toa_mine_opt-toa_her_opt))
    print("Max rel diff_opt", max_rel_dif_opt, "band", band)
