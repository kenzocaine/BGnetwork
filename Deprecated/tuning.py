for i in NSTR:
        for v in N:
            if v[0:4] == i[0:4]: # If the source matches
                m = 5000
                if v[0:4] in ['N_FS']:
                    m = cparamOLD['N_FSN']/cparamOLD['N_D1']  *5000# Maybe scale down the number of FSN too  <--- subject to change

                connectP = cparamOLD[v]/cparamOLD[i] # connection probability

                N_Cnew = connectP * m

                var = cparamOLD[v] * cparamOLD['lMSN'] * cparamOLD['g'+v[2:]]**2 *cparamOLD['tau'+v[2:]] * np.exp(2) / 4

                mean = cparamOLD[v] * cparamOLD['lMSN'] * cparamOLD['g'+v[2:]] *cparamOLD['tau'+v[2:]] * np.exp(1)

                gNEW = mean / (N_Cnew * cparamOLD['lMSN'] * cparamOLD['tau'+v[2:]] * np.exp(1))

                cparam['g'+v[2:]] = gNEW
                cparam[v] = np.round(N_Cnew)
                #print(gNEW)

                #print('g: ',gNEW)
                #print('n_c: ',N_Cnew)
                #print(v,i)