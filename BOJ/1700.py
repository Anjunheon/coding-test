from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N, K = map(int, input().split())

multi_tab = []
check = []
queue = list(map(int, input().split()))

answer = 0

while len(queue):
    p = queue.pop(0)

    if p in multi_tab:
        continue

    elif len(multi_tab) < N:
        multi_tab.append(p)
        continue

    else:
        Max = -1
        out = 0
        for i in multi_tab:
            if i not in queue:
                out = i
                break
            elif Max < queue.index(i):
                Max = queue.index(i)
                out = i

        multi_tab.remove(out)
        answer += 1

        multi_tab.append(p)

print(str(answer))
