n = 100
primes = set(range(2, n+1))

for i in range(2, int(n**0.5+1)):
    primes.difference_update(range(i*2, n+1, i))

primes=list(primes)
print(primes)
