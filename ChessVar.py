# Author: Ho Gia Bao Le
# GitHub username: baole-schools
# Date: 03/16/2025
# Description: Implements an abstract board game based on a chess variant known as "King Of The Hills".
#              The game ends when a player's king is captured and that player loses, or when one player's king
#              moves to one of the four central squares and that player wins.

# Creates Piece and its child classes.
class Piece:
    """
    Represents a chess piece object.
    """
    def __init__(self, player):
        """
        Creates a chess piece object with 1 private data member.
        :param player: The color representing the player - 'white' or 'black'.
        """
        self._player = player

    def get_player(self):
        """
        Returns the private data member player.
        """
        return self._player

class Pawn(Piece):
    """
    Represents a pawn object, inheriting from the Piece class.
    """
    def check_valid_move(self, board, start_square, end_square):
        """
        Returns the boolean value of whether the pawn move is valid.
        :param board: The current state of the chess board.
        :param start_square: The starting position in algebraic notation.
        :param end_square: The ending position in algebraic notation.
        """
        start_row, start_col = convert_position(start_square)
        end_row, end_col = convert_position(end_square)

        # Checks white pawn.
        if self._player == 'white':

            # Check if straight moves.
            if start_col == end_col and board[end_row][end_col] == ' ':
                if start_row == 6 and end_row == 4 and board[5][end_col] == ' ':
                    return True
                if start_row <= 6 and end_row - start_row == -1:
                    return True

            # Diagonal captures.
            if abs(end_col - start_col) == 1 and end_row - start_row == -1:
                if board[end_row][end_col] != ' ' and board[end_row][end_col].get_player() == 'black':
                    return True

        # Checks black pawn.
        if self._player == 'black':

            # Checks if straight moves.
            if start_col == end_col and board[end_row][end_col] == ' ':
                if start_row == 1 and end_row == 3 and board[2][end_col] == ' ':
                    return True
                if start_row >= 1 and end_row - start_row == 1:
                    return True

            # Checks if diagonal captures.
            if abs(end_col - start_col) == 1 and end_row - start_row == 1:
                if board[end_row][end_col] != ' ' and board[end_row][end_col].get_player() == 'white':
                    return True

        # Otherwise.
        return False

    def get_symbol(self):
        """
        Returns the symbol represent the pawn chess piece. 'P' for white pawn and 'p' for black pawn.
        """
        if self._player == 'white':
            return 'P'
        else:
            return 'p'

class Rook(Piece):
    """
    Represents a rook object, inheriting from the Piece class.
    """
    def check_valid_move(self, board, start_square, end_square):
        """
        Returns the boolean value of whether the rook move is valid.
        :param board: The current state of the chess board.
        :param start_square: The starting position in algebraic notation.
        :param end_square: The ending position in algebraic notation.
        """
        start_row, start_col = convert_position(start_square)
        end_row, end_col = convert_position(end_square)

        # Checks if straight.
        if start_row == end_row or start_col == end_col:

            # Checks if path blocked.
                # Calculates the counting step.
            step_row = 0
            step_col = 0
            if start_row == end_row:                                                            # Vertically parallel
                step_col = 1 if end_col - start_col > 0 else -1
            elif start_col == end_col:                                                          # Horizontally parallel
                step_row = 1 if end_row - start_row > 0 else -1

                # Loops between the start and end positions.
            while (start_row, start_col) != (end_row - step_row, end_col - step_col):
                start_row += step_row
                start_col += step_col
                if board[start_row][start_col] != ' ':
                    return False
            return True

        # Otherwise.
        return False

    def get_symbol(self):
        """
        Returns the symbol represent the rook chess piece. 'R' for white rook and 'r' for black rook.
        """
        if self._player == 'white':
            return 'R'
        else:
            return 'r'

class Knight(Piece):
    """
    Represents a knight object, inheriting from the Piece class.
    """
    def check_valid_move(self, board, start_square, end_square):
        """
        Returns the boolean value of whether the knight move is valid.
        :param board: The current state of the chess board.
        :param start_square: The starting position in algebraic notation.
        :param end_square: The ending position in algebraic notation.
        """
        start_row, start_col = convert_position(start_square)
        end_row, end_col = convert_position(end_square)

        # Checks if one dimension is 2 and one dimension is 1.
        return (abs(end_row - start_row), abs(end_col - start_col)) in [(1, 2), (2, 1)]

    def get_symbol(self):
        """
        Returns the symbol represent the knight chess piece. 'N' for white knight and 'n' for black knight.
        """
        if self._player == 'white':
            return 'N'
        else:
            return 'n'

