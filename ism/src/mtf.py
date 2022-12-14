from math import pi

from numpy.matlib import repmat

from config.ismConfig import ismConfig
import numpy as np
from config.globalConfig import globalConfig
import math
from numpy import matlib as mb
import matplotlib.pyplot as plt
from scipy.special import j1
from common.io.readMat import writeMat
from common.plot.plotMat2D import plotMat2D
from scipy.interpolate import interp2d
from numpy.fft import fftshift, ifft2
import os

class mtf:
    """
    Class MTF. Collects the analytical modelling of the different contributions
    for the system MTF
    """
    def __init__(self, logger, outdir):
        self.ismConfig = ismConfig()
        self.logger = logger
        self.outdir = outdir

    def system_mtf(self, nlines, ncolumns, D, lambd, focal, pix_size,
                   kLF, wLF, kHF, wHF, defocus, ksmear, kmotion, directory, band):
        """
        System MTF
        :param nlines: Lines of the TOA
        :param ncolumns: Columns of the TOA
        :param D: Telescope diameter [m]
        :param lambd: central wavelength of the band [m]
        :param focal: focal length [m]
        :param pix_size: pixel size in meters [m]
        :param kLF: Empirical coefficient for the aberrations MTF for low-frequency wavefront errors [-]
        :param wLF: RMS of low-frequency wavefront errors [m]
        :param kHF: Empirical coefficient for the aberrations MTF for high-frequency wavefront errors [-]
        :param wHF: RMS of high-frequency wavefront errors [m]
        :param defocus: Defocus coefficient (defocus/(f/N)). 0-2 low defocusing
        :param ksmear: Amplitude of low-frequency component for the motion smear MTF in ALT [pixels]
        :param kmotion: Amplitude of high-frequency component for the motion smear MTF in ALT and ACT
        :param directory: output directory
        :return: mtf
        """

        self.logger.info("Calculation of the System MTF")

        # Calculate the 2D relative frequencies
        self.logger.debug("Calculation of 2D relative frequencies")
        fn2D, fr2D, fnAct, fnAlt = self.freq2d(nlines, ncolumns, D, lambd, focal, pix_size)

        # Diffraction MTF
        self.logger.debug("Calculation of the diffraction MTF")
        Hdiff = self.mtfDiffract(fr2D)

        # Defocus
        Hdefoc = self.mtfDefocus(fr2D, defocus, focal, D)

        # WFE Aberrations
        Hwfe = self.mtfWfeAberrations(fr2D, lambd, kLF, wLF, kHF, wHF)

        # Detector
        Hdet  = self. mtfDetector(fn2D)

        # Smearing MTF
        Hsmear = self.mtfSmearing(fnAlt, ncolumns, ksmear)

        # Motion blur MTF
        Hmotion = self.mtfMotion(fn2D, kmotion)

        # Calculate the System MTF
        self.logger.debug("Calculation of the Sysmtem MTF by multiplying the different contributors")
        Hsys = Hdiff*Hwfe*Hdefoc*Hdet*Hsmear*Hmotion

        # Plot cuts ACT/ALT of the MTF
        self.plotMtf(Hdiff, Hdefoc, Hwfe, Hdet, Hsmear, Hmotion, Hsys, nlines, ncolumns, fnAct, fnAlt, directory, band)
        return Hsys

    def freq2d(self,nlines, ncolumns, D, lambd, focal, w):
        """
        Calculate the relative frequencies 2D (for the diffraction MTF)
        :param nlines: Lines of the TOA
        :param ncolumns: Columns of the TOA
        :param D: Telescope diameter [m]
        :param lambd: central wavelength of the band [m]
        :param focal: focal length [m]
        :param w: pixel size in meters [m]
        :return fn2D: normalised frequencies 2D (f/(1/w))
        :return fr2D: relative frequencies 2D (f/(1/fc))
        :return fnAct: 1D normalised frequencies 2D ACT (f/(1/w))
        :return fnAlt: 1D normalised frequencies 2D ALT (f/(1/w))
        """
        #frequence step along and across track
        eps=1e-6
        fstepAlt=1/nlines/w
        fstepAct=1/ncolumns/w

        #calculation of the one dimensional freq vector,
        #These are the spatial frequencies
        fAlt= np.arange(-1/(2*w),1/(2*w)-eps,fstepAlt)
        fAct= np.arange(-1/(2*w),1/(2*w)-eps,fstepAct)

        #normalized frequencies
        fnAlt= fAlt/(1/w)
        fnAct= fAct/(1/w)

        #CUt off freq and relative freq
        cutoff= D/(lambd*focal)
        frAlt=fAlt/cutoff
        frAct= fAct/cutoff

        [fnAltxx,fnActxx]= np.meshgrid(fnAlt,fnAct,indexing='ij')
        fn2D= np.sqrt(fnAltxx*fnAltxx + fnActxx*fnActxx)
        fr2D= fn2D*(1/w)/cutoff

        writeMat(self.outdir, "fn2D", fn2D)
        writeMat(self.outdir, "fr2D", fr2D)

        return fn2D, fr2D, fnAct, fnAlt

    def mtfDiffract(self,fr2D):
        """
        Optics Diffraction MTF
        :param fr2D: 2D relative frequencies (f/fc), where fc is the optics cut-off frequency
        :return: diffraction MTF
        """
        Hdiff= 2/np.pi*(np.arccos(fr2D) - fr2D* np.sqrt(1-fr2D*fr2D))
        return Hdiff


    def mtfDefocus(self, fr2D, defocus, focal, D):
        """
        Defocus MTF
        :param fr2D: 2D relative frequencies (f/fc), where fc is the optics cut-off frequency
        :param defocus: Defocus coefficient (defocus/(f/N)). 0-2 low defocusing
        :param focal: focal length [m]
        :param D: Telescope diameter [m]
        :return: Defocus MTF
        """
        #TODO
        x= np.pi *defocus*fr2D*(1-fr2D)
        Hdefoc = (2*j1(x))/x
        return Hdefoc

    def mtfWfeAberrations(self, fr2D, lambd, kLF, wLF, kHF, wHF):
        """
        Wavefront Error Aberrations MTF
        :param fr2D: 2D relative frequencies (f/fc), where fc is the optics cut-off frequency
        :param lambd: central wavelength of the band [m]
        :param kLF: Empirical coefficient for the aberrations MTF for low-frequency wavefront errors [-]
        :param wLF: RMS of low-frequency wavefront errors [m]
        :param kHF: Empirical coefficient for the aberrations MTF for high-frequency wavefront errors [-]
        :param wHF: RMS of high-frequency wavefront errors [m]
        :return: WFE Aberrations MTF
        """
        Hwfe = np.exp(-fr2D*(1-fr2D)*(kLF*(wLF/lambd)*(wLF/lambd)+kHF*(wHF/lambd)*(wHF/lambd)))
        return Hwfe

    def mtfDetector(self,fn2D):
        """
        Detector MTF
        :param fnD: 2D normalised frequencies (f/(1/w))), where w is the pixel width
        :return: detector MTF
        """
        Hdet=np.abs(np.sin(np.pi*fn2D)/(np.pi*fn2D))
        return Hdet

    def mtfSmearing(self, fnAlt, ncolumns, ksmear):
        """
        Smearing MTF
        :param ncolumns: Size of the image ACT
        :param fnAlt: 1D normalised frequencies 2D ALT (f/(1/w))
        :param ksmear: Amplitude of low-frequency component for the motion smear MTF in ALT [pixels]
        :return: Smearing MTF
        """
        # Smearing is an ALT effect. Calculate the 1D MTF In the ALT direction
        #using fn2D, size nlines and repeat in the ACT direction with a repmat
        # ME SALE DISTINTO EL OCTAVO DECIMAL
        MTFs = np.sinc(ksmear*fnAlt)
        Hsmear = np.transpose(mb.repmat(MTFs,ncolumns,1))
        return Hsmear

    def mtfMotion(self, fn2D, kmotion):
        """
        Motion blur MTF
        :param fnD: 2D normalised frequencies (f/(1/w))), where w is the pixel width
        :param kmotion: Amplitude of high-frequency component for the motion smear MTF in ALT and ACT
        :return: detector MTF
        """
        #remember to use fn2D (normalised frequencies)
        Hmotion = np.sinc(kmotion*fn2D)
        return Hmotion


    def plotMtf(self,Hdiff, Hdefoc, Hwfe, Hdet, Hsmear, Hmotion, Hsys, nlines, ncolumns, fnAct, fnAlt, directory, band):
        """"
        Plotting the system MTF and all of its contributors
        :param Hdiff: Diffraction MTF
        :param Hdefoc: Defocusing MTF
        :param Hwfe: Wavefront electronics MTF
        :param Hdet: Detector MTF
        :param Hsmear: Smearing MTF
        :param Hmotion: Motion blur MTF
        :param Hsys: System MTF
        :param nlines: Number of lines in the TOA
        :param ncolumns: Number of columns in the TOA
        :param fnAct: normalised frequencies in the ACT direction (f/(1/w))
        :param fnAlt: normalised frequencies in the ALT direction (f/(1/w))
        :param directory: output directory
        :param band: band
        :return: N/A
        """
        halfAct = int(np.floor(fnAct.shape[0]/2))
        halfAlt = int(np.floor(fnAlt.shape[0]/2))

        fig,ax = plt.subplots()
        ax.plot(fnAct[halfAct:], Hdiff[halfAlt,halfAct:], label='Diffraction', linewidth=1.0)
        ax.plot(fnAct[halfAct:], Hdefoc[halfAlt,halfAct:], label='Defocusing', linewidth=1.0)
        ax.plot(fnAct[halfAct:], Hwfe[halfAlt,halfAct:], label='Wavefront electronics', linewidth=1.0)
        ax.plot(fnAct[halfAct:], Hdet[halfAlt,halfAct:], label='Detector', linewidth=1.0)
        ax.plot(fnAct[halfAct:], Hsmear[halfAlt,halfAct:], label='Smearing', linewidth=1.0)
        ax.plot(fnAct[halfAct:], Hmotion[halfAlt,halfAct:], label='Motion Blur', linewidth=1.0)
        ax.plot(fnAct[halfAct:], Hsys[halfAlt,halfAct:], 'k-', label='System', linewidth=1.0)
        auxv=np.arange(0,1.1,0.1)
        plt.plot(0.5*np.ones(auxv.shape),auxv,'--k',linewidth=1, label ='f Nyquist')
        plt.legend(loc='lower left')
        plt.title('System MTF slice ACT for '+band)
        plt.xlabel('Spatial Frequencies f/(1/w) [-]')
        plt.ylabel('MTF')
        plt.savefig(self.outdir + '/act_mtf'+band+'.eps')

        fig2, ax2 = plt.subplots()
        ax2.plot(fnAlt[halfAlt:], Hdiff[halfAlt:,halfAct], label='Diffraction', linewidth=1.0)
        ax2.plot(fnAlt[halfAlt:], Hdefoc[halfAlt:,halfAct], label='Defocusing', linewidth=1.0)
        ax2.plot(fnAlt[halfAlt:], Hwfe[halfAlt:,halfAct], label='Wavefront electronics', linewidth=1.0)
        ax2.plot(fnAlt[halfAlt:], Hdet[halfAlt:,halfAct], label='Detector', linewidth=1.0)
        ax2.plot(fnAlt[halfAlt:], Hsmear[halfAlt:,halfAct], label='Smearing', linewidth=1.0)
        ax2.plot(fnAlt[halfAlt:], Hmotion[halfAlt:,halfAct], label='Motion', linewidth=1.0)
        ax2.plot(fnAlt[halfAlt:], Hsys[halfAlt:,halfAct], 'k-', label='System', linewidth=1.0)
        auxv=np.arange(0,1.1,0.1)
        plt.plot(0.5*np.ones(auxv.shape),auxv,'--k',linewidth=1, label ='f Nyquist')
        plt.legend(loc='lower left')
        plt.title('System MTF slice ALT for '+band)
        plt.xlabel('Spatial Frequencies f/(1/w) [-]')
        plt.ylabel('MTF')
        plt.savefig(self.outdir + '/alt_mtf'+band+'.eps')
