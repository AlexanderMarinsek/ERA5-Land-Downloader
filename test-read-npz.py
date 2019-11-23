
"""
Read NPZ file and simple plot in order to check integrity.

Data format and units found at (ex. solar radiation is in J/m^2):
https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=overview

Timestamp is in UTC format:
https://confluence.ecmwf.int/display/CKB/ERA5-Land+data+documentation
"""

from matplotlib import pyplot as plt
import numpy as np


# READ
filename = 'ERA5-Land/Area-44.5-28.5-44.7-28.7/2018/12/01/data.npz'
#filename = 'ERA5-Land/Area-46.0-15.0-46.0-15.0/2019/01/01/data.npz'

data = np.load(filename, allow_pickle=True)
lst = data.files

names = data[lst[0]]
arrays = data[lst[1]]

print ""
print "TEST READ NPZ FILE: \n%s" % filename

print ""
print "Combined shape: %s" % str(arrays.shape)


fig = plt.figure()
x = np.arange(0,24,1)

for i, arr in enumerate(arrays):
    print ""
    print "Name (%d): %s" % (i, names[i])
    print "Shape: %s" % str(arr.shape)
    
    ax = fig.add_subplot(3,3,i+1)
    ax.plot(x, arr[:,1,1])
    ax.set_title(names[i])
    
plt.tight_layout()
plt.show()
        