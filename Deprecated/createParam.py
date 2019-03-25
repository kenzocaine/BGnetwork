import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
from sample.param import cparamOLD, nparam, staticsyn, cparamOLD1, noise, staticsynNoise
import numpy as np
import copy
import pickle

pparam = {"D1" : None, "D2" : None, "FSN" : None, "GPTA" : None, "GPTI" : None, "GPI" : None, "STN" : None	}



class param:
	def __init__(self, nparam, pparam, cparam, synparam, noise, synparamNoise):
		self.nparam = nparam
		self.pparam = pparam
		self.cparam = cparam
		self.synparam = synparam
		self.noise = noise 
		self.synparamNoise = synparamNoise


def exportPICKLE(param, name):
	f = open(name,"wb")
	pickle.dump(param,f)
	f.close()
	
	
def importPICKLE(name):
	f = open(name, "rb")
	return pickle.load(f)
	f.close()



def make_nparam(nparam):
	# Optional code in case some nparam needs to be changed in a procedural manner
	
	return nparam



def make_staticsyn(staticsyn):
	# Optional code in case some staticsyn needs to be changed in a procedural manner
	# 

	return staticsyn

def make_pparam(pparam):
	# Optional code in case some pparam needs to be changed in a procedural manner
	# 

	return pparam






def make_cparam(cparamOLD):
	# Optional code in case some cparam needs to be changed in a procedural manner
	# 
	cparamT = copy.deepcopy(cparamOLD) # New dictionary to store updated cparameters

	NSTR = ['P_D1','P_D2', 'P_FSN']
	N = ['C_D1_D1', 'C_D1_D2','C_D2_D1', 'C_D2_D2', 'C_FSN_D1','C_FSN_D2','C_FSN_FSN','C_D1_GPI','C_D2_GPTI']


	for n in cparamOLD:
		if n in N:
		    m = 5000
		    connectP = cparamOLD[n]/cparamOLD["P_"+n.split("_")[1]]
		   

		    N_Cnew = connectP * m

		    var = cparamOLD[n] * cparamOLD['lMSN'] * cparamOLD['g'+n[2:]]**2 *cparamOLD['tau'+n[2:]] * np.exp(2) / 4

		    mean = cparamOLD[n] * cparamOLD['lMSN'] * cparamOLD['g'+n[2:]] *cparamOLD['tau'+n[2:]] * np.exp(1)

		    gNEW = mean / (N_Cnew * cparamOLD['lMSN'] * cparamOLD['tau'+n[2:]] * np.exp(1))

		    cparamT['g'+n[2:]] = gNEW
		    cparamT[n] = np.round(N_Cnew)







	cparamT['P_D1'] = 5000
	cparamT['P_D2'] = 5000
	#print(cparamT)
	cparamT['P_FSN'] = cparamOLD['P_FSN']/cparamOLD['P_D1'] *cparamT['P_D1']
	for i in cparamOLD:
		if i[0:4] not in ['P_D1','P_D2','P_FS','gD1_','gD2_','gFSN','tauD','tauF']:
			cparamT[i] = cparamOLD[i] * 2 # double the amount of connection and pop for neurons not in str

			# total population
			cparamT['P_n'] =  cparamT['P_STN'] + cparamT['P_GPTA'] + cparamT['P_GPTI'] + cparamT['P_GPI'] + cparamT['P_FSN'] + cparamT['P_D1'] + cparamT['P_D2']




	cparam = copy.deepcopy(cparamOLD1)

	for i in cparamT:
		if i[0] in ["C"]:
			SOURCE = i.split("_")[1]
			TARGET = i.split("_")[2]
			cparam[TARGET][SOURCE] = round(cparamT[i])
	for i in cparamT:
		if i[0] in ["P"]:
			NODE = i.split("_")[1]
			if NODE not in ["n"]:
				pparam[NODE] = cparamT[i]

		
	return cparam,pparam










if __name__ == '__main__':
	
	
	cparam,pparam = make_cparam(cparamOLD)
	print("Cparam: ",cparam)
	print("Cparamold1", cparamOLD1)
	p = param(nparam,pparam, cparam, staticsyn, noise, staticsynNoise)
	exportPICKLE(p,"params.p")
	pil = importPICKLE("params.p")
	#print(pil.synparamNoise)

