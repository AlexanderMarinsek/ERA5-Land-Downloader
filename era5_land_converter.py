
# Handle 'undefined' error
import os
import conda

conda_file_dir = conda.__file__
conda_dir = conda_file_dir.split('lib')[0]
proj_lib = os.path.join(os.path.join(conda_dir, 'share'), 'proj')
os.environ["PROJ_LIB"] = proj_lib


from v_print import vPrint, vPrint_init # Verbose print

import pygrib # GRIB file interpreter
import numpy as np


"""
Convert ERA5-Land format to NPZ (numpy) and save to file
    p1: target parameter ... list of strings (view ECMWF documentation)
    p2: target directory ... path to data directory
"""
def convert_era5_land (params, dirname):
    grbs = pygrib.open(dirname + 'data.grib')
    num_of_rows = 1.0 * len(grbs.select()) / len(params)
    
    vPrint( "" )
    vPrint( "Data conversion started (%0.1f rows)" % num_of_rows)
    vPrint( "\tParameters: \n%s" % str(params) )
    vPrint( "\tDirname: \n%s" % dirname )
    
    output_data = []
    
    # Iterate ERA5-Land parameters
    for i, param in enumerate(params):
        # Extract param-specific measurements
        param_grbs = grbs.select(name=param)
        # Add initial dummy element to match size (later dleeted)
        data_aggregator = np.array([param_grbs[0].values])
        # Iterate measurements for the given param
        for j, grb in enumerate(param_grbs):
            grb = param_grbs[j]
            # Encapsulate array in an additional array
            tmp = np.array([grb.values])
            # Append param measurements to data aggregator
            data_aggregator = np.append( data_aggregator, tmp, axis=0 )
        # Delete initial dummy element
        data_aggregator = np.delete( data_aggregator, 0, axis=0 )
        # Add aggregated data to output list
        output_data.append(data_aggregator);

    # Save to file
    np.savez(dirname + "data.npz", output_data, params)
    
    