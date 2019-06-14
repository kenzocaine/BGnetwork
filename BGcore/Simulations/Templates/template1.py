import sys
import os
# Always specify the path of your working environment
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/") 

# Import the base modules BGnodes and BGnetwork (or just BGnodes if you wish not connect anything in your setup)
import BGcore.Model.BGnodes
from BGcore.Model.BGnetwork import BGnetwork
# Import the param.py file of your choosing
import BGcore.Simulations.BasalFiring.paramtest8 as param # Desired parameters
# Import nest
import nest

# Import aditional libraries of your choosing 
import matplotlib.pyplot as plt
import time
import numpy as np



class myclass(BGnetwork):
	def __init__(self,nparam,cparam,synparam, noise,synparamNoise, connections, pparam=True):
		# All arguments are sent to the parent class BGnetwork
		super().__init__(nparam,cparam,synparam, noise, synparamNoise, connections, pparam)


	def myMethod(self):
		return
		# Here you can specify any function using the nest library, specific to your setup





# Start by reseting the kernel. Always perform this operation before creating any new class
nest.ResetKernel()

# Create a class with chosen parameters from param. Do NOT create more than one class since NEST can only simulate one set-up at a given time
# If you want to create an aditional class with different parameters make sure to reset the kernel and specify a new path for your data to be writen
# Do all this AFTER you have simulated the first class if you don't wanna loose any changes. 
mySetup1 = myclass(param.nparam, param.cparam, param.staticsyn, param.noise,param.staticsynNoise, param.connections,param.pparam)

# Specify folder where data should be writen to
nest.SetKernelStatus({'data_path': '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/BGcore/variableBG/data/', 'overwrite_files':True})

# Connect spike detector and set Ie to 0
mySetup1.connectSpikeDet()
mySetup1.setIe(0.0)

# Perform any other operation on the class based on what methods you specified
# You can put any operation in a loop, for example changing the poisson rate for a specific node
# 

# Simulate
mySetup1.simulate(1000.0)
