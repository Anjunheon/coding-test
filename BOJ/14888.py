from sys import stdin, stdout

input = stdin.readline
print = stdout.write

minval = 1000000000
maxval = -1000000000

cnt = 0


def dfs(Op, res):
    global minval, maxval, cnt
    cnt += 1

    if sum(Op) == 0:
        minval = min(minval, res)
        maxval = max(maxval, res)

    if Op[0] > 0:
        Op[0] -= 1
        dfs(Op, res + A[cnt])
    if Op[1] > 0:
        Op[1] -= 1
        dfs(Op, res - A[cnt])
    if Op[2] > 0:
        Op[2] -= 1
        dfs(Op, res * A[cnt])
    if Op[3] > 0:
        Op[3] -= 1
        if res < 0:
            dfs(Op, -(abs(res) // A[cnt]))
        if res > 0:
            dfs(Op, abs(res) / A[cnt])


N = input()
A = list(map(int, input().split()))
Op = list(map(int, input().split()))

dfs(Op, A[0])

print(str(maxval) + '\n')
print(str(minval))
