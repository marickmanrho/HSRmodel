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

    # Custom packages
    from initialization.txt_to_dict import txt_to_dict
    from initialization.init_folder import init_folder

    # Read parameters file
    try:
        parmsfile = sys.argv[1]
    except:
        parmsfile = "initialization/default_parameters.txt"
    parms = txt_to_dict(parmsfile)

    # Setup Data/<name> folder
    parms = init_folder(parms)

    # Write parameters JSON file
    jsonpath = parms["PathDataFolder"]+'/parameters.json'
    with open(jsonpath, "w") as write_file:
        json.dump(parms, write_file)

    return parms
