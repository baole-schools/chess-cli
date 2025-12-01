# chess-cli

This is the portfolio program for my class CS162.
This is an abstract board game based on a chess variant known as "King Of The Hills". Pieces move and capture the same way as in standard chess, but there are no checks, checkmates, castling, en passant, or pawn promotion. Players are not informed if their king is in check, and both staying in check or moving into check are legal moves, though they may result in the king being captured and losing the game. The objective is not to checkmate the king but to capture it. You can also win the game by bringing your king to one of the four central squares of the board. That means the game ends when a player's king is captured and that player loses, or when one player's king moves to one of the four central squares(d4, e4, d5, and e5) and that player wins. Like in standard chess, pawns can move two spaces forward on their first move, but only one space on subsequent moves.

Example call:
```
game = ChessVar()
print(game.make_move('d2', 'd4'))
print(game.make_move('g7', 'g5'))
print(game.make_move('c1', 'g5'))
print(game.make_move('e7', 'e6'))
print(game.make_move('g5', 'd8'))
print(game.get_board())
```
Example output:
```
True
True
True
True
True
[
 ['r', 'n', 'b', 'B', 'k', 'b', 'n', 'r'], 
 ['p', 'p', 'p', 'p', ' ', 'p', ' ', 'p'], 
 [' ', ' ', ' ', ' ', 'p', ' ', ' ', ' '], 
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
 [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' '], 
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
 ['P', 'P', 'P', ' ', 'P', 'P', 'P', 'P'], 
 ['R', 'N', ' ', 'Q', 'K', 'B', 'N', 'R']
]

```
