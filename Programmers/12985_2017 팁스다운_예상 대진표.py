def solution(n, a, b):
    answer = 1

    if a > b:
        tmp = a
        a = b
        b = tmp

    while ((abs(a - b) != 1) or (a % 2 != 1)):
        q = int(a / 2)
        if q == 0:
            a = 1
        elif a == q * 2:
            a = q
        else:
            a = q + 1

        q = int(b / 2)
        if q == 0:
            b = 1
        elif b == q * 2:
            b = q
        else:
            b = q + 1
        answer += 1

    return answer