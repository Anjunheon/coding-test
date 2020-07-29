def solution(numbers, hand):
    answer = ''
    keypad = [[3,1], # 0
              [0,0], [0,1], [0,2], # 1,2,3
              [1,0], [1,1], [1,2], # 4,5,6
              [2,0], [2,1], [2,2], # 7,8,9
              [3,0], [3,2]] # *,#
    lh = 10
    rh = 11
    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            lh = numbers[i]
            answer = answer + 'L'
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            rh = numbers[i]
            answer = answer + 'R'
        else:
            ldist = abs(keypad[numbers[i]][0] - keypad[lh][0]) + abs(keypad[numbers[i]][1] - keypad[lh][1])
            rdist = abs(keypad[numbers[i]][0] - keypad[rh][0]) + abs(keypad[numbers[i]][1] - keypad[rh][1])
            if ldist < rdist:
                lh = numbers[i]
                answer = answer + 'L'
            elif ldist > rdist:
                rh = numbers[i]
                answer = answer + 'R'
            else:
                if hand == 'left':
                    lh = numbers[i]
                    answer = answer + 'L'
                else:
                    rh = numbers[i]
                    answer = answer + 'R'
    return answer