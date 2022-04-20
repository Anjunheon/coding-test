from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def dfs(idx, cnt):
    global max_cnt

    if cnt == K:
        wcnt = 0
        for word in words:
            check = True
            for c in word:
                if not visited[ord(c) - ord('a')]:
                    check = False
                    break
            if check:
                wcnt += 1
        max_cnt = max(max_cnt, wcnt)
    for i in range(idx, 26):
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt + 1)
            visited[i] = False


N, K = map(int, input().split())

if K < 5:
    print('0')
    exit()
elif K == 26:
    print(str(N))
    exit()

K -= 5
words = [list(set(list(input()[4:-5]))) for _ in range(N)]
visited = [False for _ in range(26)]

for c in ('a', 'c', 'i', 'n', 't'):
    visited[ord(c) - ord('a')] = True

max_cnt = 0

dfs(0, 0)

print(str(max_cnt))
