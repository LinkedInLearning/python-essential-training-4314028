
def getFactors(n):
    return [factor for factor in range(1, n+1) if n % factor == 0]

print(f'name in factors.py is {__name__}')