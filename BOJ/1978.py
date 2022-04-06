from sys import stdin, stdout

input = stdin.readline
print = stdout.write

def isPrime(n):
    if n == 1: return False
    cnt = 0
    for i in range(2, n):
        if n % i == 0:
            cnt += 1
    if cnt == 0: return True
    else: return False


_ = input()
arr = input().split()

ans = 0
for i in arr:
    if isPrime(int(i)):
        ans += 1

print(str(ans))
