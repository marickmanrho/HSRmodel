def save_np_array(data,path,type):

    import numpy as np
    import json

    # And write it to JSON
    #if isinstance(data, np.ndarray):
    #    raise TypeError('Data is not a Numpy.Array object')

    jsonpath = path + '/' + type + '.json'
    data_dict = {}
    data_dict['type'] = type
    data_dict['data'] = data.tolist()
    with open(jsonpath, "w") as write_file:
        json.dump(data_dict, write_file, separators=(',', ':'),\
         sort_keys=True, indent=4)

def save_c_np_array(data,path,type):

    import numpy as np
    import json

    # And write it to JSON
    #if isinstance(data, np.ndarray):
    #    raise TypeError('Data is not a Numpy.Array object')

    jsonpath = path + '/' + type + '.json'
    data_dict = {}
    data_dict['type'] = type
    real = np.real(data)
    imag = np.imag(data)
    data_dict['data_real'] = real.tolist()
    data_dict['data_imag'] = imag.tolist()
    with open(jsonpath, "w") as write_file:
        json.dump(data_dict, write_file, separators=(',', ':'),\
         sort_keys=True, indent=4)

def save_eigen(w,v,path,type):

    import numpy as np
    import json

    # And write it to JSON
    #if isinstance(data, np.ndarray):
    #    raise TypeError('Data is not a Numpy.Array object')

    jsonpath = path + '/' + type + '.json'
    data_dict = {}
    data_dict['type'] = type

    wreal = np.real(w)
    wimag = np.imag(w)

    vreal = np.real(v)
    vimag = np.imag(v)

    data_dict['w_real'] = wreal.tolist()
    data_dict['w_imag'] = wimag.tolist()

    data_dict['v_real'] = vreal.tolist()
    data_dict['v_imag'] = vimag.tolist()

    with open(jsonpath, "w") as write_file:
        json.dump(data_dict, write_file, separators=(',', ':'),\
         sort_keys=True, indent=4)

def save_dict(data_dict,path,type):
    import numpy as np
    import json

    # And write it to JSON
    #if isinstance(data, np.ndarray):
    #    raise TypeError('Data is not a Numpy.Array object')

    jsonpath = path + '/' + type + '.json'
    data_dict['type'] = type

    with open(jsonpath, "w") as write_file:
        json.dump(data_dict, write_file, separators=(',', ':'),\
         sort_keys=True, indent=4)
