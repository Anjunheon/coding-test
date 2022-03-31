from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N = int(input())
l = list(map(int, input().split()))

min = 1000000
max = -1000000

for n in l:
    if min > n:
        min = n
    if max < n:
        max = n

print(str(min) + ' ' + str(max))
