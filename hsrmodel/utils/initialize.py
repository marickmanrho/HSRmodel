#
#                               initialize.py
#
#   This function wil read in the parameters given in the command line, or it
#   uses the default_parameters.txt as an input. I also creates a Data/<name>
#   folder in which all data will be stored.
#
#------------------------------------------------------------------------------#
def initialize():
    # Python packages
    import sys
    import json
    import numpy as np

    # Custom packages
    from utils.txt_to_dict import txt_to_dict
    from utils.init_folder import init_folder

    # Read parameters file
    try:
        parmsfile = sys.argv[1]
    except:
        parmsfile = "utils/default_parameters.txt"
    parms = txt_to_dict(parmsfile)

    # Setup Data/<name> folder
    parms = init_folder(parms)

    # Write parameters JSON file
    jsonpath = parms["PathDataFolder"]+'/parameters.json'
    with open(jsonpath, "w") as write_file:
        json.dump(parms, write_file, sort_keys=True, indent=4)

    return parms
