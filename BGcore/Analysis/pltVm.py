import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import glob
import sample.param as param
import sample.LINDAHLtune as t
import matplotlib.pyplot as plt
from itertools import product
import time
paramNEW= t.tune(param.nparam, param.cparamOLD, param.staticsyn, param.noise, param.staticsynNoise, param.connections)



x = (0,1,2)
ite = list(product(x,x))
fig, axes = plt.subplots(3, 3)
n = 0


plotD1 = True
plotD2 = True
plotFSN = True
plotGPI = True
plotGPTA = True
plotGPTI = True
plotSTN = True
plotALL = False

if plotD1:
    popD1 = paramNEW.pparam['D1']
    fD1 = '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/data/D1-15136-0.dat'
    D1dat = dict()
    V_m = []
    t = []
    deviceID = []

    strideD1 = popD1
    it = time.time()
    with open(fD1, 'r') as f:
            for count,line in enumerate(f,start=100):
                if count %strideD1 == 0:
                    l = line.split()
                    #print("--- Split took %s seconds ---" % (time.time() - start_time))
                    
                    
                    #t = t + [float(l[1])]
                    
                    t.append(float(l[1]))
                    V_m.append(float(l[2]))
                    #print("--- Append took %s seconds ---" % (time.time() - start_time))
                    #print("--- Total took %s seconds ---" % (time.time() - it))

    print('Done with D1')
    print("--- Total took %s seconds ---" % (time.time() - it))




    D1dat['V_m'] = V_m
    D1dat['t'] = t
    
    n = 0
    axes[ite[n]].plot(t, V_m)
    axes[ite[n]].set_title('D1')
    axes[ite[n]].set_xlabel('time (s)')
    axes[ite[n]].set_ylabel('V_m (mV)')
    axes[ite[n]].set_ylim((-100,10))
    
    

#print(D1dat) 

#plt.plot(D1dat['t'][::10],D1dat['V_m'][::10])
#plt.show()


if plotD2:
    popD2 = paramNEW.pparam['D2']
    fD2 = '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/data/D2-15137-0.dat'
    D2dat = dict()
    V_m = []
    t = []
    deviceID = []
    strideD2 = popD2
    it = time.time()
    with open(fD2, 'r') as f:
            for count,line in enumerate(f,start=150):
                if count %strideD2 == 0:
                    l = line.split()
                    #deviceID = deviceID + [float(l[0])]
                    t.append(float(l[1]))
                    V_m.append(float(l[2]))

               	


    print('Done with D2')
    print("--- Total took %s seconds ---" % (time.time() - it))

    D2dat['V_m'] = V_m
    D2dat['t'] = t
    
    n = 1
    axes[ite[n]].plot(t, V_m)
    axes[ite[n]].set_title('D2')
    axes[ite[n]].set_xlabel('time (s)')
    axes[ite[n]].set_ylabel('V_m (mV)')
    axes[ite[n]].set_ylim((-100,10))


if plotFSN:
    popFSN = paramNEW.pparam['FSN']
    fFSN = '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/data/FSN-15143-0.dat'
    FSNdat = dict()
    V_m = []
    t = []
    deviceID = []
    strideFSN = popFSN
    it = time.time()
    with open(fFSN, 'r') as f:
            for count,line in enumerate(f,start=100):
                if count %strideFSN == 0:
                	l = line.split()
                	
                	t.append(float(l[1]))
                	V_m.append(float(l[2]))


    FSNdat['V_m'] = V_m
    FSNdat['t'] = t
    

    print('Done with FSN')
    print("--- Total took %s seconds ---" % (time.time() - it))
    n = 2
    axes[ite[n]].plot(t, V_m)
    axes[ite[n]].set_title('FSN')
    axes[ite[n]].set_xlabel('time (s)')
    axes[ite[n]].set_ylabel('V_m (mV)')
    axes[ite[n]].set_ylim((-100,10))



if plotGPI:
    popGPI = paramNEW.pparam['GPI']
    fGPI = '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/data/GPI-15139-0.dat'
    GPIdat = dict()
    V_m = []
    t = []
    deviceID = []
    it = time.time()
    strideGPI = popGPI
    with open(fGPI, 'r') as f:
            for count,line in enumerate(f,start=0):
                if count %strideGPI == 0:
                    l = line.split()
                    
                    t.append(float(l[1]))
                    V_m.append(float(l[2]))

    print('Done with GPI')
    print("--- Total took %s seconds ---" % (time.time() - it))
    GPIdat['V_m'] = V_m
    GPIdat['t'] = t
    
    n = 3
    axes[ite[n]].plot(t, V_m)
    axes[ite[n]].set_title('GPI')
    axes[ite[n]].set_xlabel('time (s)')
    axes[ite[n]].set_ylabel('V_m (mV)')
    axes[ite[n]].set_ylim((-100,10))



