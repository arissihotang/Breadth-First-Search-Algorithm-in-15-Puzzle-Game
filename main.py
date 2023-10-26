import tkinter as tk
import random
from puzzle15 import Puzzle15

def create_board():
    numbers = list(range(1, 16))
    random.shuffle(numbers)
    numbers.append(' ')
    return numbers

def button_click(index):
    empty_index = board.index(' ')

    if index + 1 == empty_index and index % 4 != 3:  # Right tile
        shift_empty_space(index)

    elif index - 1 == empty_index and index % 4 != 0:  # Left tile
        shift_empty_space(index)

    elif index + 4 == empty_index:  # Bottom tile
        shift_empty_space(index)

    elif index - 4 == empty_index:  # Top tile
        shift_empty_space(index)

def shift_empty_space(index):
    empty_index = board.index(' ')
    board[index], board[empty_index] = board[empty_index], board[index]
    update_board()

def update_board():
    for i in range(16):
        text = str(board[i])

        if text == ' ':
            text = ''

        buttons[i].config(text=text)

def bfs():
    numbers = [str(num) if num != ' ' else '0' for num in board]
    board_int = [int(num) if num else 0 for num in numbers]

    initial_state = board_int
    puzzle = Puzzle15(initial_state)

    solution = puzzle.solve()

    if solution is not None:
        message_label.configure(text=f"Solution Found\nMoves: {solution}")

    else:
        message_label.configure(text="Solution Not Found.")

def edit_board():
    top = tk.Toplevel(root)
    top.title("Edit Board")

    entry_frame = tk.Frame(top)
    entry_frame.pack(padx=10, pady=10)

    entries = []

    for i in range(16):
        entry = tk.Entry(entry_frame, width=6)
        entry.grid(row=i // 4, column=i % 4, padx=5, pady=5)
        entry.insert(0, str(board[i]))
        entries.append(entry)

    def save_changes():
        for i in range(16):

            value = entries[i].get()

            if value:
                board[i] = value

            else:
                board[i] = ' '

        top.destroy()
        update_board()

    save_button = tk.Button(top, text="Save", command=save_changes)
    save_button.pack(pady=10)

board = create_board()

root = tk.Tk()
root.title("Puzzle 15")

button_frame = tk.Frame(root)
button_frame.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = []

for i in range(16):
    text = str(board[i])

    if text == ' ':
        text = ''

    button = tk.Button(button_frame, text=text, width=6, height=3,
                       command=lambda idx=i: button_click(idx))
    button.grid(row=i // 4, column=i % 4, padx=5, pady=5)
    buttons.append(button)

edit_button = tk.Button(root, text="Edit Board", command=edit_board)
edit_button.grid(row=1, column=0, columnspan=4, pady=10)

numbers_button = tk.Button(root, text="BFS", command=bfs)
numbers_button.grid(row=2, column=0, columnspan=4, pady=10)

message_label = tk.Label(root, text="")
message_label.grid(row=3, column=0, columnspan=4, pady=10)

root.mainloop()
