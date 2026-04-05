def create_grid():
    return [[None for col in range(3)] for row in range(3)]


def print_grid(board):
    for i in range(3):
        print_row = ""
        for j in range(3):
            box = " " if board[i][j] is None else str(board[i][j])
            print_row += f"{box:^7}"
            if j < 2:
                print_row += "|"
        print(print_row)
        if i < 2:
            line_len = 3 * 7 + 2
            print("-" * line_len)


def get_position(used_p):
    while True:
        position = int(input("Enter The Position (1-9): "))
        if position < 1 or position > 9:
            print("Invalid Position, Try Again!")
            continue
        if position in used_p:
            print("Invalid Position, Try Again!")
            continue
        return position


def get_value(used_v):
    while True:
        val = int(input("Enter The Value (1-9): "))
        if val < 1 or val > 9:
            print("Invalid Value, Try Again!")
            continue
        if val in used_v:
            print("Invalid Value, Try Again!")
            continue
        return val


def get_num(cell):
    return int(cell.split("_")[1])


def check_winner(board):
    for row in board:
        if None not in row and sum(get_num(cell) for cell in row) == 15:
            return True

    for col in range(3):
        column = [board[row][col] for row in range(3)]
        if None not in column and sum(get_num(cell) for cell in column) == 15:
            return True

    diag1 = board[0][0], board[1][1], board[2][2]
    diag2 = board[0][2], board[1][1], board[2][0]

    if None not in diag1 and sum(get_num(cell) for cell in diag1) == 15:
        return True

    if None not in diag2 and sum(get_num(cell) for cell in diag2) == 15:
        return True

    return False


def is_draw(board):
    return all(None not in row for row in board)


print(f"\nWelcome to TicTacToe...")
while True:
    board = create_grid()
    used_p = []
    used_v = []
    current_user = "Player 1"
    user = "U1"
    while True:
        print(f"\n{current_user}'s Turn")
        position = get_position(used_p)
        used_p.append(position)

        val = get_value(used_v)
        used_v.append(val)

        row = (position - 1) // 3
        col = (position - 1) % 3
        board[row][col] = f"{user}_{val}"
        print("\n🎯 Target Sum: 15\n")
        print_grid(board)

        if check_winner(board):
            print(f"\nCongrats!, {current_user} Won")
            break

        if is_draw(board):
            print("\nIt's a Draw\n")
            break

        current_user = "Player 2" if current_user == "Player 1" else "Player 1"
        user = "U2" if user == "U1" else "U1"

    play = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play != "yes":
        print("\nExiting...Thanks for playing\n")
        break
