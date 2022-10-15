from common.io.writeToa import readToa
from config.globalConfig import globalConfig
import numpy as np
import matplotlib.pyplot as plt


#for band in globalConfig.bands:
    # PASS FAIL CRITERIA

      # 1. check for all the bands that the difference is less than 0.01% for at least 3-sigma
    #compare if this is not right, check for 3-sigma --> TOA_isrf
    #BAND 0
toa_mine_isrf0 = readToa('/home/luss/my_shared_folder/ism_out/', 'ism_toa_isrf_VNIR-0.nc')  #my ouput toa
toa_her_isrf0 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-ISM/output/', 'ism_toa_isrf_VNIR-0.nc')
max_rel_dif_isrf0 = np.max(np.abs(toa_mine_isrf0-toa_her_isrf0))
print("Max rel diff", max_rel_dif_isrf0, "VNIR-0")

    #BAND 1
toa_mine_isrf1 = readToa('/home/luss/my_shared_folder/ism_out/', 'ism_toa_isrf_VNIR-1.nc')  #my ouput toa
toa_her_isrf1 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-ISM/output/', 'ism_toa_isrf_VNIR-1.nc')
max_rel_dif_isrf1 = np.max(np.abs(toa_mine_isrf1-toa_her_isrf1))
print("Max rel diff", max_rel_dif_isrf1, "VNIR-1")

    #BAND 2
toa_mine_isrf2 = readToa('/home/luss/my_shared_folder/ism_out/', 'ism_toa_isrf_VNIR-2.nc')  #my ouput toa
toa_her_isrf2 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-ISM/output/', 'ism_toa_isrf_VNIR-2.nc')
max_rel_dif_isrf2 = np.max(np.abs(toa_mine_isrf2-toa_her_isrf2))
print("Max rel diff", max_rel_dif_isrf1, "VNIR-2")

    #BAND 3
toa_mine_isrf3 = readToa('/home/luss/my_shared_folder/ism_out/', 'ism_toa_isrf_VNIR-3.nc')  #my ouput toa
toa_her_isrf3 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-ISM/output/', 'ism_toa_isrf_VNIR-3.nc')
max_rel_dif_isrf3 = np.max(np.abs(toa_mine_isrf3-toa_her_isrf3))
print("Max rel diff", max_rel_dif_isrf1, "VNIR-3")


    # 2. check for all the bands that the difference is less than 0.01% for at least 3-sigma
    #compare if this is not right, check for 3-sigma --> TOA_optical
    #BAND 0
toa_mine_opt0 = readToa('/home/luss/my_shared_folder/ism_out/', 'ism_toa_optical_VNIR-0.nc')  #my ouput toa
toa_her_opt0 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-ISM/output/', 'ism_toa_optical_VNIR-0.nc')
max_rel_dif_opt0 = np.max(np.abs(toa_mine_opt0-toa_her_opt0))
print("Max rel diff_opt", max_rel_dif_opt0, "VNIR-0")

    #BAND 1
toa_mine_opt1 = readToa('/home/luss/my_shared_folder/ism_out/', 'ism_toa_optical_VNIR-1.nc')  #my ouput toa
toa_her_opt1 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-ISM/output/', 'ism_toa_optical_VNIR-1.nc')
max_rel_dif_opt1 = np.max(np.abs(toa_mine_opt1-toa_her_opt1))
print("Max rel diff_opt", max_rel_dif_opt1, "VNIR-1")

    #BAND 2
toa_mine_opt2 = readToa('/home/luss/my_shared_folder/ism_out/', 'ism_toa_optical_VNIR-2.nc')  #my ouput toa
toa_her_opt2 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-ISM/output/', 'ism_toa_optical_VNIR-2.nc')
max_rel_dif_opt2 = np.max(np.abs(toa_mine_opt2-toa_her_opt2))
print("Max rel diff_opt", max_rel_dif_opt2, "VNIR-2")

    #BAND 3
toa_mine_opt3 = readToa('/home/luss/my_shared_folder/ism_out/', 'ism_toa_optical_VNIR-3.nc')  #my ouput toa
toa_her_opt3 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-ISM/output/', 'ism_toa_optical_VNIR-3.nc')
max_rel_dif_opt3 = np.max(np.abs(toa_mine_opt3-toa_her_opt3))
print("Max rel diff_opt", max_rel_dif_opt3, "VNIR-3")
