import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import numpy as np
import copy
import matplotlib.pyplot as plt
import sample.tls as tls
from sample.oscilating.paramtest7 import state
import sample.oscilating.paramtest7 as param

def drawN(typeN, cparam,x,y,sc,pparam, synparam,noise, averageVm = True):
    # type of Neuron to be draw. Needs to be a string
    # cparam: connectivity cparameters as a dictionary
    # sc : scaling (if doing multiploting)
    # x,y: position




    def label(x,y, text,N):
          # shift y-value for label so that it's below the artist
        plt.text(x, y, str(text)+'='+str(N), ha="center", family='sans-serif',size=14*sc)
    def labelWeight(x,y,weight):
        plt.text(x, y, 'w ='+str(weight), ha="center", family='sans-serif',size=14*sc)
    def labelout(x,y,averageVm):
        plt.text(x, y, str(averageVm)+' mV', ha="center", family='sans-serif',size=14*sc)

    def labelRate(x,y,rate, TYPE):
        plt.text(x, y, TYPE+' ='+str(rate)+' Hz', ha="center", family='sans-serif',size=14*sc)

    def drawLine(SOURCE,x,y,length,r,linewidth,deg,colour,facecolor,N,weight):

        angle = deg * np.pi / 180

        xmin = r
        xmax = r+length
        ymin = 0
        ymax = 0
        rotxmin = xmin*np.cos(angle)-ymin*np.sin(angle)
        rotxmax = xmax*np.cos(angle)-ymax*np.sin(angle)
        rotymin = xmin*np.sin(angle)+ymin*np.cos(angle)
        rotymax = xmax*np.sin(angle)+ymax*np.cos(angle)

        line = plt.Line2D((rotxmin+x, rotxmax + x), (rotymin + y, rotymax + y), lw=linewidth,
                                 ls='-', marker='.',
                                 markersize=14*np.sqrt(sc),
                                 markerfacecolor=facecolor,
                                 markeredgecolor=colour,
                                 markevery = 3,
                                 color=colour,
                                 alpha=1)
        plt.gca().add_line(line)
        degT = 3
        angleT = (deg-degT) * np.pi / 180

        xlab = length+0.09 + r
        ylab = 0

        rotxlab = xlab*np.cos(angleT)-ylab*np.sin(angleT)
        rotylab = xlab*np.sin(angleT)+ylab*np.cos(angleT)

        

        if SOURCE == 'D2':
            label(rotxlab+x,rotylab+y,SOURCE,N)
            degT = 9
            angleT = (deg-degT) * np.pi / 180
            xlab = length+0.08 + r
            ylab = 0

            rotxlab = xlab*np.cos(angleT)-ylab*np.sin(angleT)
            rotylab = xlab*np.sin(angleT)+ylab*np.cos(angleT)

            labelWeight(rotxlab+x,rotylab+y,weight)
        elif SOURCE in ['CTX', 'EXT']:
            degT = 3
            angleT = (deg-degT) * np.pi / 180
            xlab = length+0.08 + r
            ylab = 0

            rotxlab = xlab*np.cos(angleT)-ylab*np.sin(angleT)
            rotylab = xlab*np.sin(angleT)+ylab*np.cos(angleT)

            labelRate(rotxlab+x,rotylab+y,weight, SOURCE)

        else:
            label(rotxlab+x,rotylab+y,SOURCE,N)
            degT = 3
            angleT = (deg-degT) * np.pi / 180
            xlab = length+0.15 + r
            ylab = 0

            rotxlab = xlab*np.cos(angleT)-ylab*np.sin(angleT)
            rotylab = xlab*np.sin(angleT)+ylab*np.cos(angleT)

            labelWeight(rotxlab+x,rotylab+y,weight)









    #plt.axes()

