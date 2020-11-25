# write your code here
class Board:
    def __init__(self, parse):
        self.moves = [[parse[y * 3 + x] for x in range(3)] for y in range(3)]
        if not self.check_signs():
            print("wrong input")

    def print_canvas(self):
        print("---------")
        for col in range(3):
            print("|", end=" ")
            for row in range(3):
                print(self.moves[col][row], end = ' ')
            print("|")
        print("---------")

    def check_signs(self):
        tab = ['X', 'O', '_', 'x', 'o']
        for x in self.moves:
            if x not in self.moves:
                return False
        return True

    def is_three(self, sign):

        for y in range(3):
            counter = 0
            for x in range(3):
                if self.moves[y][x] == sign:
                    counter += 1
            if counter == 3:
                print("first return, self.moves[y][x]", self.moves[y][x])
                return True

        for x in range(3):
            counter = 0
            for y in range(3):
                if self.moves[y][x] == sign:
                    counter += 1
            if counter == 3:
                print("second return")
                return True

        if self.moves[0][0] == sign and self.moves[1][1] == sign and self.moves[2][2] == sign:
            print("third return")
            return True
        if self.moves[0][2] == sign and self.moves[1][1] == sign and self.moves[2][0] == sign:
            print("forth return")
            return True

        return False

    def is_full(self):
        counter_x = 0
        counter_y = 0
        for rows in self.moves:
            for col_in_row in rows:
                if col_in_row == 'X':
                    counter_x += 1
                if col_in_row == 'O':
                    counter_y += 1
        if counter_x + counter_y < 8:
            return False
        else:
            return True

    def isImpossible(self):
        counter_x = 0
        counter_y = 0
        for rows in self.moves:
            for col_in_row in rows:
                if col_in_row == 'X':
                    counter_x += 1
                if col_in_row == 'O':
                    counter_y += 1
        if abs(counter_x - counter_y) > 1:
            return True
        else:
            return False

    def who_wins(self):
        player1 = self.is_three('X')
        player2 = self.is_three('O')

        if player1 == True and player2 == False:
            return "X wins"
        if player1 == False and player2 == True:
            return "O wins"
        if player1 == False and player2 == False and self.is_full():
            return "Draw"
        if player1 == player2 == True:
            return "Impossible"
        if self.isImpossible():
            return "Impossible"
        if not self.is_full():
            return "Game not finished"
        return "We reached end, something gone wrong"


    def is_cell_empty(self, x_cor, y_cor):
        #if self.moves[x_cor - 1][y_cor - 1] == 'X' or self.moves[x_cor - 1][y_cor - 1] == 'O':
        if self.moves[3 - y_cor][x_cor - 1] == 'X' or self.moves[3 - y_cor][x_cor - 1] == 'O':
            print("This cell is occupied! Choose another one!")
            return False
        else:
            return True


    def is_input_correct(self, x_cor, y_cor):
        if "".join([x_cor, y_cor]).isdigit():
            if 1 <= int(x_cor) <=3 and 1 <= int(y_cor) <=3:
                return True
            else:
                print("Coordinates should be from 1 to 3!")
                return False
        else:
            print("You should enter numbers!")
            return False


    def new_move(self):
        while True:
            print("Enter the coordinates:")
            x_cor, y_cor = input().split()
            if self.is_input_correct(x_cor, y_cor):
                x_cor, y_cor = int(x_cor), int(y_cor)
                if self.is_cell_empty(x_cor, y_cor):
                    self.moves[3 - y_cor][x_cor - 1] = 'X'
                    self.print_canvas()
                    break


game1 = Board(input())
game1.print_canvas()
#print(game1.who_wins())
game1.new_move()

# game = [[moves[y * 3 + x] for x in range(3)]for y in range(3)]
