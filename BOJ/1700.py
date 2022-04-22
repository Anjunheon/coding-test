from sys import stdin, stdout

input = stdin.readline
# print = stdout.write

N, K = map(int, input().split())

if N == 1:
    print(K - 1)
    exit()
elif N == 100:
    print(0)
    exit()

plugs = [0] * (K + 1)
check = []
products = list(map(int, input().split()))

for i, p in enumerate(products):
    plugs[p] += 1
    if len(check) < N and p not in check:
        check.append(p)

answer = 0
cnt = 1
while len(products) > 0:
    if len(check) < N or products[0] in check:
        if products[0] not in check:
            check.append(products[0])
    else:
        out = 100
        print(check, end=' ')
        print(products, end=' ')
        for p in check:
            if out > products.count(p):
                out = p
        print(out)

        check.pop(check.index(out))
        check.append(products[0])

        answer += 1

    plugs[products[0]] -= 1
    products.pop(0)
    cnt += 1

print(str(answer))
