import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import sample.tls
from sample.single_neuronBG import SingleNeurons 
from sample.param import nparam
import nest
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import pickle



class withSpike(SingleNeurons):
	def __init__(self,nparam):
		super().__init__(nparam)

		self.freq ={ "GPTA" : None, "GPTI" : None, "STN" : None, "GPI" : None, "D1" : None, "D2": None, "FSN" : None}
		self.spikedetector = nest.Create("spike_detector",
                params={"withgid": True, "withtime": True})
		nest.Connect(self.GPTA, self.spikedetector)
		nest.Connect(self.GPTI, self.spikedetector)
		nest.Connect(self.STN, self.spikedetector)
		nest.Connect(self.GPI, self.spikedetector)
		nest.Connect(self.D1, self.spikedetector)
		nest.Connect(self.D2, self.spikedetector) 
		nest.Connect(self.FSN, self.spikedetector)


	def countSpikes(self):
		dSD = nest.GetStatus(self.spikedetector,keys="events")[0]
		evs = dSD["senders"]
		ts = dSD["times"]


		self.count = Counter(evs)

		self.freq["GPTA"] = self.count[self.GPTA[0]]
		self.freq["GPTI"] = self.count[self.GPTI[0]]
		self.freq["STN"] = self.count[self.STN[0]]
		self.freq["GPI"] = self.count[self.GPI[0]]
		self.freq["D1"] = self.count[self.D1[0]]
		self.freq["D2"] = self.count[self.D2[0]]
		self.freq["FSN"] = self.count[self.FSN[0]]

		return self.freq


	def setIe(self,I_e):
		nest.SetStatus(self.GPTA,{"I_e" : float(I_e)})
		nest.SetStatus(self.GPTI,{"I_e" : float(I_e)})
		nest.SetStatus(self.STN,{"I_e" : float(I_e)})
		nest.SetStatus(self.GPI,{"I_e" : float(I_e)})
		nest.SetStatus(self.FSN,{"I_e" : float(I_e)})
		nest.SetStatus(self.D1,{"I_e" : float(I_e)})
		nest.SetStatus(self.D2,{"I_e" : float(I_e)})












I_e = np.arange(0,500,10)
F ={ "GPTA" : [], "GPTI" : [], "STN" : [], "GPI" : [], "D1" : [], "D2": [], "FSN" : []}

for i_e in I_e:
	NW = withSpike(nparam) # create the single neuron network with spike count
	NW.setIe(i_e) # Set the desired I_e
	NW.simulate() # Simulate the network
	freq = NW.countSpikes()
	nest.ResetNetwork()
	for i in freq:
		F[i] = F[i] + [freq[i]] # Put the count in a list for each neuron



with open('FI.dat', 'wb') as f:  # Python 3: open(..., 'wb')
    pickle.dump([I_e, F], f)







#plt.show()





