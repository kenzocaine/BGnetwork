import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import sample.tls
from sample.BGnodes import BGnodes 
from sample.param import nparam
import nest
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import pickle



I_e = np.arange(0,500,10)
F ={ "GPTA" : [], "GPTI" : [], "STN" : [], "GPI" : [], "D1" : [], "D2": [], "FSN" : []}

for i_e in I_e:
	NW = BGnodes(nparam) # create the single neuron network with spike count
	NW.setIe(i_e) # Set the desired I_e
	NW.connectSpikeDet()
	NW.simulate(1000.0) # Simulate the network
	NW.countSpikes()
	freq = NW.freq
	nest.ResetKernel()
	for i in freq:
		F[i] = F[i] + [freq[i]] # Put the count in a list for each neuron



with open('FI.dat', 'wb') as f:  # Python 3: open(..., 'wb')
    pickle.dump([I_e, F], f)