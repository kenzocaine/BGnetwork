import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/data")
import numpy as np
import matplotlib.pyplot as plt

plotD1 = False
plotD2 = False
plotFSN = False
plotGPI = True
plotGPTA = True
plotGPTI = True
plotSTN = True
plotALL = False

simtime = 8000.0
bins = 1000.0
pop = 100

if plotD1:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/tuneBasal/data/D1-716-0.gdf')
	ed = np.arange(1000,simtime,bins)
	#print(xx[:,1]/5.0)
	weight = np.ones(len(xx[:,1]))*1/(bins*1e-3*pop)
	plt.subplot(331)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('D1')


if plotD2:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/tuneBasal/data/D2-717-0.gdf')
	ed = np.arange(100,simtime,bins)
	#print(xx[:,1]/5.0)
	weight = np.ones(len(xx[:,1]))*1/(5e3*5e-3)
	plt.subplot(332)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('D2')



if plotFSN:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/tuneBasal/data/FSN-722-0.gdf')
	ed = np.arange(100,simtime,bins)
	#print(xx[:,1]/5.0)
	weight = np.ones(len(xx[:,1]))*1/(5e3*5e-3)
	plt.subplot(333)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('FSN')



if plotGPI:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/tuneBasal/data/GPI-719-0.gdf')
	ed = np.arange(100,simtime,bins)
	#print(xx[:,1]/5.0)
	weight = np.ones(len(xx[:,1]))*1/(5e3*5e-3)
	plt.subplot(334)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('GPI')

if plotGPTA:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/tuneBasal/data/GPTA-720-0.gdf')
	ed = np.arange(100,simtime,bins)
	#print(xx[:,1]/5.0)
	weight = np.ones(len(xx[:,1]))*1/(5e3*5e-3)
	plt.subplot(335)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('GPTA')

if plotGPTI:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/tuneBasal/data/GPTI-721-0.gdf')
	ed = np.arange(100,simtime,bins)
	#print(xx[:,1]/5.0)
	weight = np.ones(len(xx[:,1]))*1/(5e3*5e-3)
	plt.subplot(336)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('GPTI')

if plotSTN:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/tuneBasal/data/STN-718-0.gdf')
	ed = np.arange(100,simtime,bins)
	#print(xx[:,1]/5.0)
	weight = np.ones(len(xx[:,1]))*1/(5e3*5e-3)
	plt.subplot(337)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('STN')


plt.show()