if plotGPTA:
    popGPTA = paramNEW.pparam['GPTA']
    fGPTA = '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/data/GPTA-15140-0.dat'
    GPTAdat = dict()
    V_m = []
    t = []
    deviceID = []
    strideGPTA = popGPTA
    it = time.time()
    with open(fGPTA, 'r') as f:
            for count,line in enumerate(f,start=0):
                if count %strideGPTA == 0:
                    l = line.split()
                    
                    t.append(float(l[1]))
                    V_m.append(float(l[2]))


    print('Done with GPTA')
    print("--- Total took %s seconds ---" % (time.time() - it))
    GPTAdat['V_m'] = V_m
    GPTAdat['t'] = t
    
    n = 4
    axes[ite[n]].plot(t, V_m)
    axes[ite[n]].set_title('GPTA')
    axes[ite[n]].set_xlabel('time (s)')
    axes[ite[n]].set_ylabel('V_m (mV)')
    axes[ite[n]].set_ylim((-100,10))



if plotGPTI:

    popGPTI = paramNEW.pparam['GPTI']
    fGPTI = '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/data/GPTI-15141-0.dat'
    GPTIdat = dict()
    V_m = []
    t = []
    deviceID = []
    strideGPTI = popGPTI
    it = time.time()
    with open(fGPTI, 'r') as f:
            for count,line in enumerate(f,start=0):
                if count %strideGPTI == 0:
                    l = line.split()
                    
                    t.append(float(l[1]))
                    V_m.append(float(l[2]))



    print('Done with GPTI')
    print("--- Total took %s seconds ---" % (time.time() - it))
    GPTIdat['V_m'] = V_m
    GPTIdat['t'] = t
    
    n = 5
    axes[ite[n]].plot(t, V_m)
    axes[ite[n]].set_title('GPTI')
    axes[ite[n]].set_xlabel('time (s)')
    axes[ite[n]].set_ylabel('V_m (mV)')
    axes[ite[n]].set_ylim((-100,10))


if plotSTN:
    popSTN = paramNEW.pparam['STN']
    fSTN = '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/data/STN-15138-0.dat'
    STNdat = dict()
    V_m = []
    t = []
    deviceID = []
    strideSTN = popSTN
    it = time.time()
    with open(fSTN, 'r') as f:
            for count,line in enumerate(f,start=0):
                if count %strideSTN == 0:
                    l = line.split()
                    
                    t.append(float(l[1]))
                    V_m.append(float(l[2]))


    print('Done with STN')
    print("--- Total took %s seconds ---" % (time.time() - it))
    STNdat['V_m'] = V_m
    STNdat['t'] = t
    
    n = 6
    axes[ite[n]].plot(t, V_m)
    axes[ite[n]].set_title('STN')
    axes[ite[n]].set_xlabel('time (s)')
    axes[ite[n]].set_ylabel('V_m (mV)')
    axes[ite[n]].set_ylim((-100,10))



plt.show()

if plotALL:
    V_M = dict()
    V_M['D1'] = D1dat['V_m']
    V_M['D2'] = D2dat['V_m']
    V_M['FSN'] = FSNdat['V_m']
    V_M['GPI'] = GPIdat['V_m']
    V_M['GTPA'] = GPTAdat['V_m']
    V_M['GTPI'] = GPTIdat['V_m']
    V_M['STN'] = STNdat['V_m']


    x = (0,1,2)
    it = list(product(x,x))
    fig, axes = plt.subplots(3, 3)
    n = 0
    for i in V_M:
    	V_m = V_M[i]

    	axes[it[n]].plot(D1dat['t'][::10], V_m[::10])
    	axes[it[n]].set_title(i)
    	axes[it[n]].set_xlabel('time (s)')
    	axes[it[n]].set_ylabel('V_m (mV)')
    	axes[it[n]].set_ylim((-100,10))
    	n = n + 1


    fig.set_dpi(70)
    fig.set_size_inches(8, 6)
    plt.subplots_adjust(hspace = 0.5, wspace = 0.5)
    plt.show()

