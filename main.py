

from v_print import vPrint, vPrint_init # Verbose print
from reanalysis_fetcher import fetch_reanalysis # fetch reanalysis data
from reanalysis_converter import convert_reanalysis # Convert reanalysis format

import os
import errno
import datetime
import numpy as np

# Fetch base directory in order to run from other directories
base_dir = os.path.dirname(__file__)

# Select desired time period
#start_date = datetime.date(2016, 1, 1)
start_date = datetime.date(2019, 1, 1)
stop_date = datetime.date(2019, 1, 1)

# Select reanalysis area coverage
reanalysis_area = [45.7, 14.6, 45.7, 14.6]  
#reanalysis_area = [45.8, 14.5, 45.5, 14.7]  
#reanalysis_area = [46.0, 15.0, 46.0, 15.0]  

#dataset = "reanalysis-era5-single-levels"
dataset = "reanalysis-era5-land"

# Select reanalysis data variables
# Later select ... var-names / param-names ... [:,0] / [:,1]
data_vars = np.array([
    [ '10m_u_component_of_wind',            '10 metre V wind component' ],
    [ '10m_v_component_of_wind',            '10 metre U wind component' ],
    [ '2m_temperature',                     '2 metre temperature' ],
    [ 'surface_pressure',                   'Surface pressure' ],
    [ 'surface_solar_radiation_downwards',  'Surface solar radiation downwards' ],
    [ '2m_dewpoint_temperature',            '2 metre dewpoint temperature' ]
])

def main ():
    
    # Import global vars
    global start_date, stop_date, reanalysis_area, data_vars
        
    area_str = "-".join([str(elem) for elem in reanalysis_area])
    
    # Initialize (non)verbose printing
    vPrint_init(True)
        
    now = datetime.datetime.now()
    dt_string = now.strftime("%Y-%m-%dT%H:%M:%S")
    vPrint( "" )
    vPrint( "STARTED: %s" % dt_string )
    vPrint( "" )

    vPrint( "Start date: %s" % str(start_date) )
    vPrint( "Stop date: %s" % str(stop_date) )

    days = (stop_date - start_date).days + 1       # as timedelta

    vPrint( "Total days: %s" % str(days))
    
    vPrint( "Area: %s" % area_str )

    for i in range(0, days):
        
        date = start_date + datetime.timedelta(days=i)
        # Generate path
        rel_dirname = "Data/%s/Area-%s/%04d/%02d/%02d/" % \
            (dataset, area_str, date.year, date.month, date.day)
        dirname = os.path.join(base_dir, rel_dirname)
        
        # *** MAIN THREE STEPS (comment out as needed) ***
        
        # Create data directory, if non-existent
        create_data_dir (date, dirname)
        
        # Fetch reanalysis data
        fetch_reanalysis (dataset, date, reanalysis_area, data_vars[:,0].tolist(), dirname)
        
        # Convert reanalysis format to NPZ (numpy)
        convert_reanalysis (data_vars[:,1], dirname)
    
        
    now = datetime.datetime.now()
    dt_string = now.strftime("%Y-%m-%dT%H:%M:%S")
    vPrint( "" )
    vPrint( "ENDED: %s" % dt_string )
    vPrint( "" )


"""
Create directory for saving reanalysis data if it does not exist
    p1: datetime.date() object
    p2: target directory ... path to data directory
"""
def create_data_dir (date, dirname):
    # Check for existence
    if not os.path.exists(dirname):
        try:
            os.makedirs(dirname)
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


main()

