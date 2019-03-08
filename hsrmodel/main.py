def main():
    import sys
    import json
    from initialization.convert_txt_to_dict import txt_to_dict
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

    # Run HSR model
    #hsrmodel(parms)

main()
