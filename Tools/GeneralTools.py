'''
    Author: Fernando Paulin
    Version: 1.0
    Description: Different tools for Data
'''
from sklearn.metrics import mean_squared_error
from math import sqrt



class GeneralTools():

    def __init__(self):
        pass


    def __del__(self):
        pass

    def CalculateRMSE(self,Data1,Data2):
        assert (len(Data1) == len(Data2)), print ("LENGTHS OF LISTS ARE NOT EQUAL")
        return sqrt(mean_squared_error(Data1,Data2))
