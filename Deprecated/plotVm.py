def plotVm(network):

	x = (0,1,2)
	it = list(product(x,x))
	names = ["GPTA", "GPTI","STN","GPI","D1","D2","FSN"]
	
	fig, axes = plt.subplots(3, 3)
	for i in range(7):
	    
	    axes[it[i]].plot(network.vm[names[i]]["t"], network.vm[names[i]]["Vm"])
	    axes[it[i]].set_title(names[i])
	    axes[it[i]].set_xlabel('ms')
	    axes[it[i]].set_ylabel('Vm')
	fig.set_dpi(70)
	fig.set_size_inches(8, 6)
	plt.subplots_adjust(hspace = 0.5, wspace = 0.5)
	plt.show()