from sys import stdin, stdout

input = stdin.readline
print = stdout.write

A, B = map(int, input().split())

n = 1
cnt = 0
arr = []
for i in range(B):
    arr.append(n)
    cnt += 1
    if n == cnt:
        n += 1
        cnt = 0

print(str(sum(arr[A-1:B])))
