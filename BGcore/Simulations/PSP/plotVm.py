import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import glob
import numpy as np
import sample.BasalFiring.paramtest8 as param

import matplotlib.pyplot as plt
from itertools import product
import time
from sample.draw_connect import drawN

#paramNEW= t.tune(param.nparam, param.cparamOLD, param.staticsyn, param.noise, param.staticsynNoise, param.connections)

plotD1 = True
plotD2 = True
plotFSN = True
plotGPI = True
plotGPTA = True
plotGPTI = True
plotSTN = True
plotALL = False

simtime = 500
bins = 5
b = bins *1e-3 
averageEx = dict()
averageIn = dict()
if plotGPTI:
	plt.figure(1)
	#xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/freemembrane/data/GPTI-15141-0.dat')
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/PSP/data/GPTI-13-0.dat')
	plt.subplot(421)
	plt.plot(xx[:,1], xx[:,2])
	plt.title('GPTI')
	plt.xlabel('time (ms)')
	plt.ylabel('V_m')

	plt.subplot(423)
	plt.plot(xx[:,1], xx[:,3])
	plt.xlabel('time (ms)')
	plt.ylabel('Excitatory g')


	plt.subplot(425)
	plt.plot(xx[:,1], xx[:,4])
	plt.xlabel('time (ms)')
	plt.ylabel('Inhibiting g')
	gdf = False

	name = 'GPTI'
	maxi = np.max(xx[700:900,2])

	print(name+' Max is: ', maxi)
	print(name+' ex is: ', maxi - param.nparam[name]['E_L'])
	E_L = param.nparam[name]['E_L']
	

	# Calculate area under curve
	x = xx[800:850,2]-E_L
	
	averageEx['GPTI'] = np.sum(x)*1e-3

	mini = np.min(xx[450:600,2])
	print(name + ' Min is: ', mini)
	print(name + ' in is: ', mini - param.nparam[name]['E_L'])


	# Inhibiton
	
	x = xx[500:545,2] - param.nparam[name]['E_L']
	
	averageIn['GPTI'] = np.sum(x)*1e-3

	

if plotSTN:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/PSP/data/STN-10-0.dat')

	#plt.subplot(331)
	plt.subplot(422)
	plt.plot(xx[:,1], xx[:,2])
	plt.title('STN')
	plt.xlabel('time (ms)')
	plt.ylabel('V_m')

	plt.subplot(424)
	plt.plot(xx[:,1], xx[:,3])
	plt.xlabel('time (ms)')
	plt.ylabel('Excitatory g')


	plt.subplot(426)
	plt.plot(xx[:,1], xx[:,4])
	plt.xlabel('time (ms)')
	plt.ylabel('Inhibiting g')


	name = 'STN'
	maxi = np.max(xx[700:900,2])

	print(name+' Max is: ', maxi)
	print(name+' ex is: ', maxi - param.nparam[name]['E_L'])

	# Excitation
	
	x = xx[800:920,2] - param.nparam[name]['E_L']
	averageEx['STN'] = np.sum(x)*1e-3

	mini = np.min(xx[500:600,2])
	print(name + ' Min is: ', mini)
	print(name + ' in is: ', mini - param.nparam[name]['E_L'])

	# Inhibition
	x = xx[500:580,2] - param.nparam[name]['E_L']
	print(x)
	averageIn['STN'] = np.sum(x)*1e-3

	gdf = False
	if gdf:
		xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/PSP/data/STN-18-0.gdf')
		plt.subplot(428)
		plt.plot(xx[:,1], xx[:,0],'.')
		plt.xlabel('time (ms)')



if plotD1:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/PSP/data/D1-08-0.dat')
	plt.figure(2)
	#plt.subplot(331)
	plt.subplot(321)
	plt.plot(xx[:,1], xx[:,2])
	plt.title('D1')
	plt.xlabel('time (ms)')
	plt.ylabel('V_m')

	plt.subplot(323)
	plt.plot(xx[:,1], xx[:,3])
	plt.xlabel('time (ms)')
	plt.ylabel('Excitatory g')


	plt.subplot(325)
	plt.plot(xx[:,1], xx[:,4])
	plt.xlabel('time (ms)')
	plt.ylabel('Inhibiting g')

	name = 'D1'
	maxi = np.max(xx[700:900,2])

	print(name+' Max is: ', maxi)
	print(name+' ex is: ', maxi - param.nparam[name]['E_L'])


	# Excitation
	
	x = xx[800:950,2] - param.nparam[name]['E_L']
	averageEx['D1'] = np.sum(x)*1e-3

	mini = np.max(xx[450:600,2])
	print(name + ' Min is: ', mini)
	print(name + ' in is: ', mini - param.nparam[name]['E_L'])


	# Inhibition
	x = xx[500:580,2] - param.nparam[name]['E_L']
	averageIn['D1'] = np.sum(x)*1e-3

	gdf = False
	if gdf:
		xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/PSP/data/STN-18-0.gdf')
		plt.subplot(428)
		plt.plot(xx[:,1], xx[:,0],'.')
		plt.xlabel('time (ms)')

