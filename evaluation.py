import chess

#################################################
# Table of positions found at: 
# https://github.com/astoeckl/mediumchess/blob/master/Blog1.ipynb
##############################################################
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
    def __init__(self, board, color):
        self.board = board
        self.color = color
    
    def evaluate(self):
        print(self.board)
        
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
        ####################################################
        #This code was found at https://medium.datadriveninvestor.com/an-incremental-evaluation-function-and-a-testsuite-for-computer-chess-6fde22aac137
        ######################################
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

        wp = len(self.board.pieces(chess.PAWN, chess.WHITE))
        bp = len(self.board.pieces(chess.PAWN, chess.BLACK))
        wn = len(self.board.pieces(chess.KNIGHT, chess.WHITE))
        bn = len(self.board.pieces(chess.KNIGHT, chess.BLACK))
        wb = len(self.board.pieces(chess.BISHOP, chess.WHITE))
        bb = len(self.board.pieces(chess.BISHOP, chess.BLACK))
        wr = len(self.board.pieces(chess.ROOK, chess.WHITE))
        br = len(self.board.pieces(chess.ROOK, chess.BLACK))
        wq = len(self.board.pieces(chess.QUEEN, chess.WHITE))
        bq = len(self.board.pieces(chess.QUEEN, chess.BLACK))

        material = 100*(wp-bp)+320*(wn-bn)+330*(wb-bb)+500*(wr-br)+900*(wq-bq)
        #print('material', material)
        pawnsq = sum([pawntable[i] for i in self.board.pieces(chess.PAWN, chess.WHITE)])
        pawnsq= pawnsq + sum([-pawntable[chess.square_mirror(i)] 
                                        for i in self.board.pieces(chess.PAWN, chess.BLACK)])
        #print('pawnsq',pawnsq)
        knightsq = sum([knightstable[i] for i in self.board.pieces(chess.KNIGHT, chess.WHITE)])
        knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)]
                                        for i in self.board.pieces(chess.KNIGHT, chess.BLACK)])
        #print('knightsq',knightsq)
        bishopsq= sum([bishopstable[i] for i in self.board.pieces(chess.BISHOP, chess.WHITE)])
        bishopsq= bishopsq + sum([-bishopstable[chess.square_mirror(i)] 
                                        for i in self.board.pieces(chess.BISHOP, chess.BLACK)])
        #print('bishopsq',bishopsq)
        rooksq = sum([rookstable[i] for i in self.board.pieces(chess.ROOK, chess.WHITE)])
        rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)] 
                                        for i in self.board.pieces(chess.ROOK, chess.BLACK)])
        #print('rooksq',rooksq)
        queensq = sum([queenstable[i] for i in self.board.pieces(chess.QUEEN, chess.WHITE)])
        queensq = queensq + sum([-queenstable[chess.square_mirror(i)] 
                                        for i in self.board.pieces(chess.QUEEN, chess.BLACK)])
        #print('queensq', queensq)
        kingsq = sum([kingstable[i] for i in self.board.pieces(chess.KING, chess.WHITE)])
        kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)]
                                        for i in self.board.pieces(chess.KING, chess.BLACK)])
        #print('kingsq', kingsq)
        eval = material + pawnsq + knightsq + bishopsq+ rooksq+ queensq + kingsq
        #print('evaluation:',eval)
        if self.board.turn:
            return eval
        else:
            return -eval

    def getBestAction(self):
        #print("entering best Action")
        bestA = None
        maxU = -999999999
        for i in self.board.legal_moves:
            #print('legal move is',i)
            self.board.push(i)
            e = self.evaluate()
            self.board.pop()

            if e >maxU:
                print('maxU changed from', maxU, 'to', e)
                maxU = e
                bestA = i

        return bestA
    
    

        
    
    def inCheck(self, kingLoc):
        print(kingLoc)
    
        attackers = chess.Board.attackers(self.color, chess.square_name(kingLoc))
        for a in attackers:
            print("attackers attacking king",a)
        return 0
    

    def kingSafety(self, kingLoc):
        
        return 0

