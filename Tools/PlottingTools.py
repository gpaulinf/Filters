'''
    Author: Fernando Paulin
    Version: 1.0
    Description: Different tools for plotting Data
'''

'''IMPORTS'''
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')


__COLOURS__ = ['b', 'c', 'r', 'g', 'm', 'y', 'k', 'w']

class PlottingTools():

    def __init__(self):
        pass

    def PlotGraphs(self, AllY, AllX=[], tags=[], figsize=(8,4), TITLE="", colors =[],XAxes='', YAxes=''):
        fig = plt.figure(1, figsize=figsize)
        ax1 = fig.add_subplot(111)
        if (AllX == []): AllX = np.zeros(len(AllY))
        if (len(tags)!=len(AllX) and len(tags)!=len(AllY)): tags=(np.ones(len(AllX)))  #IF TAGS NOT SPECIFIED
        if (len(colors) != len(AllX)): colors = __COLOURS__[:len(AllX)]
        for x,y,tag,colour in zip(AllX,AllY,tags,colors):
            if (type(x)==type(y)):
                if (len(x)==len(y)):
                    ax1.plot(x,y, color = colour, label=tag)
            else: ax1.plot(y, color=colour, label=tag)
        ax1.set_title(TITLE, size=14)
        ax1.legend()
        ax1.set_xlabel(XAxes, size=10)
        ax1.set_ylabel(YAxes, size=10)
        plt.show()


