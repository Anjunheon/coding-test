from sys import stdin, stdout

input = stdin.readline
# print = stdout.write


def cal_cost(bus, dep, total, minimum):
    total += bus[1]

    if bus[0] == dep:
        minimum = min(total, minimum)
    else:
        for i in range(len())
        cal_cost()
        return minimum


N = int(input())
M = int(input())
Bus = [] * (M + 1)

for _ in range(M):
    depart, arrive, cost = map(int, input().split)
    Bus[depart].append([arrive, cost])



start, end = map(int, input().split())


