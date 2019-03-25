import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")

import pandas as pd
import pandas.stats.var as var
from scipy.fftpack import fft
from scipy.signal import periodogram as pd
import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np


# Number of sample points
N = 1000/1
# sample spacing
T = 1e-3
GPTI = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/BasalFiring/data/GPTI-15149-0.gdf')
STN = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/BasalFiring/data/STN-15146-0.gdf')
ed = np.arange(0,1000,1)
STNp, yyed = np.histogram(STN[200:,1], ed, range=None, normed=None, weights=None, density=None)
#print(yy)
fp,yp = pd(STNp, 1/T,'hann')
#xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
#print(int(N//2)
#plt.plot(xf, 2.0/N * np.abs(yf[0:int(N//2)]))
plt.subplot(711)
plt.plot(fp,np.log10(yp))
plt.grid()
plt.title('STN')

plt.subplot(712)
GPTIp, yyed = np.histogram(GPTI[200:,1], ed, range=None, normed=None, weights=None, density=None)
fp,yp = pd(GPTIp, 1/T,'hann')
plt.plot(fp,np.log10(yp))
plt.title('GPTI')

#data = np.concatenate((GPTIp.T, STNp.T), axis=1)

D2 = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/BasalFiring/data/D2-15145-0.gdf')

plt.subplot(713)
D2p, yyed = np.histogram(D2[200:,1], ed, range=None, normed=None, weights=None, density=None)
fp,yp = pd(D2p, 1/T,'hann')
plt.plot(fp,np.log10(yp))
plt.title('D2')


D1 = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/BasalFiring/data/D1-15144-0.gdf')
plt.subplot(714)
D1p, yyed = np.histogram(D1[200:,1], ed, range=None, normed=None, weights=None, density=None)
fp,yp = pd(D1p, 1/T,'hann')
plt.plot(fp,np.log10(yp))
plt.title('D1')


FSN = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/BasalFiring/data/FSN-15150-0.gdf')
plt.subplot(715)
FSNp, yyed = np.histogram(FSN[200:,1], ed, range=None, normed=None, weights=None, density=None)
fp,yp = pd(FSNp, 1/T,'hann')
plt.plot(fp,np.log10(yp))
plt.title('FSN')



GPTA = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/BasalFiring/data/GPTA-15148-0.gdf')
plt.subplot(716)
GPTAp, yyed = np.histogram(GPTA[200:,1], ed, range=None, normed=None, weights=None, density=None)
fp,yp = pd(GPTAp, 1/T,'hann')
plt.plot(fp,np.log10(yp))
plt.title('GPTA')



GPI = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/BasalFiring/data/GPI-15147-0.gdf')
plt.subplot(717)
GPIp, yyed = np.histogram(GPI[200:,1], ed, range=None, normed=None, weights=None, density=None)
fp,yp = pd(GPIp, 1/T,'hann')
plt.plot(fp,np.log10(yp))
plt.title('GPI')

plt.show()