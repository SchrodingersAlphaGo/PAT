import math
import time

def isPrime(n):
    if n%2==0:
        return False
    if n==3:
        return True
    elif n%3==0:
        return False
    if n==5:
        return True
    elif n%5==0:
        return False

    for i in range(7,int(math.sqrt(n))+1,2):
        if n%i == 0:
            return False
    return True


n = int(input())
ts = time.clock()

all_prime = [2]
for x in range(3,n+1,2):
    if isPrime(x):
        all_prime.append(x)
print(time.clock() - ts)
#print(all_prime)

count_pairs = 0
for i in range(len(all_prime)-1):
    if (all_prime[i+1] - all_prime[i]) == 2:
        count_pairs = count_pairs + 1

#te = time.clock()
#print(te-ts)
print(count_pairs)