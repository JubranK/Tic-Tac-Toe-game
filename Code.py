# Jubran Khoury

import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe by Jubran")

        self.current_player = 'X'
        self.board = [' ']*9
        self.create_board()

    def create_board(self):
        self.status_label = tk.Label(self.master, text="Player X's turn", font=('Helvetica', 14))
        self.status_label.grid(row=0, columnspan=3, pady=10)

        self.buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(self.master, text='', width=10, height=3,
                                   font=('Helvetica', 24), command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i+1, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        self.restart_button = tk.Button(self.master, text="Restart", font=('Helvetica', 14), command=self.reset_board)
        self.restart_button.grid(row=4, columnspan=3, pady=10)

    def make_move(self, row, col):
        index = row * 3 + col
        if self.board[index] == ' ':
            self.buttons[row][col].config(text=self.current_player)
            self.board[index] = self.current_player

            if self.check_winner():
                winner = self.current_player
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.reset_board()
                return

            if ' ' not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
                return

            self.current_player = 'O' if self.current_player == 'X' else 'X'
            self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6)]

        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != ' ':
                return True
        return False

    def reset_board(self):
        self.current_player = 'X'
        self.board = [' ']*9
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state=tk.NORMAL)
        self.status_label.config(text="Player X's turn")

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