class Bishop(Piece):
    """
    Represents a bishop object, inheriting from the Piece class.
    """
    def check_valid_move(self, board, start_square, end_square):
        """
        Returns the boolean value of whether the bishop move is valid.
        :param board: The current state of the chess board.
        :param start_square: The starting position in algebraic notation.
        :param end_square: The ending position in algebraic notation.
        """
        start_row, start_col = convert_position(start_square)
        end_row, end_col = convert_position(end_square)

        # Checks if diagonal.
        if abs(end_row - start_row) == abs(end_col - start_col):

            # Checks if path blocked.
                # Calculates the counting steps.
            step_row = 1 if (end_row - start_row) > 0 else -1
            step_col = 1 if (end_col - start_col) > 0 else -1

                # Loops between the start and end positions.
            while (start_row, start_col) != (end_row - step_row, end_col - step_col):
                start_row += step_row
                start_col += step_col
                if board[start_row][start_col] != ' ':
                    return False
            return True

        # Otherwise.
        return False

    def get_symbol(self):
        """
        Returns the symbol represent the bishop chess piece. 'B' for white bishop and 'b' for black bishop.
        """
        if self._player == 'white':
            return 'B'
        else:
            return 'b'

class Queen(Piece):
    """
    Represents a queen object, inheriting from the Piece class.
    """
    def check_valid_move(self, board, start_square, end_square):
        """
        Returns the boolean value of whether the queen move is valid.
        :param board: The current state of the chess board.
        :param start_square: The starting position in algebraic notation.
        :param end_square: The ending position in algebraic notation.
        """
        # Checks if straight like Rook.
        if Rook(self._player).check_valid_move(board, start_square, end_square):
            return True

        # Checks if diagonal like Bishop.
        if Bishop(self._player).check_valid_move(board, start_square, end_square):
            return True

        # Otherwise.
        return False

    def get_symbol(self):
        """
        Returns the symbol represent the bishop chess piece. 'B' for white bishop and 'b' for black bishop.
        """
        if self._player == 'white':
            return 'Q'
        else:
            return 'q'

class King(Piece):
    """
    Represents a king object, inheriting from the Piece class.
    """
    def check_valid_move(self, board, start_square, end_square):
        """
        Returns the boolean value of whether the queen move is valid.
        :param board: The current state of the chess board.
        :param start_square: The starting position in algebraic notation.
        :param end_square: The ending position in algebraic notation.
        """
        start_row, start_col = convert_position(start_square)
        end_row, end_col = convert_position(end_square)

        # Checks if moves 1 straightly or diagonally.
        return abs(end_row - start_row) <= 1 and abs(end_col - start_col) <= 1

    def get_symbol(self):
        """
        Returns the symbol represent the king chess piece. 'K' for white king and 'k' for black king.
        """
        if self._player == 'white':
            return 'K'
        else:
            return 'k'

# Creates convert_position function.
def convert_position(notation):
    """
    Converts positions from algebraic notation into a pair of indices that correspond to their location in the board list.
    :param notation: The algebraic notation of position.
    """
    # Invalid notation.
    if len(notation) != 2:
        return None
    if notation[0] < 'a' or notation[0] > 'h' or notation[1] < '1' or notation[1] > '8':
        return None

    # Converts to indices for the nested list.
    conv_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    column = conv_dict[notation[0]]
    row = 8 - int(notation[1])
    return row, column

