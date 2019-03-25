import sys
import os
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import sample.tls as tls
import sample.BasalFiring.paramtest8noGPI as param # Desired parameters
import sample.BGnodes
from sample.network.BGnetwork import BGnetwork
import matplotlib.pyplot as plt
import nest
import time
import numpy as np
from itertools import product


class varBG(BGnetwork):
	def __init__(self,nparam,cparam,synparam, noise,synparamNoise, connections, pparam=True):
		super().__init__(nparam,cparam,synparam, noise,synparamNoise, connections, pparam)

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
	def setCTX_GPTI(self,rate):
		nest.SetStatus(self.noiseID['GPTI'], {'rate' : rate})
		print('Set rate for CTX GPTI to: ', rate)
	def setCTX_STN(self,rate):
		nest.SetStatus(self.noiseID['STN'], {'rate' : rate})
		print('Set rate for CTX STN to: ', rate)
	def setCTXJ(self, J):
		nest.SetStatus(nest.GetConnections(self.noiseID['GPTI'],self.nID['GPTI']),{'weight': J })
		print('Set weight for CTX STN to: ', J)
		nest.SetStatus(nest.GetConnections(self.noiseID['STN'],self.nID['STN']),{'weight': J })
		print('Set rate for CTX GPTI to: ', J)
	#	def setJD2(self,J):





#paramNEW= t.tune(param.nparam, param.cparamOLD, param.staticsyn, param.noise, param.staticsynNoise, param.connections)
nest.ResetKernel()

BG1 = varBG(param.nparam, param.cparam, param.staticsyn, param.noise,param.staticsynNoise, param.connections,param.pparam)
nest.SetKernelStatus({'data_path': '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/variableBG/data/', 'overwrite_files':True})
#BG1.connectMultimeterNew(to_file = True)
BG1.connectSpikeDet()
BG1.setIe(0.0)

vary = False
varyCTX = False
varyNoiseJ= False
vary1000 = False
varyLow = True

if vary:
	rate = [2400.0, 3000.0]
	JGPTI = [-0.09, -1.5]
	JSTN = [0.04, 1.1]

	simLength = len(rate) * len(JGPTI) * len(JSTN)
	tot = time.time()
	count = 0
	for r in rate:
		for jGPTI in JGPTI:
			for jSTN in JSTN:
				currentTime = time.time()
				BG1.setRateD2(r)
				BG1.setJGPTI(jGPTI)
				BG1.setJSTN(jSTN)
				BG1.simulate(1000.0)
				print('Sim took: ', time.time() - currentTime)
				count = count+1
				print(simLength-count, ' simulations to go')
				print((simLength-count)*(time.time() - currentTime )/60.0,' minutes left')


	print('Total simulation took: ', time.time()-tot)
elif varyCTX:
	rate = np.linspace(1400,2200, 5)
	JGPTI = [-0.05, -1.9]
	jSTN = 1.4

	simLength = len(rate) * len(JGPTI)
	tot = time.time()
	count = 0

	for r in rate:
		for jGPTI in JGPTI:
			currentTime = time.time()
			BG1.setCTX_GPTI(r)
			BG1.setCTX_STN(r)
			BG1.setJGPTI(jGPTI)
			BG1.setJSTN(jSTN)
			BG1.simulate(1000.0)
			print('Sim took: ', time.time() - currentTime)
			count = count+1
			print(simLength-count, ' simulations to go')
			print((simLength-count)*(time.time() - currentTime )/60.0,' minutes left')
	print('Total simulation took: ', time.time()-tot)

elif varyNoiseJ:
	weight = np.linspace(1.0,4.0,4)
	JGPTI = [-0.05, -1.9]
	jSTN = 1.4

	simLength = len(weight) * len(JGPTI)
	tot = time.time()
	count = 0

	for w in weight:
		for jGPTI in JGPTI:
			currentTime = time.time()
			BG1.setCTX_STN(1400.0)
			BG1.setCTX_GPTI(1400.0)
			BG1.setJGPTI(jGPTI)
			BG1.setJSTN(jSTN)
			BG1.setCTXJ(w)
			BG1.simulate(1000.0)
			print('Sim took: ', time.time() - currentTime)
			count = count+1
			print(simLength-count, ' simulations to go')
			print((simLength-count)*(time.time() - currentTime )/60.0,' minutes left')
	print('Total simulation took: ', time.time()-tot)

elif vary1000:
	JGPTI = np.linspace(-1.9,-0.05, 10)
	JSTN = np.linspace(0.05,1.9, 10)
	rate = np.linspace(2600,3400,10)
	simLength = len(rate) * len(JGPTI) * len(JSTN)
	tot = time.time()
	count = 0
	for r in rate:
		for jGPTI in JGPTI:
			for jSTN in JSTN:
				currentTime = time.time()
				BG1.setRateD2(r)
				BG1.setJGPTI(jGPTI)
				BG1.setJSTN(jSTN)
				BG1.simulate(8000.0)
				print('Sim took: ', time.time() - currentTime)
				count = count+1
				print(simLength-count, ' simulations to go')
				print((simLength-count)*(time.time() - currentTime )/60.0/60.0,' hours left')
	print('Total simulation took: ', time.time()-tot)






elif varyLow:
    JGPTI = np.linspace(-1.9,-0.05, 10)
    JSTN = np.linspace(1.9,2.5, 4)
    rate = np.linspace(2600,2866,4)
    simLength = len(rate) * len(JGPTI) * len(JSTN)
    it = list(product(rate,JGPTI,JSTN))
    tot = time.time()
    count = 0
    for i in it[0:]:
        r = i[0]
        jGPTI = i[1]
        jSTN = i[2]
        nest.ResetKernel()
        BG1 = varBG(param.nparam, param.cparam, param.staticsyn, param.noise,param.staticsynNoise, param.connections,param.pparam)
        path = '/Users/kimhedelin/Documents/THESIS_LOCAL/dataVaryLow2/'
        dirName = path+'S'+str(count)+'-'+str(round(r,2))+''+str(round(jGPTI,2))+'-'+str(round(jSTN,2))
        if not os.path.exists(dirName):
                os.mkdir(dirName)
                print("Directory " , dirName ,  " Created ")
        else:
                print("Directory " , dirName ,  " already exists")
        nest.SetKernelStatus({'data_path' : dirName})
        BG1.connectSpikeDet()
        BG1.setIe(0.0)
        currentTime = time.time()
        BG1.setRateD2(r)
        BG1.setJGPTI(jGPTI)
        BG1.setJSTN(jSTN)
        BG1.simulate(8000.0)
        print('Sim took: ', time.time() - currentTime)
        count = count+1
        print(simLength-count, ' simulations to go')
        print((simLength-count)*(time.time() - currentTime )/60.0/60.0,' hours left')
    print('Total simulation took: ', time.time()-tot)






else:
	r = 2400.0
	jGPTI = - 0.09
	jSTN =  1.4
	
	BG1.setJGPTI(jGPTI)
	BG1.setJSTN(jSTN)
	BG1.simulate(1000.0)
