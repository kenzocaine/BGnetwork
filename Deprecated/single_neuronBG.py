import nest
import numpy as np
from itertools import product
from collections import Counter
import matplotlib.pyplot as plt


class SingleNeurons:
	def __init__(self,nparam, popN = 1):
		#nest.ResetNetwork()
		
		if popN:
			self.popN ={ "GPTA" : 1, "GPTI" : 1, "STN" : 1, "GPI" : 1, "D1" : 1, "D2": 1, "FSN" : 1}


		self.nparam = nparam
		self.vm = {
		"GPTA" : { "Vm" : np.array([]), "t" : np.array([])},
		"GPTI" : { "Vm" : np.array([]), "t" : np.array([])},
		"STN" : { "Vm" : np.array([]), "t" : np.array([])},
		"GPI" : { "Vm" : np.array([]), "t" : np.array([])},
		"D1" : { "Vm" : np.array([]), "t" : np.array([])},
		"D2" : { "Vm" : np.array([]), "t" : np.array([])},
		"FSN" : { "Vm" : np.array([]), "t" : np.array([])}
		}
		# adaptive exponential iaf model
		self.GPTA = nest.Create("aeif_cond_exp",self.popN["GPTA"])
		self.GPTI = nest.Create("aeif_cond_exp",self.popN["GPTI"])
		self.STN = nest.Create("aeif_cond_exp",self.popN["STN"])
		self.GPI = nest.Create("aeif_cond_exp",self.popN["GPI"])

		# alpha
		self.FSN = nest.Create("iaf_cond_alpha",self.popN["FSN"])
		self.D1 = nest.Create("iaf_cond_alpha",self.popN["D1"])
		self.D2 = nest.Create("iaf_cond_alpha",self.popN["D2"])

		self.nID = {"GPTA":self.GPTA, "GPTI": self.GPTI, "STN": self.STN, "GPI": self.GPI, "FSN": self.FSN, "D1": self.D1, "D2": self.D2}


		self.set_nparam(self.GPTA,nparam,"GPTA")
		self.set_nparam(self.GPTI,nparam,"GPTI")
		self.set_nparam(self.STN,nparam,"STN")
		self.set_nparam(self.GPI,nparam,"GPI")
		self.set_nparam(self.FSN,nparam,"FSN")
		self.set_nparam(self.D1,nparam,"D1")
		self.set_nparam(self.D2,nparam,"D2")

		self.multimeter = nest.Create("multimeter")
		nest.SetStatus(self.multimeter, {"withtime":True, "record_from":["V_m"]})

		# Connect neurons to multimeter
		nest.Connect(self.multimeter, self.GPTA)
		nest.Connect(self.multimeter, self.GPTI)
		nest.Connect(self.multimeter, self.STN)
		nest.Connect(self.multimeter, self.GPI)
		nest.Connect(self.multimeter, self.D1)
		nest.Connect(self.multimeter, self.D2)
		nest.Connect(self.multimeter, self.FSN)




	def set_nparam(self,neuron, nparam, name):
	    p = self.nparam[name]
	    if name in ["GPTA","GPTI","STN","GPI"]: # Test if adaptive integrate and fire
	        for i in p:
	            if i not in ["t_f","beta_E_L"]:
	                nest.SetStatus(neuron, {i : float(p[i])})
	    else:
	        for i in p:
	            nest.SetStatus(neuron, {i: float(p[i])})

	def get_nparam(self):
		return self.nparam

	def simulate(self):
		nest.Simulate(1000.0)


	def get_vm(self):
		x = (0,1,2)
		it = list(product(x,x))
		names = ["GPTA", "GPTI","STN","GPI","D1","D2","FSN"]
		dmm = nest.GetStatus(self.multimeter)[0]
		
		
		for i in range(7):
		    Vms = dmm["events"]["V_m"][i::7]
		    ts = dmm["events"]["times"][i::7]
		    d = self.vm[names[i]]
		    d["Vm"] = Vms
		    d["t"] = ts
		   
		

	def plotVm(self):
		self.get_vm()
		x = (0,1,2)
		it = list(product(x,x))
		names = ["GPTA", "GPTI","STN","GPI","D1","D2","FSN"]
		
		fig, axes = plt.subplots(3, 3)
		for i in range(7):
		    
		    axes[it[i]].plot(self.vm[names[i]]["t"], self.vm[names[i]]["Vm"])
		    axes[it[i]].set_title(names[i])
		    axes[it[i]].set_xlabel('ms')
		    axes[it[i]].set_ylabel('Vm')
		    axes[it[i]].xlim((0,200))

		fig.set_dpi(70)
		fig.set_size_inches(8, 6)
		plt.subplots_adjust(hspace = 0.5, wspace = 0.5)
		plt.show()




class withSpike(SingleNeurons):
	def __init__(self,nparam,popN = 1):
		super().__init__(nparam, popN)

		self.freq ={ "GPTA" : None, "GPTI" : None, "STN" : None, "GPI" : None, "D1" : None, "D2": None, "FSN" : None}
		self.spikedetector = nest.Create("spike_detector",
                params={"withgid": True, "withtime": True})
		nest.Connect(self.GPTA, self.spikedetector)
		nest.Connect(self.GPTI, self.spikedetector)
		nest.Connect(self.STN, self.spikedetector)
		nest.Connect(self.GPI, self.spikedetector)
		nest.Connect(self.D1, self.spikedetector)
		nest.Connect(self.D2, self.spikedetector) 
		nest.Connect(self.FSN, self.spikedetector)


	def countSpikes(self):
		dSD = nest.GetStatus(self.spikedetector,keys="events")[0]
		evs = dSD["senders"]
		ts = dSD["times"]


		self.count = Counter(evs)

		self.freq["GPTA"] = self.count[self.GPTA[0]]
		self.freq["GPTI"] = self.count[self.GPTI[0]]
		self.freq["STN"] = self.count[self.STN[0]]
		self.freq["GPI"] = self.count[self.GPI[0]]
		self.freq["D1"] = self.count[self.D1[0]]
		self.freq["D2"] = self.count[self.D2[0]]
		self.freq["FSN"] = self.count[self.FSN[0]]

		return self.freq


	def setIe(self,I_e):
		nest.SetStatus(self.GPTA,{"I_e" : float(I_e)})
		nest.SetStatus(self.GPTI,{"I_e" : float(I_e)})
		nest.SetStatus(self.STN,{"I_e" : float(I_e)})
		nest.SetStatus(self.GPI,{"I_e" : float(I_e)})
		nest.SetStatus(self.FSN,{"I_e" : float(I_e)})
		nest.SetStatus(self.D1,{"I_e" : float(I_e)})
		
		nest.SetStatus(self.D2,{"I_e" : float(I_e)})




	









if __name__ == '__main__':
	from param import nparam
	#nest.ResetNetwork()
	a = withSpike(nparam,10)
	a.simulate()
	#data = a.get_vm()
	a.plotVm()
	#print(data)
	