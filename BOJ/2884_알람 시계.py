time = input()
h, m = time.split()
H = int(h)
M = int(m)

if M < 45:
    if H == 0:
        H = 23
    else:
        H -= 1
    M = 60 - (45 - M)
else:
    M -= 45

print(str(H), str(M))