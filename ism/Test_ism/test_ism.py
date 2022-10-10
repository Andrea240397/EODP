from common.io.writeToa import readToa
from config.globalConfig import globalConfig
import numpy as np
import matplotlib.pyplot as plt


for band in globalConfig.bands:
    # PASS FAIL CRITERIA

      # 1. check for all the bands that the difference is less than 0.01% for at least 3-sigma
    #compare if this is not right, check for 3-sigma --> TOA_isrf
    toa_mine_isrf = readToa("/home/luss/my_shared_folder/ism_out', ism_toa_isrf_VNIR-0",".nc")  #my ouput toa
    toa_her_isrf = readToa("/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-ISM/input/gradient_alt100_act150/", "ism_toa_isrf_VNIR-0", ".nc")
    max_rel_dif_isrf = np.max(np.abs(toa_mine_isrf-toa_her_isrf))
    print("Max rel diff", max_rel_dif_isrf, "band", band)

# 2. check for all the bands that the difference is less than 0.01% for at least 3-sigma
    #compare if this is not right, check for 3-sigma --> TOA_optical
    toa_mine_opt = readToa("/home/luss/my_shared_folder/ism_out', ism_toa_optical_VNIR-0",".nc")  #my ouput toa
    toa_her_opt = readToa("/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-ISM/input/gradient_alt100_act150/", "ism_toa_optical_VNIR-0", ".nc")
    max_rel_dif_opt = np.max(np.abs(toa_mine_opt-toa_her_opt))
    print("Max rel diff_opt", max_rel_dif, "band", band)

    # 3 Plot TOA after the MTF to see the border effect
    fig = plt. figure(figsize=(20,10))
    # QUÉ TOA REPRESENTO????
    #plt.plot(-fnAlt,toa,'k',linewidth=3,Label='System MTF_ALT')
    auxv = np.arange(0,1.1,0.1)
    plt.plot(0.5*np.ones(auxv.shape),auxv,'--k',Linewidth=3,label='fNyquist')
    plt.title('System MTF for '+band, fontsize=20)
    plt.xlabel('Spatial frequencies f/(1/w) [-]', fontsize=16)
    plt.ylabel('System MTF', fontsize=16)
    plt.grid()
    plt.legend()
    saveas_str='system_MTF'+band
    savestr = '/home/luss/my_shared_folder/ism_out/system_MTF
    plt.savefig(savestr)
    plt.close(fig)
    print("Saved image " + savestr)


# 4. Plot the System MTF across and along track (for central pixels)
#Report the MTF at the nyquist freq.
    fig = plt. figure(figsize=(20,10))
    plt.plot(-fnAlt,Hsys,'k',linewidth=3,Label='System MTF_ALT')
    plt.plot(-fnAct,Hsys,'k',linewidth=3,Label='System MTF_ACT')
    auxv = np.arange(0,1.1,0.1)
    plt.plot(0.5*np.ones(auxv.shape),auxv,'--k',Linewidth=3,label='fNyquist')
    plt.title('System MTF for '+band, fontsize=20)
    plt.xlabel('Spatial frequencies f/(1/w) [-]', fontsize=16)
    plt.ylabel('System MTF', fontsize=16)
    plt.grid()
    plt.legend()
    saveas_str='system_MTF'+band
    savestr = '/home/luss/my_shared_folder/ism_out/system_MTF
    plt.savefig(savestr)
    plt.close(fig)
    print("Saved image " + savestr)


    # 5
