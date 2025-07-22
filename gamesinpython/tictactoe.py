import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("300x350")
root.resizable(False, False)

# Global game variables
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

# Function to check for a win
def check_winner():
    # Rows, columns and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    return None

# Function to check for draw
def is_draw():
    for row in board:
        if "" in row:
            return False
    return True

# Function to handle button click
def on_click(row, col):
    global current_player

    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_board()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to reset the board
def reset_board():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="")

# Create a grid of buttons
frame = tk.Frame(root)
frame.pack(pady=20)

for i in range(3):
    for j in range(3):
        button = tk.Button(frame, text="", font=("Arial", 20), width=5, height=2,
                           command=lambda r=i, c=j: on_click(r, c))
        button.grid(row=i, column=j)
        buttons[i][j] = button

# Reset button
reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 12), command=reset_board)
reset_btn.pack(pady=10)

# Start the GUI loop
root.mainloop()
