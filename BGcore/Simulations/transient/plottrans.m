clear all
path = '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/BGcore/Simulations/transient/data3/';
%path = fullfile(root(n).folder,root(n).name)

[dataX, dataY] = loadtrans(path);
nbins = 1500;
%%
subplot(6,1,1)
STNh = histogram(dataX.STN,nbins);
STNz=zscore(STNh.Values);
STN = STNh.Values;
title('STN')


subplot(6,1,2)
GPTIh = histogram(dataX.GPTI,nbins);
GPTI = GPTIh.Values;
GPTIz=zscore(GPTIh.Values);
title('GPTI')
%zoom(1.5)

subplot(6,1,3)
GPTAh = histogram(dataX.GPTA,nbins);
GPTA = GPTAh.Values;
GPTAz=zscore(GPTAh.Values);
title('GPTA')

subplot(6,1,4)
D1h = histogram(dataX.D1,nbins);
D1 = D1h.Values;
D1z=zscore(D1h.Values);
title('D1')

subplot(6,1,5)
D2h = histogram(dataX.D2,nbins);
D2 = D2h.Values;
D2z=zscore(D2h.Values);
title('D2')

subplot(6,1,6)
GPIh = histogram(dataX.GPI,nbins);
GPI = GPIh.Values;
GPIz=zscore(GPIh.Values);
title('GPI')
%%
[xc,lags] = xcorr(STN(100:900)-mean(STN),GPTI(100:900)-mean(GPTI),'coeff');
stem(lags,xc)