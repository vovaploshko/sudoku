from itertools import product

def solve_sudoku(puzzle):
    for (row, col) in product(range(0, 9), repeat=2):
        if puzzle[row][col] == 0:
            for num in range(1, 10):
                allowed = True
                # Перевірка рядка та стовпця
                for i in range(0, 9):
                    if (puzzle[i][col] == num) or (puzzle[row][i] == num):
                        allowed = False
                        break
                # Перевірка 3x3 підгрупи
                for (i, j) in product(range(0, 3), repeat=2):
                    if puzzle[row - row % 3 + i][col - col % 3 + j] == num:
                        allowed = False
                        break
                # Якщо число дозволене, пробуємо далі
                if allowed:
                    puzzle[row][col] = num
                    if solve_sudoku(puzzle):
                        return puzzle
                    else:
                        # Якщо не вдалося, відкатуємо зміну
                        puzzle[row][col] = 0
            return False
    return puzzle


def print_sudoku(puzzle):
    puzzle = [['*' if num == 0 else num for num in row] for row in puzzle]
    print()
    for row in range(0, 9):
        if ((row % 3 == 0) and (row != 0)):
            print('-' * 33)
        for col in range(0, 9):
            if ((col % 3 == 0) and (col != 0)):
                print(' | ', end='')
            print('', puzzle[row][col], '', end='')
        print()
    print()


if __name__ == '__main__':
    puzzle = [
        [9, 8, 5, 4, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [1, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [4, 0, 2, 0, 0, 9, 0, 0, 3],
        [0, 9, 0, 0, 6, 3, 4, 0, 0],
        [0, 6, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 6, 0, 0, 5],
        [2, 0, 0, 0, 8, 0, 0, 0, 1]
    ]

    print("Початкова головоломка:")
    print_sudoku(puzzle)

    solution = solve_sudoku(puzzle)
    if solution:
        print("Розв'язана головоломка:")
        print_sudoku(solution)
    else:
        print("Неможливо знайти рішення.")
