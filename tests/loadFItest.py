import pickle
import matplotlib.pyplot as plt
from itertools import product

with open('FI.dat','rb') as f:  # Python 3: open(..., 'rb')
    I_e, F = pickle.load(f)


x = (0,1,2)
it = list(product(x,x))
fig, axes = plt.subplots(3, 3)
n = 0
for i in F:
	freq = F[i]

	axes[it[n]].plot(I_e, freq)
	axes[it[n]].set_title(i)
	axes[it[n]].set_xlabel('I_e (A)')
	axes[it[n]].set_ylabel('Frequency (Hz)')
	n = n + 1


fig.set_dpi(70)
fig.set_size_inches(8, 6)
plt.subplots_adjust(hspace = 0.5, wspace = 0.5)
plt.show()