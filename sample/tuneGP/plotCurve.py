import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import numpy as np
#import sample.oscilating.paramOsc as param
import sample.LINDAHLtune as t
import matplotlib.pyplot as plt
from itertools import product
import sample.tuneGP.param as param

plotD2 = True
plotGPTA = True
plotGPTI = True
plotSTN = True
paramNEW= t.tune(param.nparam, param.cparamOLD, param.staticsyn, param.noise, param.staticsynNoise, param.connections)

simtime = 1000.0
bins = 10.0
pop = 100

if plotD2:
	#xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/tuneGP/data/D2-15130-0.dat')
	#ed = np.arange(1,simtime,bins)
	#print(xx[:,1]/5.0)
	#weight = np.ones(len(xx[:,1]))*1/(bins*1e-3*pop)
	#plt.subplot(331)
	#plt.plot(xx[:,1],xx[:,2])
	plt.title('D2')

	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/tuneGP/data/D2-15138-0.gdf')
	ed = np.arange(1,simtime,bins)
	#print(xx[:,1]/5.0)
	weight = np.ones(len(xx[:,1]))*1/(bins*1e-3*paramNEW.pparam['D2'])
	plt.subplot(332)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('Rate')
	plt.subplot(333)
	plt.plot(xx[:,1],xx[:,0],'.')
	plt.title('Raster')

if plotGPTI:

	#xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/tuneGP/data/GPTI-15134-0.dat')
	#ed = np.arange(1,simtime,bins)
	#print(xx[:,1]/5.0)
	#weight = np.ones(len(xx[:,1]))*1/(bins*1e-3*pop)
	#plt.subplot(334)
	#plt.plot(xx[:,1],xx[:,2])
	plt.title('GPTI')

	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/tuneGP/data/GPTI-15142-0.gdf')
	ed = np.arange(10,simtime,bins)
	#print(xx[:,1]/5.0)
	weight = np.ones(len(xx[:,1]))*1/(bins*1e-3*paramNEW.pparam['GPTI'])
	plt.subplot(335)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('Rate')
	plt.subplot(336)
	plt.plot(xx[:,1],xx[:,0],'.')
	plt.title('Raster')

if plotSTN:

	#xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/tuneGP/data/STN-15131-0.dat')
	#ed = np.arange(1,simtime,bins)
	#print(xx[:,1]/5.0)
	#weight = np.ones(len(xx[:,1]))*1/(bins*1e-3*pop)
	#plt.subplot(337)
	#plt.plot(xx[:,1],xx[:,2])
	plt.title('STN')

	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/tuneGP/data/STN-15139-0.gdf')
	ed = np.arange(1,simtime,bins)
	#print(xx[:,1]/5.0)
	weight = np.ones(len(xx[:,1]))*1/(bins*1e-3*paramNEW.pparam['STN'])
	plt.subplot(338)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('Rate')
	plt.subplot(339)
	plt.plot(xx[:,1],xx[:,0],'.')
	plt.title('Raster')

plt.show()
