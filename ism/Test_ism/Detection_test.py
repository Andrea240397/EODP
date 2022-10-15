from common.io.writeToa import readToa
from config.globalConfig import globalConfig
from config.ismConfig import ismConfig
import numpy as np
from ism.src.initIsm import initIsm
import matplotlib.pyplot as plt
from auxiliary.constants import constants

toa_mine0 = readToa('/home/luss/my_shared_folder/ism_out/', 'ism_toa_VNIR-0.nc')  #my ouput toa
toa_her0 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-ISM/output/', 'ism_toa_VNIR-0.nc')
max_rel_dif0 = abs(toa_mine0-toa_her0)
print("Max rel diff", max_rel_dif0, "VNIR-0")


#1. Check for all the bands that the difference in the ism_toa_ is less than 0.01
toa_mine0 = readToa('/home/luss/my_shared_folder/ism_out/', 'ism_toa_VNIR-0.nc')  #my ouput toa
toa_her0 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-ISM/output/', 'ism_toa_VNIR-0.nc')
max_rel_dif0 = abs(toa_mine0-toa_her0)
print("Max rel diff", max_rel_dif0, "VNIR-0")

    #BAND 1
toa_mine1 = readToa('/home/luss/my_shared_folder/ism_out/', 'ism_toa_VNIR-1.nc')  #my ouput toa
toa_her1 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-ISM/output/', 'ism_toa_VNIR-1.nc')
max_rel_dif1 = np.max(np.abs(toa_mine1-toa_her1))
print("Max rel diff", max_rel_dif1, "VNIR-1")

    #BAND 2
toa_mine2 = readToa('/home/luss/my_shared_folder/ism_out/', 'ism_toa_VNIR-2.nc')  #my ouput toa
toa_her2 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-ISM/output/', 'ism_toa_VNIR-2.nc')
max_rel_dif2 = np.max(np.abs(toa_mine2-toa_her2))
print("Max rel diff", max_rel_dif1, "VNIR-2")

    #BAND 3
toa_mine3 = readToa('/home/luss/my_shared_folder/ism_out/', 'ism_toa_VNIR-3.nc')  #my ouput toa
toa_her3 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-ISM/output/', 'ism_toa_VNIR-3.nc')
max_rel_dif3 = np.max(np.abs(toa_mine3-toa_her3))
print("Max rel diff", max_rel_dif1, "VNIR-3")


# Irradiance to photons
irrad_ph_factor = (ismConfig.area_pix * tint)/ (self.constants.h_planck*self.constants.speed_light/wv)
print(irrad_ph_factor)


# Photons to electrons
print("The conversion factor from photons to e- is the QE = ", ismConfig.QE)

# Electrons to volts
print("The conversion factor from e- to V is ", ismConfig.OCF*ismConfig.ADC_gain)

# Volts to digital numbers
print("The conversion factor from V to DN is ", (2**ismConfig.bit_depth-1)/(ismConfig.max_voltage-ismConfig.min_voltage))
