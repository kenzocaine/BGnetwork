import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import BGcore.tls as tls
import BGcore.oscilating.paramtest7 as param # Desired parameters
import BGcore.BGnodes
from BGcore.Model.BGnetwork import BGnetwork
import matplotlib.pyplot as plt
import nest
import numpy as np
import time


class oscNetwork(BGnetwork):
	def __init__(self,nparam,cparam,synparam, noise,synparamNoise, connections, pparam=True):
		super().__init__(nparam,cparam,synparam, noise,synparamNoise, connections, pparam)

	def setRate(self, rate):
		
		#nest.SetStatus(self.noiseID['D1'],{'rate' : rate})
		nest.SetStatus(self.noiseID['D2'],{'rate' : rate})
		print('Set rate for D2', self.noiseID['D2'])



#paramNEW= t.tune(param.nparam, param.cparamOLD, param.staticsyn, param.noise, param.staticsynNoise, param.connections)


BG1 = oscNetwork(param.nparam, param.cparam, param.staticsyn, param.noise,param.staticsynNoise, param.connections,param.pparam)
nest.SetKernelStatus({'data_path': '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/oscilating/data/', 'overwrite_files':True})
#BG1.connectMultimeterNew(to_file = True)
BG1.connectSpikeDet()
BG1.setIe(0.0)

varyRate = False

currentTime = time.time()
BG1.setRate(2800.0)
BG1.simulate(1000.0)

print('Simulation took: ', time.time()-currentTime)



if varyRate:
	trials = 0
	simtime = 0
	for RATE in np.arange(2600.0, 7000.0, 1000):
		BG1.setRate(RATE) 
		BG1.simulate(200.0)
		trials = trials + 1
		simtime = simtime + 100.0
		print('Done rate: ', RATE)


plotRaster = True
if plotRaster:
	try:
		BG1.plotRaster('D1')
	except nest.NESTError as err:
		print('D1: ',err)
	try:
		BG1.plotRaster('D2')
	except nest.NESTError as err:
		print('D2: ',err)
	try: 
		BG1.plotRaster('FSN')
	except nest.NESTError as err:
		print('FSN',err)
	try:
		BG1.plotRaster('GPI')
	except nest.NESTError as err:
		print('GPI: ',err)
	try: 
		BG1.plotRaster('GPTA')
	except nest.NESTError as err:
		print('GPTA:',err)
	try: 
		BG1.plotRaster('GPTI')
	except nest.NESTError as err:
		print('GPTI: ',err)
	try: 
		BG1.plotRaster('STN')
	except nest.NESTError as err:
		print('STN: ',err)