from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N, S = map(int, input().split())
num = list(map(int, input().split()))

answer = 100001

start = end = total = 0

while True:
    if total >= S:
        answer = min(answer, end - start)
        total -= num[start]
        start += 1
    elif end == N:
        break
    else:
        total += num[end]
        end += 1

if answer > N:
    print(str(0))
else:
    print(str(answer))
