# Connectivity state. "Destination neuron" : { "Source neurons"}
state = {
"D1": {"D1": 1,"D2":1,"FSN":1,"GPTA":0,"GPTI":0,"STN":0,"CTX":1},
"D2": {"D1": 1,"D2":1,"FSN":1,"GPTA":0,"GPTI":0,"STN":0,"CTX":1},
"GPTA": {"D1": 0,"D2":0,"FSN":0,"GPTA":1,"GPTI":1,"STN":1,"CTX":0},
"GPTI": {"D1": 0,"D2":1,"FSN":0,"GPTA":1,"GPTI":1,"STN":1,"CTX":0},
"STN": {"D1": 0,"D2":0,"FSN":0,"GPTA":0,"GPTI":1,"STN":0,"CTX":1},
"FSN": {"D1": 0,"D2":0,"FSN":1,"GPTA":1,"GPTI":1,"STN":0,"CTX":1},
"GPI": {"D1": 1,"D2":0,"FSN":0,"GPTA":0,"GPTI":1,"STN":1,"CTX":1},
"drawAll": {"D1": 1,"D2":1,"FSN":1,"GPTA":1,"GPTI":1,"STN":1,"CTX":0},
}

sc = 0.1
sc2 = 0.1
start = 0.0
stop = 50000.0
noise = {

            'D1' : {'rate' : 2500.0, 'start':start,'stop':stop},
            'D2' : {'rate' : 2500.0, 'start':start,'stop':stop},
            'FSN' : {'rate' : 850.0, 'start':start,'stop':stop},
            'STN' : {'rate' : 200.0, 'start':start,'stop':stop},
            'GPTA' : {'rate' : 60.0, 'start':start,'stop':stop},
            'GPTI' : {'rate' : 600.0, 'start':start,'stop':stop},
            'GPI' : {'rate' : 380.0, 'start':start,'stop':stop}
}

STRinputH = 1.5
STRinputL = 1.4
# D1 = 2-5 Hz need 400-580 Hz with 1.5 weight, 
# D2 = 2-5 Hz --> 400-550 Hz, 
# GPTA = <5-10 Hz, (8 Hz lindahl)  need 60 Hz
# GPTI = 30-50 Hz (18 Hz lindahl),  need 400 Hz
# STN = 20 Hz,  need around 380 Hz
# GPI = 30 Hz (20-35 Hz Lindahl) need around 300 -400 Hz
# FSN = 10-20 Hz need 450 Hz with g_L=12.5, and 850 with g_L= 20 
staticsynNoise = {
            'D1' : {'weight' : {'distribution': 'uniform', 'low': STRinputL, 'high': STRinputH},'delay':1},
            'D2' : {'weight' : {'distribution': 'uniform', 'low': STRinputL, 'high': STRinputH},'delay':1},
            'FSN' : {'weight' : {'distribution': 'uniform', 'low': STRinputL, 'high': STRinputH},'delay':1},
            'STN' : {'weight' : {'distribution': 'uniform', 'low': 1.0, 'high': 1.1},'delay':1},
            'GPTA' : {'weight' : {'distribution': 'uniform', 'low': 0.5, 'high': 0.8},'delay':1},
            'GPTI' : {'weight' : {'distribution': 'uniform', 'low': 2.0, 'high': 2.8},'delay':1},
            'GPI' : {'weight' : {'distribution': 'uniform', 'low': 1.4, 'high': 1.5},'delay':1}
}


connections = {
"D1": {"D1": 1,"D2":1,"FSN":1,"GPTA":0,"GPTI":0,"STN":0,"CTX":1},
"D2": {"D1": 1,"D2":1,"FSN":1,"GPTA":0,"GPTI":0,"STN":0,"CTX":1},
"GPTA": {"D1": 0,"D2":0,"FSN":0,"GPTA":1,"GPTI":1,"STN":1,"CTX":0},
"GPTI": {"D1": 0,"D2":1,"FSN":0,"GPTA":1,"GPTI":1,"STN":1,"CTX":0},
"STN": {"D1": 0,"D2":0,"FSN":0,"GPTA":0,"GPTI":1,"STN":0,"CTX":1},
"FSN": {"D1": 0,"D2":0,"FSN":1,"GPTA":1,"GPTI":1,"STN":0,"CTX":1},
"GPI": {"D1": 1,"D2":0,"FSN":0,"GPTA":0,"GPTI":1,"STN":1,"CTX":1},
}


