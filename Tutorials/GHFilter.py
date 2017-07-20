'''
    Author: Fernando Paulin
    Version: 1.0
    Description: This file explains how to use the GH Filter both online and in batches
'''

from Imports import *

'''GENERATE NOISY DATA'''
Data = DT.GenerateNoisyData(initial = 0, step = 1, NumberOfDatapoints=300,NoiseFactor=3)
FilteredResults = GFilter.Calculate_ghFilter(Data,0,1,0.8,0.5,1)


''' TO USE THE ONLINE GH FILTER  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - '''
Filtered=[]
PreviousPrediction = 0
for i,point in enumerate(Data):
    PreviousPrediction = GFilter.Online_ghFilter(input=point, PreviousPred=PreviousPrediction, Increment=1,G=0.6,H=0.3,DeltaT=1)
    Filtered.append(PreviousPrediction) #APPEND RESULTS TO PLOT THEM
''' END OF EXAMPLE FOR ONLINE GH FILTER - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'''



'''TO USE THE GH FILTER IN BATCHES. USEFUL WHEN A SIGNAL HAS BEEN RECORDED AND WE NEED TO FILTER IT'''
Filtered = GFilter.Calculate_ghFilter(data=Data, Initial=Data[0], Increment=1 , G = 0.8, H=0.5, DeltaT=1)
'''END OF EXAMPLE FOR GH FILTER IN BATCHES'''



'''PLOT THE DATA'''
PT.PlotGraphs(AllY=[Data, Filtered], TITLE='GH FILTER', tags = ['REAL DATA', 'G_H FILTER'], XAxes='t', YAxes='Signal')