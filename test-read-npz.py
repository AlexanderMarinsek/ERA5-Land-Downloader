
"""
Read NPZ file in order to check integrity.
"""

import numpy as np


# READ
filename = 'ERA5-Land/Area-46.0-15.0-46.1-15.2/2019/01/01/data.npz'
#filename = 'ERA5-Land/Area-46.0-15.0-46.0-15.0/2019/01/01/data.npz'

data = np.load(filename, allow_pickle=True)
lst = data.files

names = data[lst[0]]
arrays = data[lst[1]]

print ""
print "TEST READ NPZ FILE: \n%s" % filename

print ""
print "Combined shape: %s" % str(arrays.shape)

for i, arr in enumerate(arrays):
    print ""
    print "Name (%d): %s" % (i, names[i])
    print "Shape: %s" % str(arr.shape)
    print arr
    
        