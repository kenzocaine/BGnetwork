import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import glob
import numpy as np
import sample.oscilating.paramOsc as param
import sample.LINDAHLtune as t
import matplotlib.pyplot as plt
from itertools import product
import time

paramNEW= t.tune(param.nparam, param.cparamOLD, param.staticsyn, param.noise, param.staticsynNoise, param.connections)

plotD1 = True
plotD2 = True
plotFSN = False
plotGPI = True
plotGPTA = True
plotGPTI = True
plotSTN = True
plotALL = False

simtime = 500
bins = 5
b = bins *1e-3 
if plotGPTI:
	#xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/freemembrane/data/GPTI-15141-0.dat')
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/freemembrane/data/GPTI-15149-0.gdf')
	ed = np.arange(0,simtime,bins)
	#print(xx[:,1]/5.0)
	w = paramNEW.pparam['GPTI']*b
	weight = np.ones(len(xx[:,1]))*1/w
	#plt.subplot(331)
	plt.subplot(211)
	plt.hist(xx[:,1],ed, weights = weight)
	
	#plt.title('GPTI')
	#print(xx[:,1]/5.0)

if plotSTN:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/freemembrane/data/STN-15146-0.gdf')
	ed = np.arange(0,simtime,bins)
	#print(xx[:,1]/5.0)
	w = paramNEW.pparam['STN']*b
	weight = np.ones(len(xx[:,1]))*1/w
	#plt.subplot(331)
	plt.subplot(212)
	plt.hist(xx[:,1],ed, weights = weight)
	
	#plt.title('')
	#
plt.show()
