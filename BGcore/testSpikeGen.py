import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import sample.tls as tls
from sample.BGnodes import BGnodes 
from sample.param import nparam
import nest
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from collections import Counter


class testSpikeGen(BGnodes):

	def __init__(self,nparam,pparam = 1):
		super().__init__(nparam,pparam)
		self.spike_generator = nest.Create("spike_generator")
		nest.SetStatus(self.spike_generator,{"start": 500.0, "stop": 900.0, "spike_times": [600.0, 800.0], "spike_weights": [20.0, 20.0]})
		nest.Connect(self.spike_generator,self.nID["GPTA"])
		nest.Connect(self.spike_generator,self.nID["D1"])









if __name__ == '__main__':
	cparam = tls.importParam()
	pparam = { "GPTA" : None, "GPTI" : None, "STN" : None, "GPI" : None, "D1" : None, "D2": None, "FSN" : None}
	for p in cparam:
		if p[0] in ["P"] and not p in ["P_n"]:
			pparam[p.split("_")[1]] = int(cparam[p])

	#print(pparam)
	print(nparam)
	name = "D1"
	BG1 = testSpikeGen(nparam)
	BG1.connectMultimeter(1234)
	BG1.connectSpikeDet()
	BG1.setIe(0.0,name)
	BG1.simulate(1000.0)
	BG1.countSpikes()
	f = BG1.freq
	print(f)
	BG1.plot_G(name)

	BG1.plotVm(name)

