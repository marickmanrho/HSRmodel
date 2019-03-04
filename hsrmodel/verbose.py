#
#                       verbose.py
#
# Simple function which serves to print info to the screen for the
# td_superoperator routine.
#
#-------------------------------------------------------------------------------

def verbose(N,L,w,v,alpha,Init):
    import numpy as np

    # Print out all matrices and vectors
    if True and N<4:
        np.set_printoptions(suppress=True)
        print('---------------\n time evolution operator')
        print(np.array_str(L, precision=3))
        print('---------------\n Eigenvalues')
        print(np.array_str(w, precision=3))
        print('---------------\n Eigenvectors')
        print(np.array_str(v, precision=3))
        print('---------------\n Alpha\'s')
        print(np.array_str(alpha, precision=3))

    print('|Alpha|: ' + str(np.sum(alpha**2).real) + ' + ' + str(np.sum(alpha**2).imag) + 'j')
    print('---------------\n Init')
    print(np.array_str(Init[::N+1,0], precision=3))
