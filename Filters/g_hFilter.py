'''
    Author: Fernando Paulin
    Version: 1.0
    Description: g-h filter
'''


'''IMPORTS'''
import numpy as np


class g_hFilter():

    def __init__(self, data, Initial, Increment, G, H, DeltaT):
        self.data = data
        self.X0 = Initial
        self.dX = Increment
        self.G = G
        self.H = H
        self.dT = DeltaT

    def Calculate_ghFilter(self):
        #INITIALISATION
        x_estimate = self.X0
        results=[]
        for point in self.data:
            #PREDICTION
            x_prediction = x_estimate + (self.dX*self.dT)
            #UPDATE
            residual = point - x_prediction
            self.dX = self.dX + self.H * (residual) / self.dT
            x_estimate = x_prediction + self.G * residual
            results.append(x_estimate)
        return results
