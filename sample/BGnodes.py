import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import sample.tls as tls

import nest
import nest.raster_plot
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from collections import Counter


class BGnodes:
	def __init__(self,nparam, pparam = True):
		# nparam must be a dictionary of the form nparam = {"neuron" : {"param1": var, "param2" : var}}
		# pparam must be a dictionary of the form pparam = {"neuron" : population}
		# nID = the device ID given from nest at creation
		nest.SetKernelStatus({"local_num_threads": 4})
		nest.SetKernelStatus({'data_path': '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/data', 'overwrite_files':True})
		self.nID = {"D1" : None, "D2" : None, "STN" : None, "GPI" : None, "GPTA" : None, "GPTI" : None, "FSN" : None}
		self.nModel = {"D1" :"iaf_cond_alpha" , "D2" : "iaf_cond_alpha", "FSN" : "iaf_cond_alpha", 
					  "GPI" : "aeif_cond_exp", "GPTA" : "aeif_cond_exp", "GPTI" : "aeif_cond_exp", "STN" : "aeif_cond_exp"}

		nest.SetDefaults('aeif_cond_exp',{'gsl_error_tol': 1e-06})
		for ID in self.nID :
			if pparam == True:
				self.nID[ID] = nest.Create(self.nModel[ID],1,nparam[ID])
				print('asdf')
				
			else:
				print(ID)
				print(pparam[ID])
				
				self.nID[ID] = nest.Create(self.nModel[ID],int(pparam[ID]),nparam[ID])



	def connectMultimeter(self,recordG = False):
		# Connects multimeter that records from V_m. Todo: record from other parameters as well
		if not recordG:
			self.multimeter = nest.Create("multimeter")
			nest.SetStatus(self.multimeter, {"withtime":True, "record_from":["V_m"]})

			for ID in self.nID: # Connects the multimeter to every node in the network
				nest.Connect(self.multimeter, self.nID[ID])

		else:
			self.multimeter = nest.Create("multimeter")
			nest.SetStatus(self.multimeter, {"withtime":True, "record_from":["V_m","g_ex"]})
			for ID in self.nID: # Connects the multimeter to every node in the network
				nest.Connect(self.multimeter, self.nID[ID])


	def connectMultimeterNew(self, recordG = False,**kwargs):
		self.multiID = dict()
		if not recordG:
			for ID in self.nID:
				self.multiID[ID] = nest.Create('multimeter')
				nest.SetStatus(self.multiID[ID],{'label' : ID, 'withtime': True,'record_from': ['V_m','g_ex','g_in']})
				if kwargs['to_file']:
					nest.SetStatus(self.multiID[ID],{'to_file':True})
				nest.Connect(self.multiID[ID], self.nID[ID])
			else:
				self.multiID[ID] = nest.Create('multimeter')
				nest.SetStatus(self.multiID[ID],{'label' : ID, 'withtime': True,'record_from': ['V_m','g_ex'],'to_file' : True})
				nest.Connect(self.multiID[ID], self.nID[ID])





	


	def connectSpikeDet(self):

		# Connects spike detector to every node
		self.spikeID = dict()
		#self.spikedetector = nest.Create("spike_detector",
                #params={"withgid": True, "withtime": True})

		for ID in self.nID:
			self.spikeID[ID] = nest.Create("spike_detector",1)
			nest.SetStatus(self.spikeID[ID], [{"label": ID,"withtime": True,"withgid": True, "to_file" : True}])
			nest.Connect(self.nID[ID], self.spikeID[ID])




	def simulate(self, t):
		nest.Simulate(float(t))

	def plotRaster(self,device):
		nest.raster_plot.from_device(self.spikeID[device], hist = True, title= device+' activity')
		nest.raster_plot.show()

	def get_G(self):

		self.G = {
					"GPTA" : { "G" : np.array([]), "t" : np.array([])},
					"GPTI" : { "G" : np.array([]), "t" : np.array([])},
					"STN" : { "G" : np.array([]), "t" : np.array([])},
					"GPI" : { "G" : np.array([]), "t" : np.array([])},
					"D1" : { "G" : np.array([]), "t" : np.array([])},
					"D2" : { "G" : np.array([]), "t" : np.array([])},
					"FSN" : { "G" : np.array([]), "t" : np.array([])}
					}
		x = (0,1,2)
		it = list(product(x,x))
		names = ["D1","D2","STN","GPI","GPTA", "GPTI","FSN"]
		dmm = nest.GetStatus(self.multimeter)[0]
		
		
		for i in range(7):
		    g = dmm["events"]["g_ex"][i::7]
		    ts = dmm["events"]["times"][i::7]
		    d = self.G[names[i]]
		    d["G"] = g
		    d["t"] = ts
		return self.G



	def plot_G(self,name =1):
		if name == 1:
			G = self.get_G()
			x = (0,1,2)
			it = list(product(x,x))
			names = ["D1","D2","STN","GPI","GPTA", "GPTI","FSN"]
			
			fig, axes = plt.subplots(3, 3)
			for i in range(7):
			    
			    axes[it[i]].plot(G[names[i]]["t"], G[names[i]]["G"])
			    axes[it[i]].set_title(names[i])
			    axes[it[i]].set_xlabel('ms')
			    axes[it[i]].set_ylabel('G')
			    #axes[it[i]].set_xlim((0,200))

			fig.set_dpi(70)
			fig.set_size_inches(8, 6)
			plt.subplots_adjust(hspace = 0.5, wspace = 0.5)
			plt.show()
		else:
			G = self.get_G()
			fig, axes = plt.subplots(1, 1)
			print(sum(G[name]["G"]))
			plt.plot(G[name]["t"], G[name]["G"])
			plt.title(name)
			plt.xlabel('ms')
			plt.ylabel('G')
			plt.show()



	def getVmNew(self,device):
		self.vm = {
					"GPTA" : { "Vm" : np.array([]), "t" : np.array([])},
					"GPTI" : { "Vm" : np.array([]), "t" : np.array([])},
					"STN" : { "Vm" : np.array([]), "t" : np.array([])},
					"GPI" : { "Vm" : np.array([]), "t" : np.array([])},
					"D1" : { "Vm" : np.array([]), "t" : np.array([])},
					"D2" : { "Vm" : np.array([]), "t" : np.array([])},
					"FSN" : { "Vm" : np.array([]), "t" : np.array([])}
					}
		return nest.GetStatus(self.multiID[device])


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



	def plotVm(self,name = 1):
		if name == 1:
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
		else:
			vm = self.get_vm()
			fig, axes = plt.subplots(1, 1)
			plt.plot(vm[name]["t"], vm[name]["Vm"])
			plt.title(name)
			plt.xlabel('ms')
			plt.ylabel('Vm')
			plt.show()

	def countSpikes(self):
		
		self.freq ={ "GPTA" : None, "GPTI" : None, "STN" : None, "GPI" : None, "D1" : None, "D2": None, "FSN" : None}

		

		for ID in self.nID:
			dSD = nest.GetStatus(self.spikeID[ID],keys="events")[0]
			evs = dSD["senders"]
			ts = dSD["times"]
			self.count = Counter(evs)
			self.freq[ID] = self.count[self.nID[ID][0]]

	def setIe(self,I_e,device = 1):
		if device ==1:
			for ID in self.nID:
				nest.SetStatus(self.nID[ID],{"I_e" : float(I_e)})
		else:
			nest.SetStatus(self.nID[device],{"I_e" : float(I_e)})


if __name__ == '__main__':
	cparam = tls.importParam()
	# Building the pparam
	pparam = { "GPTA" : None, "GPTI" : None, "STN" : None, "GPI" : None, "D1" : None, "D2": None, "FSN" : None}
	for p in cparam:
		if p[0] in ["P"] and not p in ["P_n"]:
			pparam[p.split("_")[1]] = int(cparam[p])

	#print(pparam)
	BG1 = BGnodes(nparam)
	BG1.connectMultimeter(1234)
	BG1.connectSpikeDet()
	BG1.simulate(1000.0)
	BG1.setIe(0.0,"GPTA")
	BG1.simulate(1000.0)
	BG1.countSpikes()
	f = BG1.freq
	print(f)
	BG1.plot_G('GPTA')