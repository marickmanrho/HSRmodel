def get_hamiltonian(parms):
    import numpy as np
    import codecs, json
    import sys
    from hamiltonian.gen_h import gen_h

    # Determine if Hamiltonian is to be read from file
    try:
        # Itterate over all possible input files
        for n in range(1,3):
            fileinput = sys.argv[n]

            # See if it is a JSON
            if fileinput[-4:]=='json':
                filecontent = codecs.open(fileinput, 'r', encoding='utf-8').read()
                filedict = json.loads(filecontent)

                # If JSON check if it is a hamiltonian data file
                if filedict['type'] == 'hamiltonian':
                    H = np.array(filedict['data'])

                    #del filecontent
                    del filecontent
                    del fileinput
                    del filedict
                    break

    # Or generate Hamiltonian from scratch
    except:
        H,F = gen_h(parms)

        # And write it to JSON
        if parms["save_hamiltonian"]:
            jsonpath = parms["PathDataFolder"]+'/hamiltonian.json'
            hamiltonian_dict = {}
            hamiltonian_dict['type'] = 'hamiltonian'
            hamiltonian_dict['data'] = H.tolist()
            with open(jsonpath, "w") as write_file:
                json.dump(hamiltonian_dict, write_file, separators=(',', ':'),\
                 sort_keys=True, indent=4)

    return(H,F)
