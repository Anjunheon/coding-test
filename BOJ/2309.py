from sys import stdin, stdout

input = stdin.readline
print = stdout.write

H = [int(input()[:-1]) for _ in range(9)]
H = sorted(H)

h = 0
flag = False
for i in range(0, 8):
    for j in range(i+1, 9):
        if sum(H) - H[i] - H[j] == 100:
            H.pop(i)
            H.pop(j-1)
            flag = True
            break
    if flag:
        break

for i in H:
    print(str(i) + '\n')
