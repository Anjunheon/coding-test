from sys import stdin, stdout

input = stdin.readline
print = stdout.write

psg = [list(map(int, input().split())) for _ in range(10)]


cnt = max = 0
for i in psg:
    cnt -= i[0]
    cnt += i[1]

    if max < cnt:
        max = cnt

print(str(max))
