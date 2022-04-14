from sys import stdin, stdout

input = stdin.readline
print = stdout.write

H, W = map(int, input().split())
block = list(map(int, input().split()))

dim = [[0 for j in range(W)] for i in range(H)]

for i in range(W):
    for j in range(block[i]):
        dim[j][i] = 1

answer = 0
for i in range(H):
    flag = False
    cnt = 0
    for j in range(W):
        if flag:
            if dim[i][j] == 0:
                cnt += 1
            else:
                answer += cnt
                cnt = 0
        else:
            if dim[i][j] == 1:
                flag = True


print(str(answer))
