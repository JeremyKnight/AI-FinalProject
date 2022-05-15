import chess
import time

#################################################
# Table of positions found at: 
# https://github.com/astoeckl/mediumchess/blob/master/Blog1.ipynb
##############################################################
pieceWeight = [0,10,40,40,70,90,200]
    # "pawn": 10,
    # "knight": 40,
    # "bishop": 40,
    # "rook":70,
    # "queen": 90,
    # "king": 2000

pawntable = [
 0,  0,  0,  0,  0,  0,  0,  0,
 5, 10, 10,-20,-20, 10, 10,  5,
 5, -5,-10,  0,  0,-10, -5,  5,
 0,  0,  0, 20, 20,  0,  0,  0,
 5,  5, 10, 25, 25, 10,  5,  5,
10, 10, 20, 30, 30, 20, 10, 10,
50, 50, 50, 50, 50, 50, 50, 50,
 0,  0,  0,  0,  0,  0,  0,  0]

knightstable = [
-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  5,  5,  0,-20,-40,
-30,  5, 10, 15, 15, 10,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 10, 15, 15, 10,  0,-30,
-40,-20,  0,  0,  0,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50]

bishopstable = [
-20,-10,-10,-10,-10,-10,-10,-20,
-10,  5,  0,  0,  0,  0,  5,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10,-10,-10,-10,-10,-20]

rookstable = [
  0,  0,  0,  5,  5,  0,  0,  0,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
  5, 10, 10, 10, 10, 10, 10,  5,
 0,  0,  0,  0,  0,  0,  0,  0]

queenstable = [
-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  5,  5,  5,  5,  5,  0,-10,
  0,  0,  5,  5,  5,  5,  0, -5,
 -5,  0,  5,  5,  5,  5,  0, -5,
-10,  0,  5,  5,  5,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20]

kingstable = [
 20, 30, 10,  0,  0, 10, 30, 20,
 20, 20,  0,  0,  0,  0, 20, 20,
-10,-20,-20,-20,-20,-20,-20,-10,
-20,-30,-30,-40,-40,-30,-30,-20,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30]