# Creates the ChessVar class:
class ChessVar:
    """
    Represent a ChessVar object.
    """
    def __init__(self):
        """
        Creates a ChessVar object, initialized with 3 private data members.
        """
        # Initializes the chess board with chess piece objects.
        self._board = [
        [Rook('black'), Knight('black'), Bishop('black'), Queen('black'), King('black'), Bishop('black'), Knight('black'), Rook('black')],
        [Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black')],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white')],
        [Rook('white'), Knight('white'), Bishop('white'), Queen('white'), King('white'), Bishop('white'), Knight('white'), Rook('white')]]

        # Initializes the game state to 'UNFINISHED'.
        self._game_state = 'UNFINISHED'

        # 'white' player moves first.
        self._current_turn = 'white'

    def get_real_board(self):
        """
        Returns the private data member ._board.
        """
        return self._board

    def get_board(self):
        """
        Returns the chess board with chess pieces as symbols.
        """
        board_print = [[' ' if piece == ' ' else piece.get_symbol() for piece in row] for row in self._board]
        return board_print

    def get_game_state(self):
        """
        Returns the private data member ._game_state 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'.
        """
        return self._game_state

    def get_current_turn(self):
        """
        Returns the private data member ._current_turn 'white' or 'black'.
        """
        return self._current_turn

    def make_move(self, start_square, end_square):
        """
        Returns a boolean value whether the move is successful.
            If True, updates game_state, current_turn, and board.
            Otherwise, returns False.
        :param start_square: A string representing the square moved from.
        :param end_square: A string representing the square moved to.
        """
        # Checks if invalid moves.
        if self._game_state != 'UNFINISHED':                                                    # Game finished
            return False
        if convert_position(start_square) is None or convert_position(end_square) is None:      # Out of bounds
            return False
        if start_square == end_square:                                                          # Stay still
            return False

        # Converts positions and set up the squares.
        start_row, start_col = convert_position(start_square)
        end_row, end_col = convert_position(end_square)
        piece = self._board[start_row][start_col]                                               # Starting square
        target = self._board[end_row][end_col]                                                  # Ending square

        # Checks if invalid moves.
        if piece == ' ' or piece.get_player() != self._current_turn:                            # No/Wrong piece at start
            return False
        if target != ' ' and target.get_player() == self._current_turn:                         # Target square has the same player's piece
            return False
        if piece.check_valid_move(self._board, start_square, end_square) is False:              # Rule violation
            return False

        # Otherwise, valid moves.
            # Checks if Endgames - King of the Hill
        if end_square in ['d4', 'e4', 'd5', 'e5'] and piece.get_symbol().lower() == 'k':
            if self._current_turn == 'white':
                self._game_state = 'WHITE_WON'
            else:
                self._game_state = 'BLACK_WON'

            # Checks if Endgames - King captured
        if target != ' ' and target.get_symbol().lower() == 'k':
            if self._current_turn == 'white':
                self._game_state = 'WHITE_WON'
            else:
                self._game_state = 'BLACK_WON'

            # Updates the board
        self._board[end_row][end_col] = piece
        self._board[start_row][start_col] = ' '

            # Switches turn
        if self._current_turn == 'white':
            self._current_turn = 'black'
        else:
            self._current_turn = 'white'
        return True

# Tests.
def main():
    """
    Runs if the file is run as a script, but not if it is imported to another file.
    """
    game = ChessVar()
    game.get_board()
    print(game.make_move('e2', 'e4'))       # True
    print(game.make_move('a2', 'a4'))
    print(game.make_move('a?', '!b'))
    print(game.make_move('d7', 'd5'))       # True
    print(game.make_move('a7', 'a5'))
    print(game.make_move('d1', 'h5'))       # True
    print(game.make_move('c8', 'a6'))
    print(game.make_move('f7', 'f5'))       # True
    print(game.make_move('', '????'))
    print(game.make_move('h5', 'e8'))       # True
    print(game.make_move('b8', 'a6'))
    for element in game.get_board():
        print(element)                                      # White captures Black King
    print(game.get_game_state() + "\n")                     # WHITE_WON

    game = ChessVar()
    game.get_board()
    print(game.make_move('a2', 'a4'))       # True
    print(game.make_move('e7', 'e5'))       # True
    print(game.make_move('h2', 'g2'))
    print(game.make_move('h2', 'h4'))       # True
    print(game.make_move('e8', 'e7'))       # True
    print(game.make_move('h1', 'h5'))
    print(game.make_move('f1', 'a6'))
    print(game.make_move('b1', 'a3'))       # True
    print(game.make_move('e7', 'e6'))       # True
    print(game.make_move('x1', 'h0'))
    print(game.make_move('h1', 'h3'))       # True
    print(game.make_move('e6', 'e5'))
    print(game.make_move('e6', 'd5'))       # True
    for element in game.get_board():
        print(element)                                      # Black King of the Hill
    print(game.get_game_state())                            # BLACK_WON

if __name__ == '__main__':
    main()