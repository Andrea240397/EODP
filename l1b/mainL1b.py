
# MAIN FUNCTION TO CALL THE L1B MODULE

from l1b.src.l1b import l1b
from config.globalConfig import globalConfig
from l1b.test.testL1B import testL1B

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = '/home/luss/EODP/EODP/auxiliary'
indir = '/home/luss/my_shared_folder/EODP_TER_2021/EODP-TS-L1B/input'
outdir = '/home/luss/my_shared_folder/l1b_out'

# Initialise the ISM
myL1b = l1b(auxdir, indir, outdir)
myL1b.processModule()
