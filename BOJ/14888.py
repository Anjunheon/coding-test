from sys import stdin, stdout

input = stdin.readline
print = stdout.write

minval = 1000000000
maxval = -1000000000


def dfs(Op, res, cnt):
    global A, minval, maxval
    cnt += 1

    if sum(Op) == 0:
        minval = min(minval, res)
        maxval = max(maxval, res)

    if Op[0] > 0:
        Op1 = Op.copy()
        Op1[0] -= 1
        dfs(Op1, res + A[cnt], cnt)
    if Op[1] > 0:
        Op2 = Op.copy()
        Op2[1] -= 1
        dfs(Op2, res - A[cnt], cnt)
    if Op[2] > 0:
        Op3 = Op.copy()
        Op3[2] -= 1
        dfs(Op3, res * A[cnt], cnt)
    if Op[3] > 0:
        Op4 = Op.copy()
        Op4[3] -= 1
        if res < 0 and A[cnt] > 0:
            dfs(Op4, -int(abs(res) / A[cnt]), cnt)
        else:
            dfs(Op4, res // A[cnt], cnt)


N = input()
A = list(map(int, input().split()))
Op = list(map(int, input().split()))

dfs(Op, A[0], 0)

print(str(maxval) + '\n')
print(str(minval))
