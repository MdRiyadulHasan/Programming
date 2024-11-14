def countPrimes( n: int) -> int:
        primes = [True]*(n)
        if n<2:
            return 0
        primes[0]=primes[1]=False
        i=2
        while i*i<(n):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j]=False
            i+=1
        primeList = [i for i, p in enumerate(primes) if p]
        print(primeList)
        return sum(primes)
n = 10
print(countPrimes(n))