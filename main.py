from scramble import scramble
from scramble import state
from solver import execute_move
from solver import solve


cor_ori = [0, 0, 0, 0, 0, 0, 0, 0]
cor_pie = [0, 1, 2, 3, 4, 5, 6, 7]
edge_ori = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
edge_pie = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

letter, times = scramble()

cor_pie, cor_ori, edge_pie, edge_ori = execute_move(cor_pie, cor_ori, edge_pie, edge_ori, letter, times)

state(cor_pie, cor_ori, edge_pie, edge_ori)

letter, times = solve(cor_pie, cor_ori, edge_pie, edge_ori)

cor_pie, cor_ori, edge_pie, edge_ori = execute_move(cor_pie, cor_ori, edge_pie, edge_ori, letter, times)

state(cor_pie, cor_ori, edge_pie, edge_ori)

