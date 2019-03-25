import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import nest
from sample.single_neuronBG import withSpike
import numpy as np
import sample.tls as tls
from sample.param import nparam
from sample.param import state





class BaseModel(withSpike):
	def __init__(self,nparam,cparam, random = False):
		self.popN = {"P_D1":None,"P_D2": None,"P_STN": None,"P_GPTA": None, "P_GPTI": None, "P_GPI": None, "P_FSN": None}
		for i in self.popN:
			self.popN[i]=cparam[i]
		 
		super().__init__(nparam,self.popN)

		if not random:

			for source in state:
				if not source in ["drawAll"]:
					sneuron = state[source]
					for dest in sneuron:
						if sneuron[dest] and dest not in ["CTX"]:
							nest.Connect(self.nID[source],self.nID[dest])
							print("Connected "+source+" to "+dest)
							print(sneuron[dest])

		if random:


		




















if __name__ == '__main__':
	cparam = tls.importParam()
	BG = BaseModel(nparam,cparam)
	BG.simulate()
	BG.plotVm()