staticsyn = {
                "D1" : {
                        "D1" : {"weight" : -0.15, "delay" : 1.7},
                        "D2" : {"weight" : -0.45, "delay" : 1.7} , 
                        "FSN" : {"weight" : -6.0, "delay" : 1.7}, 
                        "GPTA" : {"weight" : -0.04, "delay" : 7.0},
                        "GPTI" : {"weight" : -0.04, "delay" : 7.0},
                        "STN" : {"weight" : 1.0, "delay" : 1.0},
                        "GPI" : {"weight" : -1.0, "delay" : 1.0}
                        }, 

                "D2" :  {
                        "D1" : {"weight" : -0.375, "delay" : 1.7},
                        "D2" : {"weight" : -0.35, "delay" : 1.7} , 
                        "FSN" : {"weight" : -6.0, "delay" : 1.7}, 
                        "GPTA" : {"weight" : -0.08, "delay" : 7.0},
                        "GPTI" : {"weight" : -0.08, "delay" : 7.0},
                        "STN" : {"weight" : 1.0, "delay" : 1.0},
                        "GPI" : {"weight" : -1.0, "delay" : 1.0}
                        },

                "GPTA" : {
                        "D1" : {"weight" : -1.0, "delay" : 1.0},
                        "D2" : {"weight" : -1.0, "delay" : 1.0},
                        "FSN" : {"weight" : -1.0, "delay" : 1.0},
                        "GPTA" : {"weight" : -0.33, "delay" : 1.0},
                        "GPTI" : {"weight" : -0.33, "delay" : 1.0},
                        "STN" : {"weight" : 0.11, "delay" : 2.0},
                        "GPI" : {"weight" : -1.0, "delay" : 1.0}
                        },

                "GPTI" : {
                        "D1" : {"weight" : -1.0, "delay" : 1.0},
                        "D2" : {"weight" : -2.0, "delay" : 7.0},
                        "FSN" : {"weight" : -1.0, "delay" : 1.0},
                        "GPTA" : {"weight" : -1.3, "delay" : 1.0},
                        "GPTI" : {"weight" : -1.3, "delay" : 1.0},
                        "STN" : {"weight" : 0.35, "delay" : 2.0},
                        "GPI" : {"weight" : -1.0, "delay" : 1.0}
                        },

                "STN" : {
                        "D1" : {"weight" : -1.0, "delay" : 1.0},
                        "D2" : {"weight" : -1.0, "delay" : 1.0} , 
                        "FSN" : {"weight" : -1.0, "delay" : 1.0}, 
                        "GPTA" : {"weight" : -1.0, "delay" : 1.0},
                        "GPTI" : {"weight" : -0.08, "delay" : 1.0},
                        "STN" : {"weight" : 1.0, "delay" : 1.0},
                        "GPI" : {"weight" : -1.0, "delay" : 1.0}
                        },

                "FSN" : {
                        "D1" : {"weight" : -1.0, "delay" : 1.0},
                        "D2" : {"weight" : -1.0, "delay" : 1.0} , 
                        "FSN" : {"weight" : -1.0, "delay" : 1.7}, 
                        "GPTA" : {"weight" : -0.51, "delay" : 7.0},
                        "GPTI" : {"weight" : -2.0, "delay" : 7.0},
                        "STN" : {"weight" : 1.0, "delay" : 1.0},
                        "GPI" : {"weight" : -1.0, "delay" : 1.0}
                        },

                "GPI" :  {
                        "D1" : {"weight" : - 2.0, "delay" : 7.0},
                        "D2" : {"weight" : -1.0, "delay" : 1.0} , 
                        "FSN" : {"weight" : -1.0, "delay" : 1.0}, 
                        "GPTA" : {"weight" : -76.0, "delay" : 3.0},
                        "GPTI" : {"weight" : -76.0, "delay" : 3.0},
                        "STN" : {"weight" : 0.91, "delay" : 4.5},
                        "GPI" : {"weight" : -1.0, "delay" : 1.0}
                        }
            }




cparamOLD1 = {"D1" : {"D1" : 364, "D2" : 392, "FSN" : 16, "GPTA" : 10 }, 
             "D2" : {"D1" : 84, "D2" : 504, "FSN": 11, "GPTA" : 10 }, 
             "FSN" : {"FSN" : 10, "GPTA" : 10, "GPTI" : 10 },
             "STN" : {"GPTI" : 30},
             "GPTA" : {"STN" : 30, "GPTA" : 5, "GPTI" : 25 },
             "GPTI" : { "STN": 30,"D2" : 500, "GPTI" : 25, "GPTA" : 5},
             "GPI" : { "GPTI" : 32, "D1" : 500, "STN" : 30} }

#synparam = {"D1" : {"D1" : {"g": , "tau": }, "D2" : {"g": , "tau": }, "FSN" : {"g": , "tau": }, "GPTA" : {"g": , "tau": } }, 
#             "D2" : {"D1" : {"g": , "tau": }, "D2" : {"g": , "tau": }, "FSN": {"g": , "tau": }, "GPTA" : {"g": , "tau": } }, 
#             "FSN" : {"FSN" : {"g": , "tau": }, "GPTA" : {"g": , "tau": }, "GPTI" : {"g": , "tau": } },
#             "STN" : {"GPTI" : {"g": , "tau": }},
#             "GPTA" : {"STN" : {"g": , "tau": }, "GPTA" :{"g": , "tau": }, "GPTI" : {"g": , "tau": } },
#             "GPTI" : { "STN": {"g": , "tau": },"D2" : {"g": , "tau": }, "GPTI" : {"g": , "tau": }, "GPTA" :{"g": , "tau": }},
#             "GPI" : { "GPTI" : {"g": , "tau": }, "D1" : {"g": , "tau": }, "STN" : {"g": , "tau": }} 
#             }




