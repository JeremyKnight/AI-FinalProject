
import random
from sys import argv
import chess
from optparse import OptionParser

def writeToFile(chessOutput):
    f = open('../last_move.txt','w')
    f.write(str(chessOutput))
    f.close()

class GetNextMove:
    def __init__(self, fen, time_white, time_black, bonus_time):
        print('fen from getNextMove init', fen)
        self.board = chess.Board(fen)
        print(self.board)
        self.time_white = time_white
        self.time_black = time_black
        self.bonus_time = bonus_time
        print("created a new GetNextMove")
    
    def nextMove(self):
        #chess.STARTING_FEN = self.board
        print (self.board.legal_moves)
        #print(self.board.legal_moves[1])

if __name__ == "__main__":
    '''
    arg[1] = fenstring
    arg[2] = time_white
    arg[3] = time_black
    arg[4] = bonus_time
    '''
    fenString = argv[1]
    newBoard = chess.Board(fenString)
    moves = list(newBoard.legal_moves)
    move = random.choice(moves)
    writeToFile(move)
    # print('start \n', newBoard)
    # newBoard.remove_piece_at(chess.A1)
    
    # print('new board',newBoard)

    # #GetNextMove GM = GetNextMove(argv[1], argv[2], argv[3], argv[4])
    # GM = GetNextMove(newBoard.fen(),0,0,0)
    # GM.nextMove()

    #makeFile(options)