from sys import stdin, stdout

input = stdin.readline
# print = stdout.write

N, K = map(int, input().split())
plugs = [0] * N
products = list(map(int, input().split()))

p_set = set(products)

p_cnt = []
for p in p_set:
    p_cnt.append(products.count(p))

p_cnt = sorted(p_cnt, reverse=True)

answer = 0

while len(p_cnt) > N:
    for i in range(N):
        p_cnt[i] -= 1

        if p_cnt[i] == 0:
            p_cnt.pop(i)
            answer += 1

            break

print(answer)
[3 2 2 1]