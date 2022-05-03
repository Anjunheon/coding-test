from sys import stdin, stdout

input = stdin.readline
# print = stdout.write


def cal_cost(Buses, bus, dep, total, minimum):
    total += bus[1]

    if bus[0] == dep:
        minimum = min(total, minimum)
    else:
        for b in Buses[bus[0]]:
            cal_cost(Buses, b, dep, total, minimum)


N = int(input())
M = int(input())
Bus = [] * (M + 1)

for _ in range(M):
    depart, arrive, cost = map(int, input().split)
    Bus[depart].append([arrive, cost])

start, end = map(int, input().split())

for bus in Bus[start]:
    cal_cost(Bus, bus, end)
