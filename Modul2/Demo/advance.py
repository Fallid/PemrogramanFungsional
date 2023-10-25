_author_ = "Ahmad Naufal"
_copyright_ = "Copyright 2023, malang"

import random

def create_board(size):
    # Buat board matrix dengan ukuran sesuai inputan
    return [[' ' for _ in range(size)] for _ in range(size)]

def generate_position(size):
    # Generate posisi acak untuk bidak dan goals
    return (random.randint(0, size - 1), random.randint(0, size - 1))

def is_valid_move(board, position, direction):
    row, col = position
    size = len(board)

    if direction == 'w':
        return row > 0
    elif direction == 's':
        return row < size - 1
    elif direction == 'a':
        return col > 0
    elif direction == 'd':
        return col < size - 1

def move(board, position, direction):
    if is_valid_move(board, position, direction):
        row, col = position
        new_row, new_col = row, col

        if direction == 'w':
            new_row -= 1
        elif direction == 's':
            new_row += 1
        elif direction == 'a':
            new_col -= 1
        elif direction == 'd':
            new_col += 1

        new_board = [row[:] for row in board]
        new_board[row][col] = '-'
        new_board[new_row][new_col] = 'A'

        return new_board, (new_row, new_col)
    else:
        return board, position

def is_game_won(position, goal):
    return position == goal


def print_board(board, position, goal):
    size = len(board)
    
    # Membuat baris pemisah
    separator = "+---" * size + "+"
    
    for i, row in enumerate(board):
        row_str = ""
        for j, cell in enumerate(row):
            if (i, j) == position:
                row_str += '| A '
            elif (i, j) == goal:
                row_str += '| O '
            else:
                row_str += f'| {cell} '
        print(separator)
        print(row_str + '|')
    
    # Menambahkan baris pemisah terakhir
    print(separator)

get_new_board = lambda position: input(position).lower()
get_size_board = lambda size :int(input(size))

def main():
    size = get_size_board("Masukkan ukuran board: ")
    board = create_board(size)
    goal = generate_position(size)
    position = generate_position(size)
    moves = 0  # Tambahkan hitung langkah
    reattempt = 0
    
    while True:
        print_board(board, position, goal)
        choice =  get_new_board("\nApakah anda ingin menganti position? [yes/no]\n")
        if reattempt == 3:
            print("Tidak bisa mengganti position lebih dari 3 kali! \nMelanjutkan permainan\n")
            break
        if choice == "yes":
            board = create_board(size)
            goal = generate_position(size)
            position = generate_position(size)
        elif choice == "no":
            break
        else:
            print("Pilihan tidak ditemukan atau tidak ada!")
        reattempt = reattempt + 1

    # Loop permainan
    while True:
        print_board(board, position, goal)

        if is_game_won(position, goal):
            print("Anda menang!")
            break

        if moves >= 5:
            print("Anda kalah! Anda tidak mencapai tujuan dalam 5 langkah.")
            break

        direction = input("Masukkan arah up(w)/down(s)/left(a)/right(d)): ")

        board, position = move(board, position, direction)
        moves += 1  # Tambahkan hitungan langkah


if __name__ == "__main__":
   main()