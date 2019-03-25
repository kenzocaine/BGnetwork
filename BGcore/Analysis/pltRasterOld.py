import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import glob
import numpy as np
import sample.param as param
import sample.LINDAHLtune as t
import matplotlib.pyplot as plt
from itertools import product
import time


x = (0,1,2)
ite = list(product(x,x))
#fig, axes = plt.subplots(3, 3)
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
    fD1 = '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/data/GPTA-15148-0.gdf'
    D1dat = dict()
    
    t = []
    neuronID = []
    it = time.time()

    with open(fD1, 'r') as f:
            for line in f:
                l = line.split()
                neuronID.append(float(l[0]))
                t.append(float(l[1]))


    print('Done with D1')
    print("--- Total took %s seconds ---" % (time.time() - it))


    n = 0
    #axes[ite[n]].plot(t[::500], neuronID[::500],'.')
    #axes[ite[n]].set_title('D1')
    #axes[ite[n]].set_xlabel('time (s)')
    #axes[ite[n]].set_ylabel('V_m (mV)')

window = 10.0
spike_count = 0 # spike count per window
uniqueID = set()
startime = t[0]

listcount = []
average =[]
averagef = []
for c,i in enumerate(t):
	if i < window + startime:
		spike_count = spike_count + 1 
		#print(spike_count)
		uniqueID.add(neuronID[c])
		#print(neuronID[c])

	else:
		listcount.append(spike_count)
		#print(spike_count)
		#print(len(uniqueID))
		average.append(spike_count/float(len(uniqueID)))
		averagef.append(spike_count/(window))
		#print(average)
		spike_count = 1
		uniqueID = set()
		uniqueID.add(neuronID[c])
		startime = i


print(listcount)
#rint(listcount)
#print(average)


plt.bar(np.linspace(0,1000,len(averagef)),np.array(averagef),width=20)
plt.show()



#plt.show()