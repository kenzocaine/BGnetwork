import sys
import os
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import BGcore.tls as tls
import BGcore.Simulations.BasalFiring.paramtest8 as param # ToDO: Double Check that BasalFiring is not oscillating
import BGcore.Model.BGnodes
from BGcore.Model.BGnetwork import BGnetwork
import matplotlib.pyplot as plt
import nest
import time
import numpy as np
from itertools import product

class transient(BGnetwork):
	def __init__(self,nparam,cparam,synparam, noise,synparamNoise, connections, pparam=True):
		super().__init__(nparam,cparam,synparam, noise,synparamNoise, connections, pparam)
		self.trans_noiseID = dict()
		self.synparamNoise = synparamNoise

	def impulseD1(self,start,stop):
		# Connect impulse poisson generator to D1 for 20 ms
		# 
		self.trans_noiseID['D1'] = nest.Create("poisson_generator",1,{'rate' : 2900.0, 'start':start,'stop':stop})
		nest.Connect(self.trans_noiseID['D1'],self.nID['D1'], 'all_to_all',self.synparamNoise['D1'])
		print('Connected transient poisson to D1')


	def impulseD2(self, start,stop):
		self.trans_noiseID['D2'] = nest.Create("poisson_generator",1,{'rate' : 2900.0, 'start':start,'stop':stop})
		nest.Connect(self.trans_noiseID['D2'],self.nID['D2'], 'all_to_all',self.synparamNoise['D2'])
		print('Connected transient poisson to D2')




# Record spike trains from all nodes
# 


nest.ResetKernel()
nest.SetKernelStatus({'data_path': '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/BGcore/Simulations/transient/data/', 'overwrite_files':True})

trans = transient(param.nparam, param.cparam, param.staticsyn, param.noise,param.staticsynNoise, param.connections,param.pparam)
trans.connectSpikeDet()
trans.setIe(0.0)
trans.impulseD1(1000.0,1020.0)
trans.impulseD2(1000.0,1020.0)
trans.simulate(1500.0)




