from common.io.writeToa import readToa
from common.io.writeToa import writeToa
from config.l1bConfig import l1bConfig
from config.globalConfig import globalConfig
from l1b.src.initL1b import initL1b
import numpy as np
import matplotlib.pyplot as plt

def testL1B(band):
    for band in globalConfig.bands:
        toa_mine = readToa("/home/luss/my_shared_folder/l1b_out/", "l1b_toa_VNIR-0",".nc")  #your ouput toa
        toa_her = readToa("/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-L1B/output/", "lib_toa_VNIR-0", ".nc")
    # 1. check for all the bands that the difference is less than 0.01% for at least 3-sigma
    #compare if this is not right, check for 3-sigma
        max_rel_dif = np.max(np.abs(toa_mine - toa_her))
        print("Max rel dif", max_rel_dif, "band", band)
