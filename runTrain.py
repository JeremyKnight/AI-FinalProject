from fitnessFunct import *
from genetic_algo import *
from eval import *



#code from https://github.com/victorsimrbt/chess_mc_ga
eval_model = simple_eval()
tourno_fitness = fitness

ga = genetic_algorithm()
agent,loss = ga.execute(tourno_fitness,eval_model, pop_size =10, generations = 10)
print(agent.fitness)
board = chess.Board()


for move in agent.game:
    board.push_san(move)
print(board)
print(board.is_checkmate())
print(agent.game)