import matplotlib.pyplot as plt
import nest
from param import nparam
from itertools import product

def set_nparam(neuron, nparam, name):
    p = nparam[name]
    if name in ["GPTA","GPTI","STN","GPI"]: # Test if adaptive integrate and fire
        for i in p:
            if i not in ["t_f","beta_E_L"]:
                nest.SetStatus(neuron, {i : float(p[i])})
    else:
        for i in p:
            nest.SetStatus(neuron, {i: float(p[i])})

  

def simN(I_e):
    
    
    nest.SetStatus(GPTA, {"I_e": I_e})
    nest.SetStatus(GPTI, {"I_e": I_e})
    nest.SetStatus(STN, {"I_e": I_e})
    nest.SetStatus(GPI, {"I_e": I_e})
    nest.SetStatus(FSN, {"I_e": I_e})
    nest.SetStatus(D1, {"I_e": I_e})
    nest.SetStatus(D2, {"I_e": I_e})
    




    nest.Simulate(1000.0)


def plotAll():
    x = (0,1,2)
    it = list(product(x,x))
    names = ["GPTA", "GPTI","STN","GPI","D1","D2","FSN"]
    dmm = nest.GetStatus(multimeter)[0]
    fig, axes = plt.subplots(3, 3)
    for i in range(7):
        Vms = dmm["events"]["V_m"][i::7]
        ts = dmm["events"]["times"][i::7]
        axes[it[i]].plot(ts, Vms)
        axes[it[i]].set_title(names[i])
        axes[it[i]].set_xlabel('ms')
        axes[it[i]].set_ylabel('Vm')
    fig.set_dpi(70)
    fig.set_size_inches(8, 6)
    plt.subplots_adjust(hspace = 0.5, wspace = 0.5)
    

if __name__ == '__main__':

    # Create point neurons
    # adaptive exponential iaf model
    GPTA = nest.Create("aeif_cond_exp")
    GPTI = nest.Create("aeif_cond_exp")
    STN = nest.Create("aeif_cond_exp")
    GPI = nest.Create("aeif_cond_exp")

    # alpha
    FSN = nest.Create("iaf_cond_alpha")
    D1 = nest.Create("iaf_cond_alpha")
    D2 = nest.Create("iaf_cond_alpha")

    # Set the point neuron parameter from Lindahl 2016
    set_nparam(GPTA,nparam,"GPTA")
    set_nparam(GPTI,nparam,"GPTI")
    set_nparam(STN,nparam,"STN")
    set_nparam(GPI,nparam,"GPI")
    set_nparam(FSN,nparam,"FSN")
    set_nparam(D1,nparam,"D1")
    set_nparam(D2,nparam,"D2")

    multimeter = nest.Create("multimeter")
    nest.SetStatus(multimeter, {"withtime":True, "record_from":["V_m"]})

    # Connect neurons to multimeter
    nest.Connect(multimeter, GPTA)
    nest.Connect(multimeter, GPTI)
    nest.Connect(multimeter, STN)
    nest.Connect(multimeter, GPI)
    nest.Connect(multimeter, D1)
    nest.Connect(multimeter, D2)
    nest.Connect(multimeter, FSN)

    nest.Connect(GPTA, spikedetector)
    nest.Connect(GPTI, spikedetector)
    nest.Connect(STN, spikedetector)
    nest.Connect(GPI, spikedetector)
    nest.Connect(D1, spikedetector)
    nest.Connect(D2, spikedetector) 
    nest.Connect(FSN, spikedetector)

    I_e = [5*i for i in range(10)]
    for i in I_e:
        simN(float(i))
        #plotAll()
        nest.ResetNetwork()
    #plt.show()
