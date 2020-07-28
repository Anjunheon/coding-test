def solution(A, B):
    answer = 0
    A.sort()
    B.sort()

    i = 0
    j = 0
    while i < len(B):
        if A[j] < B[i]:
            answer += 1
            j += 1
        i += 1
    return answer