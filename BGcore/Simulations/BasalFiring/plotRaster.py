import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import glob
import numpy as np
import sample.BasalFiring.paramtest as param
import sample.LINDAHLtune as t
import matplotlib.pyplot as plt
from itertools import product
import time

paramNEW= t.tune(param.nparam, param.cparamOLD, param.staticsyn, param.noise, param.staticsynNoise, param.connections)

plotD1 = True
plotD2 = True
plotFSN = True
plotGPI = True
plotGPTA = True
plotGPTI = True
plotSTN = True
plotALL = False

simtime = 500
bins = 10
b = bins *1e-3 
if plotD1:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/BasalFiring/data/D1-15144-0.gdf')
	ed = np.arange(0,simtime,bins)
	#print(xx[:,1]/5.0)
	w = param.pparam['D1']*b
	weight = np.ones(len(xx[:,1]))*1/w
	plt.subplot(331)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('D1')


if plotD2:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/BasalFiring/data/D2-15145-0.gdf')
	ed = np.arange(0,simtime,bins)
	#print(xx[:,1]/5.0)
	w = param.pparam['D2']*b
	weight = np.ones(len(xx[:,1]))*1/w
	plt.subplot(332)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('D2')



if plotFSN:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/BasalFiring/data/FSN-15150-0.gdf')
	ed = np.arange(0,simtime,bins)
	w = param.pparam['FSN']*b
	weight = np.ones(len(xx[:,1]))*1/w
	plt.subplot(333)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('FSN')



if plotGPI:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/BasalFiring/data/GPI-15147-0.gdf')
	ed = np.arange(0,simtime,bins)
	w = param.pparam['GPI']*b
	weight = np.ones(len(xx[:,1]))*1/w
	plt.subplot(334)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('GPI')

if plotGPTA:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/BasalFiring/data/GPTA-15148-0.gdf')
	ed = np.arange(0,simtime,bins)
	w = param.pparam['GPTA']*b
	weight = np.ones(len(xx[:,1]))*1/w
	plt.subplot(335)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('GPTA')

if plotGPTI:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/BasalFiring/data/GPTI-15149-0.gdf')
	ed = np.arange(0,simtime,bins)
	w = param.pparam['GPTI']*b
	weight = np.ones(len(xx[:,1]))*1/w
	plt.subplot(336)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('GPTI')

if plotSTN:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/BasalFiring/data/STN-15146-0.gdf')
	ed = np.arange(0,simtime,bins)
	w = param.pparam['STN']*b
	weight = np.ones(len(xx[:,1]))*1/w
	plt.subplot(337)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('STN')


plt.show()