# Draw the target node

    scale = 10/sc
    lout = 0.25
    length = 0.24
    r = 0.18*1/np.sqrt(sc)
    circle = plt.Circle((x, y), radius=r, facecolor='w',edgecolor='k')
    plt.gca().add_patch(circle)

    label(x,y,typeN,str(pparam[typeN]))




    

    w = 1/(sc**1)
    r = r+0.04*w

    s = state[typeN]
    outMeanVm = 0

    if s['D1']:
        TARGET = typeN
        SOURCE = 'D1'
       
        if typeN =='drawAll':
            linewidth = 3.
        else:
            linewidth = np.sqrt(cparam[TARGET][SOURCE])/scale

        
        deg = 90
        colour = 'b'
        facecolor = 'w'
        if averageVm == True:
            drawLine(SOURCE,x,y,length,r,linewidth,deg,colour,facecolor,str(cparam[TARGET][SOURCE]),str(synparam[TARGET][SOURCE]['weight']))
        else:
            drawLine(SOURCE,x,y,length,r,linewidth,deg,colour,facecolor,str(round(averageVm[TARGET][SOURCE],2)),str(synparam[TARGET][SOURCE]['weight']))
            outMeanVm = outMeanVm + averageVm[TARGET][SOURCE]

    if s['D2']:
        TARGET = typeN
        SOURCE = 'D2'

        if typeN =='drawAll':
            linewidth = 3.
        else:
            linewidth = np.sqrt(cparam[TARGET][SOURCE])/scale
        print(linewidth)
        deg = 180
        colour = 'y'
        facecolor = 'w'

        N = str(cparam[TARGET][SOURCE])
        if averageVm == True:
            drawLine(SOURCE,x,y,length,r,linewidth,deg,colour,facecolor,N,str(synparam[TARGET][SOURCE]['weight']))
        else:
            drawLine(SOURCE,x,y,length,r,linewidth,deg,colour,facecolor,str(round(averageVm[TARGET][SOURCE],2)),str(synparam[TARGET][SOURCE]['weight']))
            outMeanVm = outMeanVm + averageVm[TARGET][SOURCE]
    if s['FSN']:
        TARGET = typeN
        SOURCE = 'FSN'



        if typeN =='drawAll':
            linewidth = 3.
        else:
            linewidth = np.sqrt(cparam[TARGET][SOURCE])/scale

        deg = 135
        colour = 'm'
        facecolor = 'w'

        N = str(cparam[TARGET][SOURCE])
        if averageVm == True:
            drawLine(SOURCE,x,y,length,r,linewidth,deg,colour,facecolor,N,str(synparam[TARGET][SOURCE]['weight']))
        else:
            drawLine(SOURCE,x,y,length,r,linewidth,deg,colour,facecolor,str(round(averageVm[TARGET][SOURCE],2)),str(synparam[TARGET][SOURCE]['weight']))
            outMeanVm = outMeanVm + averageVm[TARGET][SOURCE]


    if s['GPTA']:
        TARGET = typeN
        SOURCE = 'GPTA'

        deg = 270


        if typeN in 'drawAll':
            linewidth = 3.
        else:
            linewidth = np.sqrt(cparam[TARGET][SOURCE])/scale

        colour = 'r'
        facecolor = 'w'
        if averageVm == True:
            N = str(cparam[TARGET][SOURCE])
            drawLine(SOURCE,x,y,length,r,linewidth,deg,colour,facecolor,N,str(synparam[TARGET][SOURCE]['weight']))
        else:
            drawLine(SOURCE,x,y,length,r,linewidth,deg,colour,facecolor,str(round(averageVm[TARGET][SOURCE],2)),str(synparam[TARGET][SOURCE]['weight']))
            outMeanVm = outMeanVm + averageVm[TARGET][SOURCE]
    if s['GPTI']:
        TARGET = typeN
        SOURCE = 'GPTI'

        deg = 235


        if typeN in 'drawAll':
            linewidth = 3.
        else:
            linewidth = np.sqrt(cparam[TARGET][SOURCE])/scale

        colour = 'g'
        facecolor = 'w'

        N = str(cparam[TARGET][SOURCE])
        if averageVm == True:
            drawLine(SOURCE,x,y,length,r,linewidth,deg,colour,facecolor,N,str(synparam[TARGET][SOURCE]['weight']))
        else:
            drawLine(SOURCE,x,y,length,r,linewidth,deg,colour,facecolor,str(round(averageVm[TARGET][SOURCE],2)),str(synparam[TARGET][SOURCE]['weight']))
            outMeanVm = outMeanVm + averageVm[TARGET][SOURCE]
    if s['STN']:
        TARGET = typeN
        SOURCE = 'STN'

        deg = 315


        if typeN in 'drawAll':
            linewidth = 3.
        else:
            linewidth = np.sqrt(cparam[TARGET][SOURCE])/scale

        colour = 'c'
        facecolor = 'k'
        N = str(cparam[TARGET][SOURCE])
        if averageVm == True:
            drawLine(SOURCE,x,y,length,r,linewidth,deg,colour,facecolor,N,str(synparam[TARGET][SOURCE]['weight']))
        else:
            drawLine(SOURCE,x,y,length,r,linewidth,deg,colour,facecolor,str(round(averageVm[TARGET][SOURCE],2)),str(synparam[TARGET][SOURCE]['weight']))
            outMeanVm = outMeanVm + averageVm[TARGET][SOURCE]
    if s['CTX']:
        TARGET = typeN
        SOURCE = 'CTX'

        deg = 45


        if typeN in 'drawAll':
            linewidth = 3.
        else:
            linewidth = 3

        colour = 'c'
        facecolor = 'k'
        N = 1
        if TARGET in ['GPTA', 'GPTI', 'GPI']:
            if averageVm == True:
                drawLine('EXT',x,y,length,r,linewidth,deg,colour,facecolor,N,str(noise[TARGET]['rate']))
            else:
                drawLine('EXT',x,y,length,r,linewidth,deg,colour,facecolor,str(round(averageVm[TARGET][SOURCE],2)),str(noise[TARGET]
                    ['rate']))
                outMeanVm = outMeanVm + averageVm[TARGET][SOURCE]
        else:
            if averageVm == True:
                drawLine(SOURCE,x,y,length,r,linewidth,deg,colour,facecolor,N,str(noise[TARGET]['rate']))
            else:
                drawLine(SOURCE,x,y,length,r,linewidth,deg,colour,facecolor,str(round(averageVm[TARGET][SOURCE],2)),str(noise[TARGET]
                    ['rate']))
                outMeanVm = outMeanVm + averageVm[TARGET][SOURCE]

    if averageVm == True:
        output = plt.Line2D((x+r+lout, x+r), (y, y), lw=2.,
                                     ls='-', marker='>',
                                     markersize=8*np.sqrt(sc),
                                     markerfacecolor='k',
                                     markeredgecolor='k',
                                     markevery = 3,
                                     color='k',

                                     alpha=1)
        plt.gca().add_line(output)
    else:
        output = plt.Line2D((x+r+lout, x+r), (y, y), lw=2.,
                                     ls='-', marker='>',
                                     markersize=8*np.sqrt(sc),
                                     markerfacecolor='k',
                                     markeredgecolor='k',
                                     markevery = 3,
                                     color='k',

                                     alpha=1)
        labelout(x+r+lout+0.2, y+0.05,round(outMeanVm,2)) 

        plt.gca().add_line(output)


