

from v_print import vPrint, vPrint_init # Verbose print
from era5_land_fetcher import fetch_era5_land # fetch ERA5-Land data
from era5_land_converter import convert_era5_land # Convert ERA5-Land format

import os
import errno
import datetime
import numpy as np

# Fetch base directory in order to run from other directories
base_dir = os.path.dirname(__file__)

# Select desired time period
start_date = datetime.date(2019, 1, 1)
stop_date = datetime.date(2019, 1, 1)

# Select ERA5-Land area coverage
era5_area = [46.0, 15.0, 46.1, 15.2]  
#era5_area = [46.0, 15.0, 46.0, 15.0]  

# Select ERA5-Land data variables
# Later select ... var-names / param-names ... [:,0] / [:,1]
era5_names = np.array([
    [ '10m_u_component_of_wind',        '10 metre V wind component' ],
    [ '10m_v_component_of_wind',        '10 metre U wind component' ],
    [ '2m_temperature',                 '2 metre temperature' ]
])

def main ():
    
    # Import global vars
    global start_date, stop_date, era5_area, era5_names
        
    area_str = "-".join([str(elem) for elem in era5_area])
    
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
        rel_dirname = "ERA5-Land/Area-%s/%04d/%02d/%02d/" % \
            (area_str, date.year, date.month, date.day)
        dirname = os.path.join(base_dir, rel_dirname)
        
        # *** MAIN THREE STEPS (comment out as needed) ***
        
        # Create data directory, if non-existent
        create_data_dir (date, dirname)
        
        # Fetch ERA5-Land data
        fetch_era5_land (date, era5_area, era5_names[:,0].tolist(), dirname)
        
        # Convert ERA5-Land format to NPZ (numpy)
        convert_era5_land (era5_names[:,1], dirname)
    


"""
Create directory for saving ERA5 data if it does not exist
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

