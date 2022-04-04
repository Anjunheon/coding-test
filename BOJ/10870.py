from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n = int(input())

ans = [0, 1]
for i in range(2, n+1):
    ans.append(ans[i-2] + ans[i-1])

print(str(ans[n]))
