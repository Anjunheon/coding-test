def solution(board, moves):
    answer = 0
    basket = []
    for i in range(len(moves)):
        loc = moves[i] - 1
        for j in range(len(board)):
            if (board[j][loc] != 0):
                basket.append(board[j][loc])
                board[j][loc] = 0
                if (len(basket) >= 2):
                    if (basket[len(basket) - 2] == basket[len(basket) - 1]):
                        basket.pop()
                        basket.pop()
                        answer = answer + 2
                break
    return answer