if plotD2:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/PSP/data/D2-09-0.dat')

	#plt.subplot(331)
	plt.subplot(322)
	plt.plot(xx[:,1], xx[:,2])
	plt.title('D2')
	plt.xlabel('time (ms)')
	plt.ylabel('V_m')

	plt.subplot(324)
	plt.plot(xx[:,1], xx[:,3])
	plt.xlabel('time (ms)')
	plt.ylabel('Excitatory g')


	plt.subplot(326)
	plt.plot(xx[:,1], xx[:,4])
	plt.xlabel('time (ms)')
	plt.ylabel('Inhibiting g')


	name = 'D2'
	maxi = np.max(xx[700:900,2])

	print(name+' Max is: ', maxi)
	print(name+' ex is: ', maxi - param.nparam[name]['E_L'])

	# Excitation
	
	x = xx[800:950,2] - param.nparam[name]['E_L']
	averageEx['D2'] = np.sum(x)*1e-3


	mini = np.max(xx[450:600,2])
	print(name + ' Min is: ', mini)
	print(name + ' in is: ', mini - param.nparam[name]['E_L'])



	# Inhibition
	x = xx[500:580,2] - param.nparam[name]['E_L']
	averageIn['D2'] = np.sum(x)*1e-3

	gdf = False
	if gdf:
		xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/PSP/data/STN-18-0.gdf')
		plt.subplot(428)
		plt.plot(xx[:,1], xx[:,0],'.')
		plt.xlabel('time (ms)')

if plotFSN:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/PSP/data/FSN-14-0.dat')

	#plt.subplot(331)
	plt.figure(3)
	plt.subplot(322)
	plt.plot(xx[:,1], xx[:,2])
	plt.title('FSN')
	plt.xlabel('time (ms)')
	plt.ylabel('V_m')

	plt.subplot(324)
	plt.plot(xx[:,1], xx[:,3])
	plt.xlabel('time (ms)')
	plt.ylabel('Excitatory g')


	plt.subplot(326)
	plt.plot(xx[:,1], xx[:,4])
	plt.xlabel('time (ms)')
	plt.ylabel('Inhibiting g')

	name = 'FSN'
	maxi = np.max(xx[700:900,2])

	print(name+' Max is: ', maxi)
	print(name+' ex is: ', maxi - param.nparam[name]['E_L'])

	# Excitation
	
	x = xx[800:900,2] - param.nparam[name]['E_L']
	averageEx['FSN'] = np.sum(x)*1e-3

	mini = np.min(xx[450:600,2])
	print(name + ' Min is: ', mini)
	print(name + ' in is: ', mini - param.nparam[name]['E_L'])

	# Inhibition
	x = xx[500:540,2] - param.nparam[name]['E_L']
	averageIn['FSN'] = np.sum(x)*1e-3


if plotGPTA:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/PSP/data/GPTA-12-0.dat')
	
	#plt.subplot(331)
	plt.subplot(321)
	plt.plot(xx[:,1], xx[:,2])
	plt.title('GPTA')
	plt.xlabel('time (ms)')
	plt.ylabel('V_m')

	plt.subplot(323)
	plt.plot(xx[:,1], xx[:,3])
	plt.xlabel('time (ms)')
	plt.ylabel('Excitatory g')


	plt.subplot(325)
	plt.plot(xx[:,1], xx[:,4])
	plt.xlabel('time (ms)')
	plt.ylabel('Inhibiting g')

	name = 'GPTA'
	maxi = np.max(xx[700:900,2])

	print(name+' Max is: ', maxi)
	print(name+' ex is: ', maxi - param.nparam[name]['E_L'])

	# Excitation
	
	x = xx[800:850,2] - param.nparam[name]['E_L']
	averageEx['GPTA'] = np.sum(x)*1e-3


	mini = np.min(xx[450:600,2])
	print(name + ' Min is: ', mini)
	print(name + ' in is: ', mini - param.nparam[name]['E_L'])

	# Inhibition
	x = xx[480:550,2] - param.nparam[name]['E_L']
	averageIn['GPTA'] = np.sum(x)*1e-3

	

