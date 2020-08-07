import sys

n = int(sys.stdin.readline())
for i in range(n):
    left = []
    right = []
    s = sys.stdin.readline().strip()
    for i in s:
        if i == '-':
            if len(left) > 0:
                left.pop()
        elif i == '<':
            if len(left) > 0:
                right.append(left.pop())
        elif i == '>':
            if len(right) > 0:
                left.append(right.pop())
        else:
            left.append(i)
    left = ''.join(left)
    right = ''.join(reversed(right))
    print(left+right)