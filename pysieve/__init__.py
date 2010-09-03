import _pysieve
import os.path
import os

def factor(n):
    """ Returns a list of the prime factors of n """

    result = map(int, _pysieve.msieve(str(n)))
    

    # If there are msieve temp files, clean them up
    cwd = os.getcwd()
    for e in ['.log', '.dat', '.fb']:
        p = os.path.join(cwd, 'msieve' + e)
        if os.path.exists(p):
            os.remove(p)

    return result

def dfactor(n):
    """ Returns a list of distinct prime factors of n """
    return sorted(list(set(factor(n))))

def facExponents(n):
    """ Return a list of tuples containing the prime factors of n and their exponents """

    # determine the exponent of fac in n
    def expfind(fac, n):
        if (n/fac%fac != 0):
            return 1
        else:
            return 1 + expfind(fac, n/fac)

    def result(list):
        return zip(list,
                   (lambda(x):
                        map(expfind, x, [n]*len(x)))(list))

    return result(dfactor(n))

__all__ = ['factor', 'dfactor', 'facExponents']


