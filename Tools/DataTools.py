'''
    Author: Fernando Paulin
    Version: 1.0
    Description: Different tools for data manipulation
'''

'''IMPORTS'''
from numpy.random import randn




class DataTools():

    def __init__(self):
        pass

    def GenerateNoisyData(self, initial, step, NumberOfDatapoints, NoiseFactor):
        return [initial + step*i+randn()* NoiseFactor for i in range(NumberOfDatapoints)]