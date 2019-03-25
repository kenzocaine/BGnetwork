import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import numpy as np
import copy
import pickle
import sample.BasalFiring.param as par
#import param as par



pparam = {"D1" : None, "D2" : None, "FSN" : None, "GPTA" : None, "GPTI" : None, "GPI" : None, "STN" : None	}

class param:
	def __init__(self, nparam, pparam, cparam, synparam, noise, synparamNoise, connections):
		self.nparam = nparam
		self.pparam = pparam
		self.cparam = cparam
		self.synparam = synparam
		self.noise = noise 
		self.synparamNoise = synparamNoise
		self.connections = connections



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


def tune(nparam, cparamOLD, synparam, noise, synparamNoise, connections, tuneWeight = True):
	# Optional code in case some cparam needs to be changed in a procedural manner
	# 
	cparamT = copy.deepcopy(cparamOLD) # New dictionary to store updated cparameters
	synparam = copy.deepcopy(synparam)
	noise = copy.deepcopy(noise)
	synparamNoise = copy.deepcopy(synparamNoise)
	connections = copy.deepcopy(connections)

	NSTR = ['P_D1','P_D2', 'P_FSN']
	N = ['C_D1_D1', 'C_D1_D2','C_D2_D1', 'C_D2_D2', 'C_FSN_D1','C_FSN_D2','C_FSN_FSN','C_D1_GPI','C_D2_GPTI']

	cparamT['P_D1'] = 5000
	cparamT['P_D2'] = 5000
	cparamT['P_FSN'] = cparamOLD['P_FSN']/cparamOLD['P_D1'] *cparamT['P_D1']  

	for n in cparamOLD:
		if n in N:
		    m = cparamT[n]
		    #connectP = cparamOLD[n]/cparamOLD["P_"+n.split("_")[1]]
		    #print(cparamOLD[n])
		    #print(cparamOLD["P_"+n.split("_")[1]])
		    #print('Old conn prob: ', connectP)
		    #N_Cnew = connectP * m
		    #rint('New number of conn',N_Cnew)
		    N_Cnew = cparamOLD[n] * 2 # Double the amound of connections which will result in half the g for every node
		    var = cparamOLD[n] * cparamOLD['lMSN'] * cparamOLD['g'+n[2:]]**2 *cparamOLD['tau'+n[2:]] * np.exp(2) / 4

		    mean = cparamOLD[n] * cparamOLD['lMSN'] * cparamOLD['g'+n[2:]] *cparamOLD['tau'+n[2:]] * np.exp(1)

		    gNEW = mean / (N_Cnew * cparamOLD['lMSN'] * cparamOLD['tau'+n[2:]] * np.exp(1)) # Adjust g 
		    cparamT[n] = np.round(N_Cnew)
		    if n in ['C_D1_D1', 'C_D1_D2','C_D2_D1', 'C_D2_D2','C_D1_GPI','C_D2_GPTI']:
		    	cparamT['g'+n[2:]] = -gNEW
		    else:
		    	cparamT['g'+n[2:]] = gNEW 
			







	
	#print(cparamT)
	
	for i in cparamOLD:
		if i[0:4] not in ['P_D1','P_D2','P_FS','gD1_','gD2_','gFSN','tauD','tauF']:
			cparamT[i] = cparamOLD[i] * 2 # double the amount of connection and pop for neurons not in str

			# total population
			cparamT['P_n'] =  cparamT['P_STN'] + cparamT['P_GPTA'] + cparamT['P_GPTI'] + cparamT['P_GPI'] + cparamT['P_FSN'] + cparamT['P_D1'] + cparamT['P_D2']


	cparamOLD1 = {"D1" : {"D1" : 364, "D2" : 392, "FSN" : 16, "GPTA" : 10 }, 
             "D2" : {"D1" : 84, "D2" : 504, "FSN": 11, "GPTA" : 10 }, 
             "FSN" : {"FSN" : 10, "GPTA" : 10, "GPTI" : 10 },
             "STN" : {"GPTI" : 30},
             "GPTA" : {"STN" : 30, "GPTA" : 5, "GPTI" : 25 },
             "GPTI" : { "STN": 30,"D2" : 500, "GPTI" : 25, "GPTA" : 5},
             "GPI" : { "GPTI" : 32, "D1" : 500, "STN" : 30} }

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
				pparam[NODE] = int(cparamT[i])
	if tuneWeight:
		for i in cparamT:
			if i[0] in ["g"]:
				SOURCE =i[1:].split('_')[0]
				TARGET = i[1:].split('_')[1]
				synparam[TARGET][SOURCE]['weight'] = cparamT[i]
	


	p = param(nparam, pparam, cparam, synparam, noise, synparamNoise, connections)		
	return p


if __name__ == '__main__':
	params = tune(par.nparam, par.cparamOLD, par.staticsyn, par.noise, par.staticsynNoise, par.connections)
	print('D1: ',params.synparam['D1'])
	print('D2: ',params.synparam['D2'])
	print('FSN: ', params.synparam['FSN'])
	print('GPTA: ', params.synparam['GPTA'])
	print('GPTI: ',params.synparam['GPTI'])
	print('STN: ',params.synparam['STN'])
	print('GPI: ',params.synparam['GPI'])
	print('pop', params.pparam)