if plotGPI:
	xx = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/PSP/data/GPI-11-0.dat')
	
	#plt.subplot(331)
	plt.figure(4)
	plt.subplot(311)
	plt.plot(xx[:,1], xx[:,2])
	plt.title('GPI')
	plt.xlabel('time (ms)')
	plt.ylabel('V_m')

	plt.subplot(312)
	plt.plot(xx[:,1], xx[:,3])
	plt.xlabel('time (ms)')
	plt.ylabel('Excitatory g')


	plt.subplot(313)
	plt.plot(xx[:,1], xx[:,4])
	plt.xlabel('time (ms)')
	plt.ylabel('Inhibiting g')

	name = 'GPI'
	maxi = np.max(xx[700:900,2])

	print(name+' Max is: ', maxi)
	print(name+' ex is: ', maxi - param.nparam[name]['E_L'])

	# Calc area under curve
	x = xx[800:880,2] - param.nparam[name]['E_L']
	averageEx['GPI'] = np.sum(x)*1e-3



	mini = np.min(xx[450:600,2])
	print(name + ' Min is: ', mini)
	print(name + ' in is: ', mini - param.nparam[name]['E_L'])
	# Calculate area under in curve
	x = xx[500:540,2]-param.nparam[name]['E_L']
	averageIn['GPI'] = np.sum(x)*1e-3


print(averageEx)
print(averageIn)
ratetemp = dict()

ratetemp['D1'] = 3 
ratetemp['D2'] = 3
ratetemp['FSN'] = 10
ratetemp['GPTI'] = 45
ratetemp['GPTA'] = 10
ratetemp['STN'] = 20
ratetemp['GPI'] = 30

rate = dict()
for TARGET in ratetemp:
	rate[TARGET] = dict()
	for SOURCE in ratetemp:
		if param.connections[TARGET][SOURCE]:
			rate[TARGET][SOURCE] = ratetemp[SOURCE]
	rate[TARGET]['CTX'] = param.noise[TARGET]['rate']

print(rate)


meanVm = dict()

for TARGET in rate:
	meanVm[TARGET] = dict()
	for SOURCE in rate[TARGET]:
		if param.connections[TARGET][SOURCE]:
			if SOURCE in ['STN']:
				 meanVm[TARGET][SOURCE] = rate[TARGET][SOURCE] * param.cparam[TARGET][SOURCE] * param.staticsyn[TARGET][SOURCE]['weight']* averageEx[TARGET]
			if SOURCE in ['CTX']:
				meanVm[TARGET][SOURCE] = rate[TARGET][SOURCE] * 1 * 1* averageEx[TARGET]

			else:
				meanVm[TARGET][SOURCE] = - rate[TARGET][SOURCE] * param.cparam[TARGET][SOURCE] * param.staticsyn[TARGET][SOURCE]['weight']* averageIn[TARGET]

print('Average is',meanVm)


fig = plt.figure(5)
fig.set_dpi(110)
fig.set_size_inches(10,11)
grid = np.mgrid[0.2:2.7:3j, 0.2:2.5:3j].reshape(2, -1).T
sc = 0.88
drawN('GPTI', param.cparam,grid[0,0],grid[0,1],sc,param.pparam,param.staticsyn,param.noise, meanVm)
drawN('D2', param.cparam,grid[1,0],grid[1,1],sc,param.pparam,param.staticsyn,param.noise, meanVm)
drawN('D1', param.cparam,grid[2,0],grid[2,1],sc,param.pparam,param.staticsyn,param.noise, meanVm)
drawN('GPTA', param.cparam,grid[3,0],grid[3,1],sc,param.pparam,param.staticsyn,param.noise, meanVm)
drawN('STN', param.cparam,grid[4,0],grid[4,1],sc,param.pparam,param.staticsyn,param.noise, meanVm)
drawN('FSN', param.cparam,grid[5,0],grid[5,1],sc,param.pparam,param.staticsyn,param.noise, meanVm)
drawN('GPI', param.cparam,grid[6,0],grid[6,1],sc,param.pparam,param.staticsyn,param.noise, meanVm)
plt.axis('equal')
plt.axis('off')
plt.tight_layout()
plt.rcParams['axes.facecolor'] = 'w'
print(grid)
plt.show()

#plt.show()

