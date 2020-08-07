def solution(N, stages):
    answer = []
    fail = []
    idx = len(stages)

    for i in range(1, N + 1):
        if stages.count(i) == 0:
            fail.append(0)
        else:
            fail.append(stages.count(i) / idx)
            idx -= stages.count(i)

    for _ in range(N):
        answer.append(fail.index(max(fail)) + 1)
        fail[fail.index(max(fail))] = -1

    return answer