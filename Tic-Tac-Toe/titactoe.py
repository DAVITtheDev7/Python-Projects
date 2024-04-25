class TicTacToe:
    def __init__(self):
        self.board = [' ' for x in range(9)]

    def print_board(self):
        row1 = "| {} | {} | {} |".format(self.board[0], self.board[1], self.board[2])
        row2 = "| {} | {} | {} |".format(self.board[3], self.board[4], self.board[5])
        row3 = "| {} | {} | {} |".format(self.board[6], self.board[7], self.board[8])

        print()
        print(row1)
        print(row2)
        print(row3)
        print()

    def player_move(self, icon, number):
        print("Your turn player {}".format(number))
        try:
            choice = int(input("Enter your move (1-9): ").strip())
            if self.board[choice - 1] == ' ':
                self.board[choice - 1] = icon
            else:
                print()
                print("That space is already taken!")
        except IndexError:
            print("Please enter the number from 1 to 9!")
        except ValueError:
            print("Please enter integers!")

    def is_victory(self, icon):
        if (self.board[0] == icon and self.board[1] == icon and self.board[2] == icon) or \
           (self.board[3] == icon and self.board[4] == icon and self.board[5] == icon) or \
           (self.board[6] == icon and self.board[7] == icon and self.board[8] == icon) or \
           (self.board[0] == icon and self.board[3] == icon and self.board[6] == icon) or \
           (self.board[1] == icon and self.board[4] == icon and self.board[7] == icon) or \
           (self.board[2] == icon and self.board[5] == icon and self.board[8] == icon) or \
           (self.board[0] == icon and self.board[4] == icon and self.board[8] == icon) or \
           (self.board[2] == icon and self.board[4] == icon and self.board[6] == icon):
            return True
        else:
            return False

    def is_draw(self):
        if ' ' not in self.board:
            return True
        else:
            return False

game = TicTacToe()

while True:
    game.print_board()
    game.player_move('X', 1)
    game.print_board()
    if game.is_victory('X'):
        print("X wins! Congratulations!")
        break
    elif game.is_draw():
        print("It's a draw!")
        break
    game.player_move('O', 2)
    if game.is_victory('O'):
        game.print_board()
        print("O wins! Congratulations!")
        break
    elif game.is_draw():
        print("It's a draw!")
        break
