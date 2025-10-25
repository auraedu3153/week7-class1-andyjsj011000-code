# 요구사항은 https://www.acmicpc.net/problem/1018을 확인하세요
def min_count_of_squares(board: list[list[str]]) -> int:
    n = len(board)
    m = len(board[0])

    def function(start_index_row, start_index_column):
        W_ans = 0
        B_ans = 0
        for i in range(start_index_row, start_index_row+8):
            for j in range(start_index_column, start_index_column+8):
                if board[i][j] == "B":
                    if (i - start_index_row + j - start_index_column) % 2 ==0: W_ans += 1
                    else: B_ans += 1 
                if board[i][j] == "W":
                    if (i - start_index_row + j - start_index_column) % 2 ==1: W_ans += 1
                    else: B_ans += 1  
        if B_ans <= W_ans: return B_ans
        else: return W_ans


    min = 64
    for i in range(0, n-7):
        for j in range(0, m-7):
            x = function(i,j)
            if min > x:
                min = x 
    return min

board = [['W'] * 8 for _ in range(8)]
print(min_count_of_squares(board))