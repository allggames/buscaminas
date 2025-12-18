import random

def generate_minesweeper_board(size, num_mines):
    board = [[0 for _ in range(size)] for _ in range(size)]
    mines = set()

    while len(mines) < num_mines:
        mine = (random.randint(0, size - 1), random.randint(0, size - 1))
        if mine not in mines:
            mines.add(mine)
            x, y = mine
            board[x][y] = -1

            for i in range(max(0, x - 1), min(size, x + 2)):
                for j in range(max(0, y - 1), min(size, y + 2)):
                    if board[i][j] != -1:
                        board[i][j] += 1

    return board

def display_board(board, revealed):
    size = len(board)
    for i in range(size):
        for j in range(size):
            if revealed[i][j]:
                if board[i][j] == -1:
                    print("*", end=" ")
                else:
                    print(board[i][j], end=" ")
            else:
                print(".", end=" ")
        print()

def check_victory(board, revealed):
    size = len(board)
    for i in range(size):
        for j in range(size):
            if board[i][j] != -1 and not revealed[i][j]:
                return False
    return True

def main():
    print("Welcome to Minesweeper!")
    size = int(input("Enter board size: "))
    num_mines = int(input("Enter number of mines: "))

    if num_mines >= size * size:
        print("Too many mines for this board size. Exiting.")
        return

    board = generate_minesweeper_board(size, num_mines)
    revealed = [[False for _ in range(size)] for _ in range(size)]

    while True:
        display_board(board, revealed)
        try:
            x, y = map(int, input("Enter coordinates to reveal (row and column): ").split())
            if x < 0 or x >= size or y < 0 or y >= size:
                print("Invalid coordinates. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
            continue

        if board[x][y] == -1:
            print("You hit a mine! Game Over.")
            return

        revealed[x][y] = True

        if check_victory(board, revealed):
            display_board(board, revealed)
            print("Congratulations! You cleared the board!")
            return

if __name__ == "__main__":
    main()