from common.io.writeToa import readToa
from common.io.writeToa import writeToa
from config.l1bConfig import l1bConfig
from config.globalConfig import globalConfig
from l1b.src.initL1b import initL1b
import numpy as np
import matplotlib.pyplot as plt

#BAND 0
#for band in globalConfig.bands:
toa_mine0 = readToa('/home/luss/my_shared_folder/l1b_out/', 'l1b_toa_VNIR-0.nc')  #your ouput toa
toa_her0 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-L1B/output/', 'l1b_toa_VNIR-0.nc')
max_rel_dif0 = np.max(np.abs(toa_mine0 - toa_her0))
print("Max rel dif", max_rel_dif0, "BAND VNIR-0")

#BAND 1
toa_mine1 = readToa('/home/luss/my_shared_folder/l1b_out/', 'l1b_toa_VNIR-1.nc')  #your ouput toa
toa_her1 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-L1B/output/', 'l1b_toa_VNIR-1.nc')
max_rel_dif1 = np.max(np.abs(toa_mine1 - toa_her1))
print("Max rel dif", max_rel_dif1, "BAND VNIR-1")


#BAND 2
toa_mine2 = readToa('/home/luss/my_shared_folder/l1b_out/', 'l1b_toa_VNIR-2.nc')  #your ouput toa
toa_her2 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-L1B/output/', 'l1b_toa_VNIR-2.nc')
max_rel_dif2 = np.max(np.abs(toa_mine2 - toa_her2))
print("Max rel dif", max_rel_dif2, "BAND VNIR-2")


#BAND 3
toa_mine3 = readToa('/home/luss/my_shared_folder/l1b_out/', 'l1b_toa_VNIR-3.nc')  #your ouput toa
toa_her3 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-L1B/output/', 'l1b_toa_VNIR-3.nc')
max_rel_dif3 = np.max(np.abs(toa_mine3 - toa_her3))
print("Max rel dif", max_rel_dif3, "BAND VNIR-3")

