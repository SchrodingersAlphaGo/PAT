import time

def find_all_primes(n, temp):
    array = [1]*(n+1)
    gap = prime = 2
    
    while prime<=n:
        if array[prime] > 0:
            temp.append(prime)
            if prime > 2:
                gap = prime * 2
            for i in range(prime**2, n+1, gap):
                array[i] = 0
        prime += 1

n = int(input())

tstar = time.clock()
all_primes = []
find_all_primes(n,all_primes)
count = 0
for i in range(len(all_primes)-1):
    if (all_primes[i+1]-all_primes[i])==2:
        count = count + 1

print(count)

tend = time.clock()
print(tend-tstar)