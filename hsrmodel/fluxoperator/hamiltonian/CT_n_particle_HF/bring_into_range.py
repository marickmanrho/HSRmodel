def bring_into_range_arr(N,arr):
    import numpy as np

    a = np.shape(arr)

    for n in range(a[0]):
        for m in range(a[1]):
            if arr[n,m] > N:
                arr[n,m] = arr[n,m] - N
            if arr[n,m] < 0:
                arr[n,m] = arr[n,m] + N
    return(arr)

def bring_into_range_vec(N,vec):
    import numpy as np

    a = np.shape(vec)

    for n in range(a[0]):
        if vec[n] >= N:
            vec[n] = vec[n] - N
        if vec[n] < 0:
            vec[n] = vec[n] + N

    return(vec)
