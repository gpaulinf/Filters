from Tools.DataTools import DataTools
from Filters.g_hFilter import g_hFilter

DT = DataTools()
GFilter = g_hFilter(DT.GenerateNoisyData(0,1,300,3),0,1,0.5,0.5,1)

print (GFilter.Calculate_ghFilter())

