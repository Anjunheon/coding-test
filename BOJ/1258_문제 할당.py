import sys

N = int(sys.stdin.readline().strip())

m = []
for _ in range(N):
    prob = []
    a = (sys.stdin.readline().strip()).split()
    for i in range(N):
        prob.append(int(a[i]))
    m.append(prob)

# p = []
# for _ in range(N):
#     p.append(-1)
#
# for i in range(N):
#     c = min(m[i])
#     if c in p:

c = min(min(m))
print(c)