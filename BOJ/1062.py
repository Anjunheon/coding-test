from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N, K = map(int, input().split())

words = sorted([list(sorted(set(input()[:-2]))) for _ in range(N)])

cnt = 0
max_cnt = 0

if N == 1:
    if len(words[0]) == K:
        max_cnt = 1
else:
    for i in range(0, len(words)-1):
        if words[i] == words[i+1]:
            if cnt == 0:
                cnt += 2
            else:
                cnt += 1
        else:
            if cnt > max_cnt and len(words[i]) == K:
                max_cnt = cnt

            cnt = 0

if cnt > max_cnt:
    max_cnt = cnt

print(str(max_cnt))
