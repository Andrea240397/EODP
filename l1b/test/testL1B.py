from common.io.writeToa import readToa
from common.io.writeToa import writeToa
from config.l1bConfig import l1bConfig
from config.globalConfig import globalConfig
from l1b.src.initL1b import initL1b
import numpy as np
import matplotlib.pyplot as plt

def testL1B(band):
    for band in globalConfig.bands:
        toa_mine = readToa("/home/luss/my_shared_folder/l1b_out', l1b_toa_VNIR-0",".nc")  #your ouput toa
        toa_her = readToa("/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-L1B/output/", "lib_toa_VNIR-0", ".nc")
    # 1. check for all the bands that the difference is less than 0.01% for at least 3-sigma
    #compare if this is not right, check for 3-sigma
        max_rel_dif = np.max(np.abs(toa_mine-toa_her))
        print("Max rel diff", max_rel_dif, "band", band)

"""
# 2. For the central ALT position, plot the restored signal (l1b_toa), and the TOA after the ISRF
    #plots
        fig_TOA_rest = plt.figure(figsize=(20,10))
        plt.plot(toa_l1b,Label='l1b_toa_ALT')
        plt.plot(ism_toa_isrf,Label='l1b_TOA_isrf')
        plt.title('TOA before and after the ISRF for ' +band,fontsize=20)
    plt.xlabel('ACT [-]', fontsize=16)
    plt.ylabel('Restored TOA [mW/m2s]', fontsize=16)
    plt.grid()
    plt.legend()
    saveas_str='TOA_L1b_rest'+ band
    savestr = '/home/luss/my_shared_folder/l1b_out/TOA_L1b_rest'
    plt.savefig(savestr)
    plt.close(fig_TOA_rest)
    print("Saved image " + savestr)

    # 3. WITHOUT EQUALIZATOR, turn off the equalizator in l1bConfig.py
    #also change the outdir in main not to overwrite
    #Plot the restored signal without equalizator
    """
""""
    fig_TOA_no_EQ = plt.figure(figsize=(20,10))
    plt.plot([0:100],toa_l1b,Label='l1b_toa_ALT')
    plt.plot([0:100],ism_toa_isrf,Label='l1b_toa_ALT')
    plt.title('TOA without Equalizator before and after the ISRF for ' +band,fontsize=20)
    plt.xlabel('ACT [-]', fontsize=16)
    plt.ylabel('TOA without EQ [mW/m2s]', fontsize=16)
    plt.grid()
    plt.legend()
    saveas_str='TOA_L1b_no_EQ'+ band
    savestr = '/home/luss/my_shared_folder/l1b_out/TOA_L1b_no_EQ'
    plt.savefig(savestr)
    plt.close(fig_TOA_no_EQ)
    print("Saved image " + savestr)
"""
