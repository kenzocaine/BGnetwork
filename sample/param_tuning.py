#Network cparameters Lindahl 2016
import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import numpy as np
import copy
import matplotlib.pyplot as plt
import sample.tls as tls
from param import state
from param import cparamOLD


#Number of neurons
def tune():
    cparam = copy.deepcopy(cparamOLD) # New dictionary to store updated cparameters

    NSTR = ['P_D1','P_D2', 'P_FSN']
    N = ['C_D1_D1', 'C_D1_D2','C_D2_D1', 'C_D2_D2', 'C_FSN_D1','C_FSN_D2','C_FSN_FSN','C_D1_GPI','C_D2_GPTI']


    for n in cparamOLD:
        if n in N:
            m = 5000
            connectP = cparamOLD[n]/cparamOLD["P_"+n.split("_")[1]]
           

            N_Cnew = connectP * m

            var = cparamOLD[n] * cparamOLD['lMSN'] * cparamOLD['g'+n[2:]]**2 *cparamOLD['tau'+n[2:]] * np.exp(2) / 4

            mean = cparamOLD[n] * cparamOLD['lMSN'] * cparamOLD['g'+n[2:]] *cparamOLD['tau'+n[2:]] * np.exp(1)

            gNEW = mean / (N_Cnew * cparamOLD['lMSN'] * cparamOLD['tau'+n[2:]] * np.exp(1))

            cparam['g'+n[2:]] = gNEW
            cparam[n] = np.round(N_Cnew)



    



    cparam['P_D1'] = 5000
    cparam['P_D2'] = 5000
    cparam['P_FSN'] = cparamOLD['P_FSN']/cparamOLD['P_D1'] *cparam['P_D1']
    for i in cparamOLD:
        if i[0:4] not in ['P_D1','P_D2','P_FS','gD1_','gD2_','gFSN','tauD','tauF']:
            cparam[i] = cparamOLD[i] * 2 # double the amount of connection and pop for neurons not in str

    # total population
    cparam['P_n'] =  cparam['P_STN'] + cparam['P_GPTA'] + cparam['P_GPTI'] + cparam['P_GPI'] + cparam['P_FSN'] + cparam['P_D1'] + cparam['P_D2']

    tls.param2file(cparam)
    print('Done')

if __name__ == '__main__':
    tune()
