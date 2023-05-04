from numbers.factors import getFactors
def isPrime(n, foundPrimes=None):
    return len(getFactors(n)) == 2

def listPrimes(max):
    foundPrimes = []
    for n in range(2, max):
        if isPrime(n, foundPrimes):
            foundPrimes.append(n)
    return foundPrimes
