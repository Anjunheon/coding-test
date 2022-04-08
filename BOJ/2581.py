from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def isPrime(n):
    for i in range(n//2, 1, -1):
        if n % i == 0:
            return False
    return True


M = int(input())
M = 2 if M == 1 else M
N = int(input())

P = []
min = 10000

for i in range(M, N+1):
    if isPrime(i):
        P.append(i)
        if min > i:
            min = i

print(str(sum(P)) + '\n' + str(min)) if len(P) else print(str(-1) + '\n')
