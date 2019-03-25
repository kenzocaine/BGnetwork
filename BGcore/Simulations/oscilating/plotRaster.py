import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import glob
import numpy as np
import sample.oscilating.paramtest7 as param
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

simtime = 1000
bins = 20
b = bins *1e-3 
if plotD1:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/oscilating/data/D1-15144-0.gdf')
	ed = np.arange(0,simtime,bins)
	#print(xx[:,1]/5.0)
	w = paramNEW.pparam['D1']*b
	weight = np.ones(len(xx[:,1]))*1/w
	plt.figure(1)
	plt.subplot(241)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('D1')
	plt.subplot(245)
	plt.plot(xx[:,1], xx[:,0],'.')


if plotD2:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/oscilating/data/D2-15145-0.gdf')
	ed = np.arange(0,simtime,bins)
	#print(xx[:,1]/5.0)
	w = paramNEW.pparam['D2']*b
	weight = np.ones(len(xx[:,1]))*1/w
	plt.subplot(242)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('D2')
	plt.subplot(246)
	plt.plot(xx[:,1], xx[:,0],'.')



if plotFSN:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/oscilating/data/FSN-15150-0.gdf')
	ed = np.arange(0,simtime,bins)
	w = paramNEW.pparam['FSN']*b
	weight = np.ones(len(xx[:,1]))*1/w
	plt.subplot(243)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('FSN')
	plt.subplot(247)
	plt.plot(xx[:,1], xx[:,0],'.')



if plotGPI:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/oscilating/data/GPI-15147-0.gdf')
	ed = np.arange(0,simtime,bins)
	w = paramNEW.pparam['GPI']*b
	weight = np.ones(len(xx[:,1]))*1/w
	plt.subplot(244)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('GPI')
	plt.subplot(248)
	plt.plot(xx[:,1], xx[:,0],'.')

if plotGPTA:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/oscilating/data/GPTA-15148-0.gdf')
	ed = np.arange(0,simtime,bins)
	w = paramNEW.pparam['GPTA']*b
	weight = np.ones(len(xx[:,1]))*1/w

	plt.figure(2)
	plt.subplot(231)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('GPTA')
	plt.subplot(234)
	plt.plot(xx[:,1], xx[:,0],'.')

if plotGPTI:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/oscilating/data/GPTI-15149-0.gdf')
	ed = np.arange(0,simtime,bins)
	w = paramNEW.pparam['GPTI']*b
	weight = np.ones(len(xx[:,1]))*1/w
	plt.subplot(232)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('GPTI')

	plt.subplot(235)
	plt.plot(xx[:,1], xx[:,0],'.')

if plotSTN:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/oscilating/data/STN-15146-0.gdf')
	ed = np.arange(0,simtime,bins)
	w = paramNEW.pparam['STN']*b
	weight = np.ones(len(xx[:,1]))*1/w
	plt.subplot(233)
	plt.hist(xx[:,1],ed, weights = weight)
	plt.title('STN')


	plt.subplot(236)
	plt.plot(xx[:,1], xx[:,0],'.')


plt.show()