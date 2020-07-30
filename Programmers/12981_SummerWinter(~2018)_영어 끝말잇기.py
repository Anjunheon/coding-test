def solution(n, words):
    answer = []

    count = []
    for i in range(n):
        count.append(0)

    check = []
    pre_word = " "
    for idx, word in enumerate(words):
        count[idx % n] += 1

        if (pre_word[len(pre_word) - 1] != word[0] and idx != 0) or (word in check) or (len(word) == 1):
            answer.append(idx % n + 1)
            answer.append(count[idx % n])
            break
        else:
            if idx + 1 == len(words):
                answer.append(0)
                answer.append(0)
                break
            else:
                check.append(word)
                pre_word = word
    return answer