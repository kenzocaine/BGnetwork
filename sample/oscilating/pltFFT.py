import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")

import pandas as pd
import pandas.stats.var as var
from scipy.fftpack import fft
from scipy.signal import periodogram as pd
import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.stattools import grangercausalitytests as gt
# Number of sample points
N = 1000/1
# sample spacing
T = 1e-3
GPTI = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/oscilating/data/GPTI-15149-0.gdf')
STN = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/oscilating/data/STN-15146-0.gdf')
ed = np.arange(0,1000,1)
STNp, yyed = np.histogram(STN[:,1], ed, range=None, normed=None, weights=None, density=None)
#print(yy)
fp,yp = pd(STNp, 1/T,'hamming', scaling= 'spectrum', nfft = 32)
#xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
#print(int(N//2)
#plt.plot(xf, 2.0/N * np.abs(yf[0:int(N//2)]))
plt.figure(1)
plt.plot(fp,np.log10(yp))
plt.plot(fp,np.log10(45*1/fp))
plt.grid()
plt.title('STN')

plt.figure(2)
plt.subplot(712)
GPTIp, yyed = np.histogram(GPTI[:,1], ed, range=None, normed=None, weights=None, density=None)
fp,yp = pd(GPTIp, 1/T,'hamming')
plt.plot(fp,np.log1p(yp))
plt.title('GPTI')

#data = np.concatenate((GPTIp.T, STNp.T), axis=1)

D2 = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/oscilating/data/D2-15145-0.gdf')

plt.subplot(713)
D2p, yyed = np.histogram(D2[:,1], ed, range=None, normed=None, weights=None, density=None)
fp,yp = pd(D2p, 1/T,'hamming',scaling='spectrum')
plt.plot(fp,np.log10(yp))
plt.title('D2')


D1 = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/oscilating/data/D1-15144-0.gdf')
plt.subplot(714)
D1p, yyed = np.histogram(D1[:,1], ed, range=None, normed=None, weights=None, density=None)
fp,yp = pd(D1p, 1/T,'hamming')
plt.plot(fp,np.log10(yp))
plt.title('D1')


FSN = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/oscilating/data/FSN-15150-0.gdf')
plt.subplot(715)
FSNp, yyed = np.histogram(FSN[:,1], ed, range=None, normed=None, weights=None, density=None)
fp,yp = pd(FSNp, 1/T,'hamming')
plt.plot(fp,np.log10(yp))
plt.title('FSN')



GPTA = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/oscilating/data/GPTA-15148-0.gdf')
plt.subplot(716)
GPTAp, yyed = np.histogram(GPTA[:,1], ed, range=None, normed=None, weights=None, density=None)
fp,yp = pd(GPTAp, 1/T,'hamming')
plt.plot(fp,np.log10(yp))
plt.title('GPTA')



GPI = np.loadtxt('/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/oscilating/data/GPI-15147-0.gdf')
plt.subplot(717)
GPIp, yyed = np.histogram(GPI[:,1], ed, range=None, normed=None, weights=None, density=None)
fp,yp = pd(GPIp, 1/T,'hamming')
plt.plot(fp,np.log10(yp))
plt.title('GPI')



#data = np.concatenate((GPTI.T[0:10], STN.T[0:10]), axis=-1)
data = np.array([GPTIp, STNp])

#testnull = gt(GPTIp,-1)
#print(testnull)
var.VAR.granger_causality
#plt.subplot(714)
f, Cxy = signal.coherence(GPTIp, STNp, 1/T)
#plt.semilogy(f, Cxy)
#plt.xlabel('frequency [Hz]')
#plt.ylabel('Coherence')
#
#
plt.figure(2)

plt.plot(GPTAp)
plt.show()

#plt.show()

