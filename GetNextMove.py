
from asyncore import write
import random
from sys import argv
import chess
from optparse import OptionParser
from evaluation import evaluation
import time

def writeToFile(chessOutput):
    f = open('./players/last_move.txt','w')
    f.write(str(chessOutput))
    f.close()
    # print("ZJminMax Writing to File")

class GetNextMove:
    def __init__(self, fen, time_white, time_black, bonus_time):
        #print('fen from getNextMove init', fen)
        self.board = chess.Board(fen)
        #print(self.board)
        self.time_white = time_white
        self.time_black = time_black
        self.bonus_time = bonus_time
        #print("created a new GetNextMove")
    
    def nextMove(self):
        #chess.STARTING_FEN = self.board
        #print (self.board.legal_moves)
        # for i in range(1,100):
        # for i in range(1,100):
            # print("ahhhhhhhhhhhhhhhhhhhh NEXT ACTION ahhhhhhhhhhhhhhhhhhhhhhhh")
        e = evaluation(self.board)
        move = e.getBestAction()
        self.board.push(move)
        # print(self.board)
            # time.sleep(2)
        writeToFile(move)

        '''
        for i in range(1,100):
            moves = list(self.board.legal_moves)
            move = random.choice(moves)
            self.board.push(move)
            e = evaluation(self.board, self.color)
            e.getBestAction
            score = e.evaluate()
            print("score from evaluation",score)
        '''
            
        #print(e)
        #print(self.board.legal_moves[1])
        

def runTest(fenString):
    #print("hello there")
    #fenString = "rnb1kbnr/ppp2ppp/2p1qp2/8/8/3P1P2/PPP2PPP/RNBQKBNR w KQkq - 0 1"
    
    GM = GetNextMove(fenString,0,0,0)
    GM.nextMove()

if __name__ == "__main__":
    '''
    arg[1] = fenstring
    arg[2] = time_white
    arg[3] = time_black
    arg[4] = bonus_time
    '''
    fenString = argv[1]
    # fenString = "rnbqkbnr/pppppppp/8/8/6P1/8/PPPPPP1P/RNBQKBNR b KQkq - 0 1"
    #fenString = 'rnbqkbnr/pppppppp/PPPPPPP1/7P/8/8/8/RNBQKBNR b KQkq - 0 1'


    '''
    fenString = chess.STARTING_FEN
    newBoard = chess.Board(fenString)
    moves = list(newBoard.legal_moves)
    move = random.choice(moves)
    writeToFile(move)
    '''
    runTest(fenString)
    
        
    
    # print('start \n', newBoard)
    # newBoard.remove_piece_at(chess.A1)
    
    # print('new board',newBoard)

    # #GetNextMove GM = GetNextMove(argv[1], argv[2], argv[3], argv[4])
    

    #makeFile(options)