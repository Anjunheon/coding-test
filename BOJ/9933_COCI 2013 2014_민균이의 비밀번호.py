import sys

N = int(sys.stdin.readline())
filename = []
for i in range(N):
    s = sys.stdin.readline().strip()
    filename.append(s)

for name in filename:
    s = name[::-1]
    if s in filename:
        print(len(name), name[int(len(name) / 2)])
        break