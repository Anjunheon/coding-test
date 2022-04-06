from sys import stdin, stdout

input = stdin.readline
print = stdout.write

A = [list(map(int, input().split())) for _ in range(int(input()))]

for i in range(len(A)):
    print(str(sorted(A[i])[7]) + '\n')
