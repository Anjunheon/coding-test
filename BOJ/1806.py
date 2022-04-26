from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N, S = map(int, input().split())

num = list(map(int, input().split()))

if sum(num) < S:
    print(str(0))
    exit()

for i in range(N):
    for j in range(N-i):
        if sum(num[j:j+i+1]) >= S:
            print(str(i+1))
            exit()

