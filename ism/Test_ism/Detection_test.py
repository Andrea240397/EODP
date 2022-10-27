from common.io.writeToa import readToa
from config.globalConfig import globalConfig
from config.ismConfig import ismConfig
import numpy as np
from ism.src.initIsm import initIsm
import matplotlib.pyplot as plt
from auxiliary.constants import constants


#1. Check for all the bands that the difference in the ism_toa_ is less than 0.01
# BAND 0
toa_mine0 = readToa('/home/luss/my_shared_folder/ism_out/', 'ism_toa_VNIR-0.nc')  #my ouput toa
toa_her0 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-ISM/output/', 'ism_toa_VNIR-0.nc')
max_rel_dif0 = np.max(np.abs(toa_mine0-toa_her0))
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
print("Max rel diff", max_rel_dif2, "VNIR-2")

    #BAND 3
toa_mine3 = readToa('/home/luss/my_shared_folder/ism_out/', 'ism_toa_VNIR-3.nc')  #my ouput toa
toa_her3 = readToa('/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-ISM/output/', 'ism_toa_VNIR-3.nc')
max_rel_dif3 = np.max(np.abs(toa_mine3-toa_her3))
#max_rel_dif3 = toa_mine3-toa_her3
print("Max rel diff", max_rel_dif3, "VNIR-3")



pix_size = 30e-6
t_int = 0.00672
area_pix = pix_size*pix_size
wv = np.array([0.49,0.665,0.865,0.945])*1e-6
QE=0.8
ADC_gain = 0.56                     # [-]
OCF = 5.4e-6                        # [V/e-] Output conversion factor
bit_depth = 12                      # [-]
min_voltage = 0.0                   # [V]
max_voltage = 0.86
speed_light = 299792458  # [m/s]
h_planck = 6.62607004e-34  # [m2 kg / s]

# Irradiance to photons
irrad_ph_factor0 = (area_pix * t_int)/ (h_planck*speed_light/wv[0])
print("The conversion factor from irradiance to photons for VNIR-0 is ", irrad_ph_factor0)
irrad_ph_factor1 = (area_pix * t_int)/ (h_planck*speed_light/wv[1])
print("The conversion factor from irradiance to photons for VNIR-1 is ", irrad_ph_factor1)
irrad_ph_factor2 = (area_pix * t_int)/ (h_planck*speed_light/wv[2])
print("The conversion factor from irradiance to photons for VNIR-2 is ", irrad_ph_factor2)
irrad_ph_factor3 = (area_pix * t_int)/ (h_planck*speed_light/wv[3])
print("The conversion factor from irradiance to photons for VNIR-3 is ", irrad_ph_factor3)

# Photons to electrons
print("The conversion factor from photons to e- is the QE = ", QE)

# Electrons to volts
print("The conversion factor from e- to V is ", OCF*ADC_gain)

# Volts to digital numbers
print("The conversion factor from V to DN is ", (2**bit_depth-1)/(max_voltage-min_voltage))
