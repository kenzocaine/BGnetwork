import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import nest
from BGcore.Model.BGnodes import BGnodes
import numpy as np
import BGcore.tls as tls


class BGnetwork(BGnodes):
	def __init__(self,nparam,cparam,synparam, noise,synparamNoise, connections, pparam=True):
		super().__init__(nparam,pparam)
		self.connect(nparam,cparam,synparam, noise, connections, pparam)
		self.createPoisson(noise, synparamNoise)




	def createPoisson(self,noise, synparamNoise):
		# Creates poisson generators with the desired parameters noise
		#
		self.noiseID = dict()
		for i in noise:
			self.noiseID[i] = nest.Create("poisson_generator",1,noise[i])


		for i in self.noiseID:
			nest.Connect(self.noiseID[i],self.nID[i], 'all_to_all',synparamNoise[i])
			print('Connected poisson to: '+i)
		



	def connect(self, nparam,cparam,synparam, noise, connections, pparam=True,poisson = True):
		# Connects the network using cparam
		#
		if pparam == True:
			for TARGET in self.nID:
				for SOURCE in connections[TARGET]:
					if connections[TARGET][SOURCE]:
						if SOURCE not in ["CTX"]:
							#Connect nodes to each other
							
							
							nest.Connect(self.nID[SOURCE],self.nID[TARGET],"one_to_one",synparam[TARGET][SOURCE])
							print("Connected "+SOURCE+" to "+TARGET)


		else:
			for TARGET in self.nID:
				for SOURCE in connections[TARGET]:
					if connections[TARGET][SOURCE]:
						if SOURCE not in ["CTX"]:
							#Connect nodes to each other
							
							
							nest.Connect(self.nID[SOURCE],self.nID[TARGET],{'rule': 'fixed_indegree', 'indegree': cparam[TARGET][SOURCE]},synparam[TARGET][SOURCE])
							print("Connected "+SOURCE+" to "+TARGET)








