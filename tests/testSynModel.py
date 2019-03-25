import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import sample.tls as tls
from sample.single_neuronBG import withSpike 
from sample.param import nparam
import nest
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from collections import Counter


class BGnodes:
	def __init__(self,nparam, pparam = 1):
		# nparam must be a dictionary of the form nparam = {"neuron" : {"param1": var, "param2" : var}}
		# pparam must be a dictionary of the form pparam = {"neuron" : population}
		# nID = the device ID given from nest at creation
		self.nID = {"D1" : None, "D2" : None, "STN" : None, "GPI" : None, "GPTA" : None, "GPTI" : None, "FSN" : None}
		self.nModel = {"D1" :"iaf_cond_alpha" , "D2" : "iaf_cond_alpha", "FSN" : "iaf_cond_alpha", 
					  "GPI" : "aeif_cond_exp", "GPTA" : "aeif_cond_exp", "GPTI" : "aeif_cond_exp", "STN" : "aeif_cond_exp"}
		for ID in self.nID :
			if pparam:
				self.nID[ID] = nest.Create(self.nModel[ID],pparam,nparam[ID])
				print(ID)
			else:
				print(ID)
				self.nID[ID] = nest.Create(self.nModel[ID],pparam[ID],nparam[ID])



	def connectMultimeter(self):
		# Connects multimeter that records from V_m. Todo: record from other parameters as well
		
		self.multimeter = nest.Create("multimeter")
		nest.SetStatus(self.multimeter, {"withtime":True, "record_from":["V_m"]})

		for ID in self.nID: # Connects the multimeter to every node in the network
			nest.Connect(self.multimeter, self.nID[ID])


	def simulate(self, t):
		nest.Simulate(float(t))


	def connectSpikeDet(self):

		# Connects spike detector to every node
		self.spikedetector = nest.Create("spike_detector",
                params={"withgid": True, "withtime": True})

		for ID in self.nID:
			nest.Connect(self.nID[ID], self.spikedetector)



	def get_vm(self): # Retrieves the membrane potential data and return it as a dictionary
			
			self.vm = {
						"GPTA" : { "Vm" : np.array([]), "t" : np.array([])},
						"GPTI" : { "Vm" : np.array([]), "t" : np.array([])},
						"STN" : { "Vm" : np.array([]), "t" : np.array([])},
						"GPI" : { "Vm" : np.array([]), "t" : np.array([])},
						"D1" : { "Vm" : np.array([]), "t" : np.array([])},
						"D2" : { "Vm" : np.array([]), "t" : np.array([])},
						"FSN" : { "Vm" : np.array([]), "t" : np.array([])}
						}
			x = (0,1,2)
			it = list(product(x,x))
			names = ["D1","D2","STN","GPI","GPTA", "GPTI","FSN"]
			dmm = nest.GetStatus(self.multimeter)[0]
			
			
			for i in range(7):
			    Vms = dmm["events"]["V_m"][i::7]
			    ts = dmm["events"]["times"][i::7]
			    d = self.vm[names[i]]
			    d["Vm"] = Vms
			    d["t"] = ts
			return self.vm



	def plotVm(self):
		vm = self.get_vm()
		x = (0,1,2)
		it = list(product(x,x))
		names = ["D1","D2","STN","GPI","GPTA", "GPTI","FSN"]
		
		fig, axes = plt.subplots(3, 3)
		for i in range(7):
		    
		    axes[it[i]].plot(vm[names[i]]["t"], vm[names[i]]["Vm"])
		    axes[it[i]].set_title(names[i])
		    axes[it[i]].set_xlabel('ms')
		    axes[it[i]].set_ylabel('Vm')
		    #axes[it[i]].set_xlim((0,200))

		fig.set_dpi(70)
		fig.set_size_inches(8, 6)
		plt.subplots_adjust(hspace = 0.5, wspace = 0.5)
		plt.show()


	def countSpikes(self):
		dSD = nest.GetStatus(self.spikedetector,keys="events")[0]
		evs = dSD["senders"]
		ts = dSD["times"]
		self.freq ={ "GPTA" : None, "GPTI" : None, "STN" : None, "GPI" : None, "D1" : None, "D2": None, "FSN" : None}

		self.count = Counter(evs)

		for ID in self.nID:
			self.freq[ID] = self.count[self.nID[ID][0]]




if __name__ == '__main__':
	cparam = tls.importParam()
	pparam = { "GPTA" : None, "GPTI" : None, "STN" : None, "GPI" : None, "D1" : None, "D2": None, "FSN" : None}
	for p in cparam:
		if p[0] in ["P"] and not p in ["P_n"]:
			pparam[p.split("_")[1]] = int(cparam[p])

	#print(pparam)
	BG1 = BGnodes(nparam)
	BG1.connectMultimeter()
	BG1.connectSpikeDet()
	BG1.simulate(1000.0)
	BG1.countSpikes()
	f = BG1.freq
	print(f)
	#BG1.plotVm()
		





