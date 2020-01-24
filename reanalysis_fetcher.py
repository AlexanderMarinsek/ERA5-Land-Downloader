
from v_print import vPrint, vPrint_init # Verbose print

import cdsapi # reanalysis API

c = cdsapi.Client()

"""
Fetch reanalysis data and save to file
    p1: target date ... datetime.date() object
    p2: target area ... list, 0.1 accuracy (ex. [46.0, 14.2, 45.4, 15])
    p3: target variable names ... list of strings (not equal to parameter names)
    p4: target directory ... path to data directory
"""
def fetch_reanalysis (dataset, date, area, vars, dirname):
    
    vPrint( "" )
    vPrint( "Retrieving grib data for: %s" % str(date) )
    vPrint( "\tArea: \n%s" % str(area) )
    vPrint( "\tVariables: \n%s" % vars )
    vPrint( "\tDirname: \n%s" % dirname )
    
    r = c.retrieve(
        dataset,
        {
            'area': area,
            'format': 'grib',
            'year': date.year,
            'month': date.month,
            'day': date.day,
            'time': [ 
                '00:00', '01:00', '02:00', '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', 
                '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00', '21:00', '22:00', '23:00' ],
            'variable': vars
        },
        dirname + "data.grib"
     )