from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N, K = map(int, input().split())

answer = None

for i in range(1, N+1):
    if N % i == 0:
        K -= 1
    if K == 0:
        answer = i
        break

if K == 0:
    print(str(answer))
else:
    print(str(0))