cparamOLD = {
    'P_n' : 80000,
    'P_D1' : 37971,
    'P_D2' : 37971,
    'P_FSN' : 1599,
    'P_STN' : 388,
    'P_GPTA' : 329,
    'P_GPTI' : 988,
    'P_GPI' : 754,
    'C_D1_D1' : 364,
    'C_D1_D2' : 84,
    'C_D2_D1' : 392,
    'C_D2_D2' : 504,
    'C_FSN_D1' : 16,
    'C_FSN_D2' : 11,
    'C_GPTA_D1' : 10,
    'C_GPTA_D2' : 10,
    'C_FSN_FSN' : 10,
    'C_GPTA_FSN' : 10,
    'C_GPTI_FSN' : 10,
    'C_GPTI_GPI' : 32,
    'C_D1_GPI' : 500,
    'C_STN_GPI' : 30,
    'C_D2_GPTI' : 500,
    'C_STN_GPTA' : 30,
    'C_STN_GPTI' : 30,
    'C_GPTA_GPTA' : 5,
    'C_GPTA_GPTI' : 5,
    'C_GPTI_GPTA' : 25,
    'C_GPTI_GPTI' : 25,
    'C_GPTI_STN' : 30,
    'tauD2_GPTI' : 6,
    'gD2_GPTI' : 2,
    'tauD2_D1' : 8,
    'gD2_D1' : 0.45,
    'tauD1_D2' : 8,
    'gD1_D2' : 0.375,
    'tauD1_D1' : 8,
    'gD1_D1' : 0.15,
    'tauD2_D2' : 8,
    'gD2_D2' : 0.35,
    'tauD1_GPI' : 5.2,
    'gD1_GPI' : 2,
    'gFSN_D1' : 2, # Correct these and below
    'gFSN_FSN' : 2,
    'gFSN_D2' : 2,
    'tauFSN_D1' : 8,
    'tauFSN_FSN' : 8,
    'tauFSN_D2' : 8,
    'lMSN' : 1,

}

nparam = {
"GPTI" : {"a" : 2.5, "b" : 70.0, "Delta_T" : 1.7, "tau_w": 20.0,
          "E_L": -55.1, "g_L": 1.0,  "C_m": 40.0,"I_e":12.0, "V_peak":15.0,
            "V_reset": -60.0, "V_th": -54.7,
            "tau_syn_ex":2.0, "tau_syn_in":2.0 },
"GPTA" : {"a" : 2.5, "b" : 105.0, "Delta_T" : 2.55, "tau_w": 20.0,
          "E_L": -55.1, "g_L": 1.0,  "C_m": 60.0,"I_e":1.0, "V_peak":15.0,
            "V_reset": -60.0, "V_th": -54.7,
            "tau_syn_ex":2.0, "tau_syn_in":2.0 },
"GPI" : {"a" : 3.0, "b" : 200.0, "Delta_T" : 1.8, "tau_w": 20.0,
          "E_L": -55.8, "g_L": 3.0,  "C_m": 80.0,"I_e":15.0, "V_peak":20.0,
            "V_reset": -65.0, "V_th": -55.2,
            "tau_syn_ex":2.0, "tau_syn_in":2.0 },
"STN" : {"a" : 0.3, "b" : 0.05, "Delta_T" : 16.2, "tau_w": 333.0,
          "E_L": -80.2, "g_L": 10.0, "C_m": 60.0, "I_e":5.0,
            "V_reset": -70.0, "V_th": -64.0, "V_peak": 15.0,
            "tau_syn_ex":2.0, "tau_syn_in":2.0
            },
# West2016 param "FSN" : {"a" : 0.2, "b" : 0.025, "c": -60, "C_m" : 80, "d": 0, "k": 1,
#            "beta_V_r": -0.078, "v_b": -55, "v_peak": 25, "v_reset": -64, "v_th" : -50}
"FSN" : {"V_m" : -80.0, "E_ex" : 0.0, "E_in": -76.0, "V_th": -50.0, "tau_syn_ex":2.0, "tau_syn_in":2.0,
            "C_m": 80.0, "g_L": 20.0, "I_e" : 500.0,"E_L":-80.0},
"D1" : {"V_m" : -80.0, "E_ex" : 0.0, "E_in": -64.0, "V_th": -29.7, "tau_syn_ex":2.0, "tau_syn_in":2.0,
            "C_m": 200.0, "g_L": 12.5, "I_e":350.0,"E_L":-80.0},
"D2" : {"V_m" : -80.0, "E_ex" : 0.0, "E_in": -64.0, "V_th": -29.7, "tau_syn_ex":2.0, "tau_syn_in":2.0,
            "C_m": 200.0, "g_L": 12.5, "I_e": 350.0,"E_L":-80.0}
}