class evaluation:
    #this board is the previous board before the move
    def __init__(self, board):
        #print(board)
        self.board = board
    
    def kingSafety(self, kingLoc):
        
        return 0
    '''
    def pieceCover(self, piece, color, square):
        #pawns cover
        if piece == 1:
            print('from pawn')
        #knights cover
        elif piece == 2:
            print('from knight')
        #bishop cover
        elif piece == 3:
            print('from bishop')
        #rook cover
        elif piece == 4:
            print('from rook')
        #queen cover
        elif piece == 5:
            print("queen covers")
    '''

    #calcualtes the opportunity to attack the opponent
    def attackopportunity(self, move):
        move = self.board.pop()
        squareTo = move.to_square #str(move)[:2], str(move)[2:]
        pieceAt = str(self.board.piece_at(squareTo))
        #print(pieceAt)
        #if not pieceAt == None:
            #pieceAt = chess.piece_name(pieceAt)
        
        # print("piecAt",pieceAt)
        score = 0
        #print(squareTo)
        if pieceAt == 'p' or pieceAt == 'P' :
            # print('from pawn')
            score += pieceWeight[1]
        #knights cover
        elif pieceAt == 'k' or pieceAt == 'K' :
            # print('from knight')
            score += pieceWeight[2]
        #bishop cover
        elif pieceAt == 'b' or pieceAt == 'B' :
            # print('from bishop')
            score += pieceWeight[3]
        #rook cover
        elif pieceAt == 'r' or pieceAt == 'R' :
            # print('from rook')
            score += pieceWeight[4]
        #queen cover
        elif pieceAt == 'q' or pieceAt == 'Q' :
            # print("queen covers")
            score += pieceWeight[5]
            
        self.board.push(move)
        return score
            #print('yay?')

    def evaluate(self, move):
        # print(self.board)
        #kingDanger = self.kingSafety(self.board.king(self.color))
        '''
        kingLoc = None
        if self.color:
            kingLoc = self.board.king(chess.WHITE)
        else: 
            kingLoc = self.board.king(chess.BLACK)
        print('color ',self.color, 'king loc',kingLoc)
        #if chess.is_check():
        self.inCheck(chess.square_name(kingLoc))
        #for attackers in kingDanger:
            #print attackers
        '''
        #ideas:
        # be defensive around king
        # be aggressive against enemy pieces of high value (king queen, rook, bishop, etc.)


        ####################################################
        #This code was found at https://medium.datadriveninvestor.com/an-incremental-evaluation-function-and-a-testsuite-for-computer-chess-6fde22aac137
        ######################################
        #print(self.board)
        #self.board.push(move)
        # print("\n checking board of: \n", self.board)
        if self.board.is_checkmate():
            if self.board.turn:
                return -9999
            else:
                return 9999
        if self.board.is_stalemate():
            #print("board stalemate")
            return 0
        if self.board.is_insufficient_material():
            #print("board has insufficient material")
            return 0

        wp = len(self.board.pieces(chess.PAWN, self.board.turn))
        bp = len(self.board.pieces(chess.PAWN, not self.board.turn))
        wn = len(self.board.pieces(chess.KNIGHT, self.board.turn))
        bn = len(self.board.pieces(chess.KNIGHT, not self.board.turn))
        wb = len(self.board.pieces(chess.BISHOP, self.board.turn))
        bb = len(self.board.pieces(chess.BISHOP, not self.board.turn))
        wr = len(self.board.pieces(chess.ROOK, self.board.turn))
        br = len(self.board.pieces(chess.ROOK, not self.board.turn))
        wq = len(self.board.pieces(chess.QUEEN, self.board.turn))
        bq = len(self.board.pieces(chess.QUEEN, not self.board.turn))

        material = (100/2)*(wp-bp)+(320/2)*(wn-bn)+(330/2)*(wb-bb)+(500/2)*(wr-br)+(900/2)*(wq-bq)
        #print('material', material)
        pawnsq = sum([-pawntable[chess.square_mirror(i)] for i in self.board.pieces(chess.PAWN, not self.board.turn)])
        for i in self.board.pieces(chess.PAWN, self.board.turn):
            pawnsq += pawntable[i] - (2 * chess.square_distance(i,self.board.king(self.board.turn)))
            #print(chess.square_distance(i,self.board.king(self.board.turn)))
            #time.pause(1000)
                                 
        # print('pawnsq',pawnsq)
        
        knightsq = sum([-knightstable[chess.square_mirror(i)] for i in self.board.pieces(chess.KNIGHT, not self.board.turn)])
        #sum([knightstable[i] for i in self.board.pieces(chess.KNIGHT, self.board.turn)])
        for i in self.board.pieces(chess.KNIGHT, self.board.turn):
            knightsq += knightstable[i]

        # print('knightsq',knightsq)
        bishopsq= sum([-bishopstable[i] for i in self.board.pieces(chess.BISHOP, not self.board.turn)])
        #bishopsq= bishopsq + sum([-bishopstable[chess.square_mirror(i)] 
        for i in self.board.pieces(chess.BISHOP, self.board.turn):
            bishopsq += bishopstable[i] - (4 * chess.square_distance(i,self.board.king(self.board.turn)))

        # print('bishopsq',bishopsq)
        rooksq = sum([-rookstable[i] for i in self.board.pieces(chess.ROOK, not self.board.turn)])
        #rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)]
        for i in self.board.pieces(chess.ROOK, self.board.turn):
            rooksq += rooksq - (4 * chess.square_distance(i,self.board.king(self.board.turn)))
        # print('rooksq',rooksq)
        queensq = sum([queenstable[i] for i in self.board.pieces(chess.QUEEN, not self.board.turn)])
        #queensq = queensq + sum([-queenstable[chess.square_mirror(i)] 
        for i in self.board.pieces(chess.QUEEN, self.board.turn):
            queensq += queensq - (5 * chess.square_distance(i,self.board.king(self.board.turn)))
        # print('queensq', queensq)
        kingsq = sum([kingstable[i] for i in self.board.pieces(chess.KING, self.board.turn)])
        
        kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)]
                                        for i in self.board.pieces(chess.KING, not self.board.turn)])
        
        #print('kingsq', kingsq)
        eval = material + pawnsq + knightsq + bishopsq+ rooksq+ queensq + kingsq
        #print('evaluation:',eval)
        #if self.board.turn:
        #    return eval
        #else:
        #    return -eval
        attackOpportunity = self.attackopportunity(move)
        # print('attackOpportunity',attackOpportunity)
        eval += attackOpportunity
        # print("total: ",eval)
        #self.board.pop()
        return eval

    def getBestAction(self):
        #print("entering best Action")
        bestA = None
        maxU = -999999999
        #print(self.board.legal_moves)
        
        for i in self.board.legal_moves:
            #print('legal move is',i)
            self.board.push(i)
            e = self.evaluate(i)
            self.board.pop()
            
            if e >maxU:
                #print('maxU changed from', maxU, 'to', e)
                maxU = e
                bestA = i
        #print(maxU)
        return bestA
    
    # def inCheck(self, kingLoc):
    #     # print(kingLoc)
    
    #     attackers = chess.Board.attackers(self.color, chess.square_name(kingLoc))
    #     for a in attackers:
    #         print("attackers attacking king",a)
    #     return 0
    

    # def kingSafety(self, kingLoc):
        
    #     return 0

