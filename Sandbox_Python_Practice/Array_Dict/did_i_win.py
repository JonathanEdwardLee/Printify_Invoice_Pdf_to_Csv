# Jonathan Lee

def did_i_win_down(player, board):
    # did_win = player == board[0][2] and \
    #           player == board[1][2] and \
    #           player == board[2][2]  
    all_win = False
    for x in range(3):
        did_win = True
        for i in range(3):
            did_win &= player == board[i][x]
        all_win |= did_win
    return all_win


def print_2D(b):
    for i in range(len(b)):
        print("|", end=" ")
        for j in b[i]:
            print(j, end=" ")
        print("|")

def main():
    boards = [
        [["X", "O", "O"]] * 3, \
        [["X", "O", "X"], ["O"]* 3, ["O","X", "O"]], \
        [["O", "O", "X"], ["O", "X", "O"], ["X", "O", "O"]],\
        [["O", "O", "X"]] * 3]
    for b in boards:
         print_2D(b)
         print("*" * 10)
         print("X won?", did_i_win_down("X", b))
         print("O won?", did_i_win_down("O", b))

if __name__ == "__main__":
    main()