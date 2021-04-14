import np

RC1 = 0.01
RC2 = 0.1
RC3 = 1

def v_in(t):
    if (np.floor(2 * t) % 2) == 0:
        return 1
    else:
        return -1


