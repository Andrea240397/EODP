from common.io.writeToa import readToa
from common.io.writeToa import writeToa
from config.l1bConfig import l1bConfig
from config.globalConfig import globalConfig
from l1b.src.initL1b import initL1b
import numpy as np
import matplotlib.pyplot as plt

# BAND 0
toa_mine0 = readToa('/home/luss/my_shared_folder/l1c_out/', 'l1c_toa_VNIR-0.nc')  #your ouput toa
toa_her0 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-L1C/output/', 'l1c_toa_VNIR-0.nc')
toa_mine0_sorted= np.sort(toa_mine0)
toa_her0_sorted= np.sort(toa_her0)
max_rel_dif0 = np.max(np.abs(toa_mine0_sorted - toa_her0_sorted))
print("Max rel dif", max_rel_dif0, "BAND VNIR-0")

# BAND 1
toa_mine1 = readToa('/home/luss/my_shared_folder/l1c_out/', 'l1c_toa_VNIR-1.nc')  #your ouput toa
toa_her1 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-L1C/output/', 'l1c_toa_VNIR-1.nc')
toa_mine1_sorted= np.sort(toa_mine1)
toa_her1_sorted= np.sort(toa_her1)
max_rel_dif1 = np.max(np.abs(toa_mine1_sorted - toa_her1_sorted))
print("Max rel dif", max_rel_dif1, "BAND VNIR-1")

#BAND 2
toa_mine2 = readToa('/home/luss/my_shared_folder/l1c_out/', 'l1c_toa_VNIR-2.nc')  #your ouput toa
toa_her2 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-L1C/output/', 'l1c_toa_VNIR-2.nc')
toa_mine2_sorted= np.sort(toa_mine2)
toa_her2_sorted= np.sort(toa_her2)
max_rel_dif2 = np.max(np.abs(toa_mine2_sorted - toa_her2_sorted))
print("Max rel dif", max_rel_dif2, "BAND VNIR-2")

# BAND 3
toa_mine3 = readToa('/home/luss/my_shared_folder/l1c_out/', 'l1c_toa_VNIR-3.nc')  #your ouput toa
toa_her3 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-L1C/output/', 'l1c_toa_VNIR-3.nc')
toa_mine3_sorted= np.sort(toa_mine3)
toa_her3_sorted= np.sort(toa_her3)
max_rel_dif3 = np.max(np.abs(toa_mine3_sorted - toa_her3_sorted))
print("Max rel dif", max_rel_dif3, "BAND VNIR-3")
