import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import BGcore.tls as tls
import BGcore.BasalFiring.paramtest8 as param # Desired parameters
import BGcore.BGnodes
from BGcore.BGnodes import BGnodes
import BGcore.LINDAHLtune as t
import matplotlib.pyplot as plt
import nest


class PSP(BGnodes):
	def __init__(self,nparam,synparam, synparamNoise, noise,testsyn, pparam=True):
		super().__init__(nparam, pparam)
		#self.setThreshold()
		self.synparam = synparam
		self.synparamNoise = synparamNoise
		self.noise = noise
		self.testsyn = testsyn

	def connect(self):
		nest.Connect(self.nID['GPTI'],self.nID['STN'], 'one_to_one',self.synparam['STN']['GPTI'])
		print("Connected "+"GPTI to STN")
		nest.Connect(self.nID['STN'], self.nID['GPTI'], 'one_to_one', self.synparam['GPTI']['STN'])
		print("Connected "+"STN to GPTI")


	def connectSpikeGen(self):
		self.spikeGEN = dict()

		self.spikeGEN['ex'] = nest.Create('spike_generator')
		nest.SetStatus(self.spikeGEN['ex'],{'start' : 0.0, 'stop' : 1000.0,'spike_times': [800.0], 'spike_weights': [1.0]})

		self.spikeGEN['in'] = nest.Create('spike_generator')
		nest.SetStatus(self.spikeGEN['in'],{'start' : 0.0, 'stop' : 1000.0,'spike_times': [500.0], 'spike_weights': [1.0]})

		
		# Connect inhibitory spike generator
		for ID in self.nID:

			nest.Connect(self.spikeGEN['in'], self.nID[ID],'one_to_one',self.testsyn[ID]['in'])
			nest.Connect(self.spikeGEN['ex'], self.nID[ID], 'one_to_one',self.testsyn[ID]['ex'])
			

	def connectNoise(self):
		self.noiseID = dict()
		
		self.noiseID['STN'] = nest.Create("poisson_generator",1,self.noise['STN'])
		nest.Connect(self.noiseID['STN'],self.nID['STN'], 'one_to_one',self.synparamNoise['STN'])
		self.noiseID['GPTI'] = nest.Create('poisson_generator',1, self.noise['GPTI'])
		nest.Connect(self.noiseID['GPTI'],self.nID['GPTI'], 'one_to_one',self.synparamNoise['GPTI'])


paramNEW= t.tune(param.nparam, param.cparamOLD, param.staticsyn, param.noise, param.staticsynNoise, param.connections)

pop = 1

testPop = {

            'D1' : pop,
            'D2' : pop,
            'FSN' : pop,
            'STN' : pop,
            'GPTA' : pop,
            'GPTI' : pop,
            'GPI' : pop
}

BG1 = PSP(param.nparam,param.staticsyn, param.staticsynNoise,param.noise,param.testsyn,testPop)
nest.SetKernelStatus({'data_path': '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/PSP/data/', 'overwrite_files':True})
BG1.connectMultimeterNew(to_file = True)
BG1.connectSpikeDet()
BG1.connectSpikeGen()
#BG1.connect()
BG1.setIe(0.0)
BG1.simulate(1000.0)