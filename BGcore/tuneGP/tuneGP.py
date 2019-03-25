import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import sample.tls as tls
import sample.tuneGP.param as param # Desired parameters
from sample.BGnodes import BGnodes
import nest
import sample.LINDAHLtune as t
import matplotlib.pyplot as plt
import numpy as np



class tuneGP(BGnodes):
	def __init__(self,nparam,cparam,synparam, noise,synparamNoise, connections, pparam=True):
		super().__init__(nparam,pparam)
		nest.SetKernelStatus({'data_path': '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/tuneGP/data/', 'overwrite_files':True})
		self.synparam = synparam
		self.synparamNoise = synparamNoise
		self.noise = noise
		self.cparam = cparam
	def connect(self):

		nest.Connect(self.nID['STN'],self.nID['GPTI'],{'rule': 'fixed_indegree', 'indegree': self.cparam['GPTI']['STN']},self.synparam['GPTI']['STN'])
		print("Connected "+"STN+"" to "+"GPTI")
		print('Weight is', self.synparam['GPTI']['STN'])

		nest.Connect(self.nID['D2'],self.nID['GPTI'],{'rule': 'fixed_indegree', 'indegree': self.cparam['GPTI']['D2']},self.synparam['GPTI']['D2'])
		print("Connected "+"D2"" to "+"GPTI")
		print('Weight is', self.synparam['GPTI']['D2'])

		nest.Connect(self.nID['GPTI'],self.nID['GPTI'],{'rule': 'fixed_indegree', 'indegree': self.cparam['GPTI']['GPTI']},self.synparam['GPTI']['GPTI'])
		print("Connected "+"GPTI"" to "+"GPTI")
		print('Weight is', self.synparam['GPTI']['GPTI'])

		nest.Connect(self.nID['GPTI'],self.nID['STN'],{'rule': 'fixed_indegree', 'indegree': self.cparam['STN']['GPTI']},self.synparam['STN']['GPTI'])
		print("Connected "+"GPTI"" to "+"STN")
		print('Weight is', self.synparam['STN']['GPTI'])


	def connectNoise(self, ):
		self.noiseID = dict()
		self.noiseID['STN'] = nest.Create("poisson_generator",1,self.noise['STN'])
		self.noiseID['D2'] = nest.Create('poisson_generator', 1, self.noise['D2'])
		self.noiseID['GPTI'] = nest.Create('poisson_generator', 1, self.noise['GPTI'])


		for ID in self.noiseID:
			nest.Connect(self.noiseID[ID],self.nID[ID], 'all_to_all',self.synparamNoise[ID])
			print('Connected poisson to: '+ID)

paramNEW= t.tune(param.nparam, param.cparamOLD, param.staticsyn, param.noise, param.staticsynNoise, param.connections)
pop = 100
pparam = {'D1' : pop, 'D2' : pop, 'FSN' : pop, 'GPTA' : pop, 'GPTI' : pop, 'STN' : pop, 'GPI' : pop}

BG1 = tuneGP(paramNEW.nparam, paramNEW.cparam, paramNEW.synparam, paramNEW.noise,paramNEW.synparamNoise, paramNEW.connections, paramNEW.pparam)
BG1.connectMultimeterNew(to_file = True)
BG1.connectSpikeDet()
BG1.setIe(0.0)
BG1.connect()
BG1.connectNoise()
BG1.simulate(1000.0)



