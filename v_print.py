
# Module's global verbose variable
verbose = False

"""
Initialize module's global verbose variable
    p1: boolean value
"""
def vPrint_init (v):
    global verbose
    verbose = v

"""
Custom print only, if verbose is ON
    p1: string to print
"""
def vPrint (text):
    if verbose:
        print "*\t%s" % text