if __name__ == '__main__':
    #p = tune(par.nparam, par.cparamOLD, par.staticsyn, par.noise, par.staticsynNoise, par.connections)
    #cparam=p.cparam
    plotmulti = True
    if plotmulti:
        

        fig = plt.figure(1)
        fig.set_dpi(110)
        fig.set_size_inches(12,15)
        grid = np.mgrid[0.2:3:3j, 0.2:3.0:3j].reshape(2, -1).T
        sc = 0.88
        drawN('GPTI', param.cparam,grid[1,0],grid[1,1],sc,param.pparam,param.staticsyn,param.noise)
        drawN('D2', param.cparam,grid[5,0],grid[5,1],sc,param.pparam,param.staticsyn,param.noise)
        drawN('D1', param.cparam,grid[2,0],grid[2,1],sc,param.pparam,param.staticsyn,param.noise)
        drawN('GPTA', param.cparam,grid[4,0],grid[4,1],sc,param.pparam,param.staticsyn,param.noise)
        drawN('STN', param.cparam,grid[0,0],grid[0,1],sc,param.pparam,param.staticsyn,param.noise)
        drawN('FSN', param.cparam,grid[8,0],grid[8,1],sc,param.pparam,param.staticsyn,param.noise)
        drawN('GPI', param.cparam,grid[3,0],grid[3,1],sc,param.pparam,param.staticsyn,param.noise)
        plt.axis('equal')
        plt.axis('off')
        plt.tight_layout()
        plt.rcParams['axes.facecolor'] = 'w'
        print(grid)
        plt.savefig('demo.png', transparent=True)
        plt.show()
    else:
        fig = plt.figure()
        fig.set_dpi(120)
        fig.set_size_inches(6, 8.5)
        sc = 1.5 # scale
        drawN('GPI', cparam,0,0,sc,p.pparam,p.staticsyn)

        #plt.axis([-3,3,-3,3])
        #plt.axis('equal')
        plt.axis('scaled')
        plt.axis('off')
        plt.tight_layout()
        plt.rcParams['axes.facecolor'] = 'w'

        plt.show()
        fig = plt.figure(1)
        fig.set_dpi(100)
        fig.set_size_inches(7, 6.5)
        grid = np.mgrid[0.2:1.6:2j, 0.2:1.3:2j].reshape(2, -1).T
        sc = 1.3
        drawN('D1', cparam,grid[0,0],grid[0,1],sc,p.pparam,p.staticsyn)
        drawN('D2', cparam,grid[1,0],grid[1,1],sc,p.pparam,p.staticsyn)
        drawN('GPTI', cparam,grid[2,0],grid[2,1],sc,p.pparam,p.staticsyn)
        drawN('GPTA', cparam,grid[3,0],grid[3,1],sc,p.pparam,p.staticsyn)
        plt.axis('equal')
        plt.axis('off')
        plt.tight_layout()
        plt.rcParams['axes.facecolor'] = 'w'

        fig = plt.figure(2)
        fig.set_dpi(70)
        fig.set_size_inches(6, 8.5)
        sc = 1.5 # scale
        drawN('GPI', cparam,0,0,sc,p.pparam,p.staticsyn)

        #plt.axis([-3,3,-3,3])
        #plt.axis('equal')
        plt.axis('scaled')
        plt.axis('off')
        plt.tight_layout()
        plt.rcParams['axes.facecolor'] = 'w'
        plt.show()
