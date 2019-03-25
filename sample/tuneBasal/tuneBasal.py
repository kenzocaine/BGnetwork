import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import sample.tls as tls
import sample.oscilating.paramtest4 as param # Desired parameters
from sample.BGnodes import BGnodes
import nest
import sample.LINDAHLtune as t
import matplotlib.pyplot as plt
import numpy as np



class tuneBasal(BGnodes):
	def __init__(self,nparam,cparam,synparam, noise,synparamNoise, connections, pparam=True):

		super().__init__(nparam,pparam)
		nest.SetKernelStatus({'data_path': '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/tuneBasal/data/', 'overwrite_files':True})
		self.createPoisson(noise, synparamNoise)



	def createPoisson(self,noise, synparamNoise):
		# Creates poisson generators with the desired parameters noise
		#
		self.noiseID = dict()
		for ID in noise:
			self.noiseID[ID] = nest.Create("poisson_generator",1,noise[ID])


		for ID in self.noiseID:
			nest.Connect(self.noiseID[ID],self.nID[ID], 'all_to_all',synparamNoise[ID])
			print('Connected poisson to: '+ID)
	def setRate(self, rate):
		for ID in self.noiseID:
			nest.SetStatus(self.noiseID[ID],{'rate' : rate})
			print('Set rate for', self.noiseID[ID])

paramNEW= t.tune(param.nparam, param.cparamOLD, param.staticsyn, param.noise, param.staticsynNoise, param.connections)
pop = 100
pparam = {'D1' : pop, 'D2' : pop, 'FSN' : pop, 'GPTA' : pop, 'GPTI' : pop, 'STN' : pop, 'GPI' : pop}

BG1 = tuneBasal(param.nparam, param.cparam, param.staticsyn, param.noise,param.staticsynNoise, param.connections, pparam)
BG1.connectMultimeterNew(to_file = True)
BG1.connectSpikeDet()
BG1.setIe(0.0)
varyRate = True

if varyRate:
	trials = 0
	simtime = 0
	for RATE in np.arange(0.0, 1500.0, 200):
		BG1.setRate(RATE) 
		BG1.simulate(1000.0)
		trials = trials + 1
		simtime = simtime + 1000.0
		print('Done rate: ', RATE)
else:
	BG1.setRate(400.0)
	BG1.simulate(1000.0)

print('Number of trials', trials)
print('Total simulation time', simtime)


plotRaster = False

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