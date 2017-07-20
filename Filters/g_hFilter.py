'''
    Author: Fernando Paulin
    Version: 1.0
    Description: g-h filter
'''


'''IMPORTS'''
import numpy as np


class g_hFilter():

    def __init__(self):
        self.OnlineInitialised = False
        pass


    def Calculate_ghFilter(self, data, Initial, Increment, G, H, DeltaT):
        #INITIALISATION
        x_estimate = Initial
        results=[]
        for point in data:
            #PREDICTION
            x_prediction = x_estimate + (Increment*DeltaT)
            #UPDATE
            residual = point - x_prediction
            Increment = Increment + H * (residual) / DeltaT
            x_estimate = x_prediction + G * residual
            results.append(x_estimate)
        return results

    def Online_ghFilter(self, input, PreviousPred, Increment, G,H,DeltaT):
        if not (self.OnlineInitialised): # If the filter has not been initialised, the first "hint" is the first point.
            PreviousPred = input
            self.OnlineInitialised=True
        x_prediction = PreviousPred + (Increment*DeltaT)
        #UPDATE
        residual = (input - x_prediction)
        Increment = Increment + (H * (residual) / DeltaT )
        return (x_prediction + G * residual)



