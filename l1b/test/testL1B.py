from common.io.writeToa import readToa
from config.globalConfig import globalConfig
import numpy as np
import matplotlib.pyplot as plt

for band in globalConfig.bands:
    # PASS FAIL CRITERIA
    toa_mine = readToa(directory, filename)  #your ouput toa
    toa_her = readToa("/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-L1B/output/", "lib_toa_VNIR-0", ".nc")
    # 1. check for all the bands that the difference is less than 0.01% for at least 3-sigma
    #compare if this is not right, check for 3-sigma
    max_rel_dif = np.max(np.abs(mine-her))
    print("Max rel diff", max_rel_dif, "band", band)

    # 2. For the central ALT position, plot the restored signal (l1b_toa), and the TOA after the ISRF
    #plots
    fig = plt. figure(figsize=(20,10))
    plt.plot(-fnAlt[0:mAlt],abs(Hdiff[0:mAlt,mAct]),Label='DiffractionMTF')
    auxv = np.arange(0,1.1,0.1)
    plt.plot(0.5*np.ones(auxv.shape),auxv,'--k',Linewidth=3,label='fNyquist')
    plt.title('System MTF slice ALT for

    # 3. WITHOUT EQUALIZATOR, turn off the equalizator in l1bConfig.py
    #also change the outdir in main not to overwrite


