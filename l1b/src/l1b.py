
# LEVEL-1B MODULE

from l1b.src.initL1b import initL1b
from common.io.writeToa import writeToa, readToa
from common.src.auxFunc import getIndexBand
from common.io.readFactor import readFactor, EQ_MULT, EQ_ADD, NC_EXT
from config.globalConfig import globalConfig
import numpy as np
import os
import matplotlib.pyplot as plt

class l1b(initL1b):

    def __init__(self, auxdir, indir, outdir):
        super().__init__(auxdir, indir, outdir)

    def processModule(self):

        self.logger.info("Start of the L1B Processing Module")

        for band in self.globalConfig.bands:

            self.logger.info("Start of BAND " + band)

            # Read TOA - output of the ISM in Digital Numbers
            # -------------------------------------------------------------------------------
            toa = readToa(self.indir, self.globalConfig.ism_toa + band + '.nc')

            # Equalization (radiometric correction)
            # -------------------------------------------------------------------------------
            if self.l1bConfig.do_equalization:
                self.logger.info("EODP-ALG-L1B-1010: Radiometric Correction (equalization)")

                # Read the multiplicative and additive factors from auxiliary/equalization/
                eq_mult = readFactor(os.path.join(self.auxdir,self.l1bConfig.eq_mult+band+NC_EXT),EQ_MULT)
                eq_add = readFactor(os.path.join(self.auxdir,self.l1bConfig.eq_add+band+NC_EXT),EQ_ADD)

                # Do the equalization and save to file
                toa = self.equalization(toa, eq_add, eq_mult)
                writeToa(self.outdir, self.globalConfig.l1b_toa_eq + band, toa)

            # Restitution (absolute radiometric gain)
            # -------------------------------------------------------------------------------
            self.logger.info("EODP-ALG-L1B-1020: Absolute radiometric gain application (restoration)")
            toa = self.restoration(toa, self.l1bConfig.gain[getIndexBand(band)])

            # Write output TOA
            # -------------------------------------------------------------------------------
            writeToa(self.outdir, self.globalConfig.l1b_toa + band, toa)
            self.plotL1bToa(toa, self.outdir, band)

            self.logger.info("End of BAND " + band)

        self.logger.info("End of the L1B Module!")


    def equalization(self, toa, eq_add, eq_mult):
        """
        Equlization. Apply an offset and a gain.
        :param toa: TOA in DN
        :param eq_add: Offset in DN
        :param eq_mult: Gain factor, adimensional
        :return: TOA in DN, equalized
        """
        #We have to do it along track
        #[0] gives the numer of rows
        #[1] gives the number of columns
        #Python iterates from 0 to -1
        #python uses brackets, not parenthesis

        #this creates an empty matrix with the size of toa
        toa_out = np.zeros(toa.shape)  # initialization

        for ialt in range(toa.shape[0]):
            toa_out[ialt,:] = (toa[ialt,:] - eq_add) / eq_mult
        return toa_out


    def restoration(self,toa,gain):
        """
        Absolute Radiometric Gain - restore back to radiances
        :param toa: TOA in DN
        :param gain: gain in [rad/DN]
        :return: TOA in radiances [mW/sr/m2]
        """
        toa_out2=np.zeros(toa.shape)
        toa_out2= toa*gain
        self.logger.debug('Sanity check. TOA in radiances after gain application ' + str(toa[1,-1]) + ' [mW/m2/sr]')
        return toa_out2

    def plotL1bToa(self, l1b_toa, outputdir, band):
        #for band in globalConfig.bands:
        x=1
        fig_L1b_toa = plt.figure(figsize=(20,10))
            #EJE X??
        plt.plot(l1b_toa,label='TOA out')
        plt.title('TOA L1B for '+band, fontsize=20)
        plt.xlabel('ACT Pixel [-]', fontsize=16)
        plt.ylabel('TOA [mW/m2s]', fontsize=16)
        plt.grid()
        plt.legend()
        saveas_str='TOA_L1b'+band
        savestr = '/home/luss/my_shared_folder/l1b_out/TOA_L1b'
        plt.savefig(savestr)
        plt.close(fig_L1b_toa)
        print("Saved image " + savestr)
