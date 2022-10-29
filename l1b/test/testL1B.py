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



# Plot TOA with and without equalization
l1b_toa_eq = readToa('/home/luss/my_shared_folder/l1b_out/', 'l1b_toa_VNIR-0.nc')
l1b_toa_wo_eq = readToa('/home/luss/my_shared_folder/l1b_out/Without_eq/', 'l1b_toa_VNIR-0.nc')
outdir = '/home/luss/my_shared_folder/l1b_out/'

mid_value=int(l1b_toa_eq.shape[0]/2)
mid_value2 = int(l1b_toa_wo_eq.shape[0]/2)
fig,ax= plt.subplots()
ax.plot(l1b_toa_eq[mid_value,:],'r',Label='TOA with Equalization')
ax.plot(l1b_toa_wo_eq[mid_value2,:], 'b',Label='TOA without Equalization')
plt.title('TOA L1B - for VNIR-0')
plt.xlabel('ACT Pixel [-]')
plt.ylabel('TOA [mW/m2/sr]')
plt.grid()
plt.legend()
plt.show()
fig.savefig(outdir+'Comparison_VNIR-0_graph.png')


# Plot the  restored signal l1b_toa and the toa after the isrf for the central ALT Position
l1b_toa_rest = readToa('/home/luss/my_shared_folder/l1b_out/', 'l1b_toa_VNIR-3.nc')
l1b_toa_isrf = readToa('/home/luss/my_shared_folder/ism_out/', 'ism_toa_isrf_VNIR-3.nc')
outdir = '/home/luss/my_shared_folder/l1b_out/'
mid_value3= int(l1b_toa_rest.shape[0]/2)
mid_value4 = int(l1b_toa_isrf.shape[0]/2)
fig,ax2=plt.subplots()
ax2.plot(l1b_toa_rest[mid_value3,:],'r',Label='TOA restored')
ax2.plot(l1b_toa_isrf[mid_value4,:],'b',Label='TOA after isrf')
plt.title('TOA restored and after ISRF for VNIR-3')
plt.xlabel('ALT PIxel [-]')
plt.ylabel('TOA [mW/m2/sr]')
plt.grid()
plt.legend()
plt.show()
fig.savefig(outdir+'Comparison_rest_isrf_VNIR-3.png')


# For the geometry module, compared L1B_TOA and TOA_ISRF
l1b_toa_rest_geo = readToa('/home/luss/my_shared_folder/l1b_out/l1b_out_geo/', 'l1b_toa_VNIR-0.nc')
l1b_toa_isrf_geo = readToa('/home/luss/my_shared_folder/ism_out/ism_out_geo/', 'ism_toa_isrf_VNIR-0.nc')
outdir = '/home/luss/my_shared_folder/l1b_out/l1b_out_geo/'
mid_value5= int(l1b_toa_rest_geo.shape[1]/2)
mid_value6 = int(l1b_toa_isrf_geo.shape[1]/2)
fig,ax3=plt.subplots()
ax3.plot(l1b_toa_rest_geo[mid_value5,:],'r',Label='L1B TOA')
ax3.plot(l1b_toa_isrf_geo[mid_value6,:],'b',Label='ISRF TOA')
plt.title('TOA restored and TOA ISRF for VNIR-0')
plt.xlabel('ACT PIxel [-]')
plt.ylabel('TOA [mW/m2/sr]')
plt.grid()
plt.legend()
plt.show()
fig.savefig(outdir+'Comparison_rest_isrf_GEO_VNIR-0.png')
