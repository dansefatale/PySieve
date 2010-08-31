import _pysieve

def factor(n):
    """ Returns a list of the prime factors of n """
    return map(int, _pysieve.pysieve(str(n)))

def dfactor(n):
    """ Returns a list of distinct prime factors of n """
    return list(set(factor(n)))

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


