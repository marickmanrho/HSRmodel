# functions for importing Json files

def input_c_np_array(type,parms):
    # Itterate over all possible input files
    for n in range(1,3):
        fileinput = sys.argv[n]

        # See if it is a JSON
        if fileinput[-4:]=='json':
            filecontent = codecs.open(fileinput, 'r', encoding='utf-8').read()
            filedict = json.loads(filecontent)

            # If JSON check if it is a hamiltonian data file
            if filedict['type'] == type:
                H = np.array(filedict['data_real']) + 1j*np.array(filedict['data_imag'])

                #del filecontent
                del filecontent
                del fileinput
                del filedict
                break
    return(H)

def input_eigen(type,parms):
    # Itterate over all possible input files
    for n in range(1,3):
        fileinput = sys.argv[n]

        # See if it is a JSON
        if fileinput[-4:]=='json':
            filecontent = codecs.open(fileinput, 'r', encoding='utf-8').read()
            filedict = json.loads(filecontent)

            # If JSON check if it is a hamiltonian data file
            if filedict['type'] == type:
                v = np.array(filedict['v_real']) + 1j*np.array(filedict['v_imag'])
                w = np.array(filedict['w_real']) + 1j*np.array(filedict['w_imag'])
                #del filecontent
                del filecontent
                del fileinput
                del filedict
                break
    return(v,w)
