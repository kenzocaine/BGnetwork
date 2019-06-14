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
		self.trans_noiseID['D1'] = nest.Create("poisson_generator",1,{'rate' : 900.0, 'start':start,'stop':stop})
		nest.Connect(self.trans_noiseID['D1'],self.nID['D1'], 'all_to_all',self.synparamNoise['D1'])
		print('Connected transient poisson to D1')

# 15 ms pulse, DC input or poisson
# Cross correlate pair stimulate , take average

	def impulseD2(self, start,stop):
		self.trans_noiseID['D2'] = nest.Create("poisson_generator",1,{'rate' : 1500.0, 'start':start,'stop':stop})
		nest.Connect(self.trans_noiseID['D2'],self.nID['D2'], 'all_to_all',self.synparamNoise['D2'])
		print('Connected transient poisson to D2')

	def setJSTN(self, J):
		nest.SetStatus(nest.GetConnections(self.nID['STN'],self.nID['GPTI']),{'weight': J})
		print('Set STN --> GPTI weight to: ', J)

	def setJGPTI(self, J):
		print(len(nest.GetConnections(self.nID['GPTI'],self.nID['STN'])))
		nest.SetStatus(nest.GetConnections(self.nID['GPTI'],self.nID['STN']),{'weight': J })
		print('Set GTPI --> STN weight to: ', J)

	def setRateD2(self,rate):
		nest.SetStatus(self.noiseID['D2'],{'rate' : rate})
		print('Set rate for D2 to: ', rate)


# Record spike trains from all nodes
# 

setup1 = False


if setup1: 
	nest.ResetKernel()
	nest.SetKernelStatus({'data_path': '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/BGcore/Simulations/transient/data/', 'overwrite_files':True})

	trans = transient(param.nparam, param.cparam, param.staticsyn, param.noise,param.staticsynNoise, param.connections,param.pparam)
	trans.connectSpikeDet()
	trans.setIe(0.0)
	trans.impulseD1(1000.0,1030.0)
	trans.impulseD2(1000.0,1030.0)
	trans.simulate(1500.0)

setup2 = False

if setup2: 
	nest.ResetKernel()
	nest.SetKernelStatus({'data_path': '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/BGcore/Simulations/transient/data2/', 'overwrite_files':True})

	trans = transient(param.nparam, param.cparam, param.staticsyn, param.noise,param.staticsynNoise, param.connections,param.pparam)
	trans.connectSpikeDet()
	trans.setIe(0.0)
	trans.impulseD2(1000.0,1030.0)
	trans.simulate(1500.0)

setup3 = True

if setup3: 
	nest.ResetKernel()
	nest.SetKernelStatus({'data_path': '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/BGcore/Simulations/transient/data3/', 'overwrite_files':True})

	trans = transient(param.nparam, param.cparam, param.staticsyn, param.noise,param.staticsynNoise, param.connections,param.pparam)
	trans.connectSpikeDet()
	trans.setIe(0.0)
	jGPTI = -0.3
	jSTN = 1.5
	r = 3000.0
	trans.setJGPTI(jGPTI)
	trans.setJSTN(jSTN)
	trans.setRateD2(r)
	trans.impulseD2(1000.0,1030.0)
	trans.simulate(1500.0)