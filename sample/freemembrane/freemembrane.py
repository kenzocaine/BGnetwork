import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import sample.tls as tls
import sample.freemembrane.param as param # Desired parameters
import sample.BGnodes
from sample.network.BGnetwork import BGnetwork
import sample.LINDAHLtune as t
import matplotlib.pyplot as plt
import nest


class freeMembrane(BGnetwork):
	def __init__(self,nparam,cparam,synparam, noise,synparamNoise, connections, pparam=True):
		super().__init__(nparam,cparam,synparam, noise,synparamNoise, connections, pparam)
		#self.setThreshold()

	def setThreshold(self):
		check = ['GPTI', 'GPTA', 'STN', 'GPI']
		for ID in self.nID:
			#print(self.nID[ID])
			if ID not in check:
				nest.SetStatus([self.nID[ID][0]], {'V_th' : 1e3})
			else:
				nest.SetStatus([self.nID[ID][0]], {'V_peak' : 1e3})


paramNEW= t.tune(param.nparam, param.cparamOLD, param.staticsyn, param.noise, param.staticsynNoise, param.connections)


BG1 = freeMembrane(paramNEW.nparam, paramNEW.cparam, paramNEW.synparam, paramNEW.noise,paramNEW.synparamNoise, paramNEW.connections,paramNEW.pparam)
nest.SetKernelStatus({'data_path': '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/freeMembrane/data/', 'overwrite_files':True})
BG1.connectMultimeterNew(to_file = True)
BG1.connectSpikeDet()
BG1.setIe(0.0)
BG1.simulate(500.0)