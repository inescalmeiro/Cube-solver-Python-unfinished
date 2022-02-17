from moves import move
from moves import solved
from moves import scramble
from moves import scramble_print


current_c_ori = [0, 0, 0, 0, 0, 0, 0, 0]
current_c_pie = [0, 1, 2, 3, 4, 5, 6, 7]
current_e_ori = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
current_e_pie = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

scramble = 'RU'

cicle = 0
state = 1

while state == 1:
    for character in range(0, len(scramble)):
        turn = scramble[character]
        current_c_pie, current_c_ori, current_e_pie, current_e_ori = \
            move(current_c_pie, current_c_ori, current_e_pie, current_e_ori, turn)
    cicle += 1
    state = solved(current_c_pie, current_c_ori, current_e_pie, current_e_ori)

print(cicle)

print(current_c_ori)
print(current_c_pie)
print(current_e_ori)
print(current_e_pie)

letters, type = scramble()

scramble_print(letters, type)

for turns in range(0,len(letters)):
    turn = letters[turns]
    for times in range(0,type[turns]):
        current_c_pie, current_c_ori, current_e_pie, current_e_ori = \
            move(current_c_pie, current_c_ori, current_e_pie, current_e_ori, turn)

"""
scheme1 = '       Y Y Y'
scheme2 = '       Y Y Y'
scheme3 = '       Y Y Y'
scheme4 = 'O O O  B B B  R R R  G G G'
scheme5 = 'O O O  B B B  R R R  G G G'
scheme6 = 'O O O  B B B  R R R  G G G'
scheme7 = '       W W W'
scheme8 = '       W W W'
scheme9 = '       W W W'

"""

correct_piece = 0
pieces = [0, 1, 2, 3]

for piece in pieces:
    if edge_pie.index(piece) == piece:
        correct_piece += 1

if correct_piece == 2:
    let_incr += 'RURURUR'
    tim_incr += [1, 1, 3, 1, 1, 2, 3]
else:



let_incr += 'U'
tim_incr += [1]

cor_pie, cor_ori, edge_pie, edge_ori = execute_move(cor_pie, cor_ori, edge_pie, edge_ori, let_incr,
                                                    tim_incr)

for piece in pieces:
    if edge_pie.index(piece) == piece:
        correct_piece += 1

from scramble import scramble
from scramble import scramble_print
from scramble import state
from solver import pseudo_cross
from solver import execute_move
from solver import w_cross
from solver import d2u_all
from solver import u2d_cor
from solver import u2lateral_all
from solver import lateral2u_edge
from solver import y_cross
from solver import y_cross_edges
from solver import corner_in_place
from solver import corner_orient

cor_ori = [0, 0, 0, 0, 0, 0, 0, 0]
cor_pie = [0, 1, 2, 3, 4, 5, 6, 7]
edge_ori = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
edge_pie = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

letters, times = scramble()
"""
letters = 'FRLFBFRFBDRUFLBLBDRB'
times = [3, 1, 1, 2, 1, 1, 3, 1, 2, 3, 1, 2, 1, 3, 1, 1, 3, 2, 3, 3]
"""

scramble_print(letters, times)

cor_pie, cor_ori, edge_pie, edge_ori = \
                execute_move(cor_pie, cor_ori, edge_pie, edge_ori, letters, times)

letters = ''
times = []

for cicle in range(0, 4):
    cor_pie, cor_ori, edge_pie, edge_ori, temp_times, temp_letter = pseudo_cross(cor_pie, cor_ori, edge_pie, edge_ori)
    letters += temp_letter
    if not temp_times == []:
        for index in range(0, len(temp_times)):
            times += [temp_times[index]]

cor_pie, cor_ori, edge_pie, edge_ori,  tim_incr, let_incr = w_cross(cor_pie, cor_ori, edge_pie, edge_ori)

letters += let_incr
times += tim_incr

for cicle in range(0, 2):
    cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr = u2d_cor(cor_pie, cor_ori, edge_pie, edge_ori)
    letters += let_incr
    times += tim_incr

cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr = d2u_all(cor_pie, cor_ori, edge_pie, edge_ori)

letters += let_incr
times += tim_incr

for cicle in range(0, 2):
    cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr = u2d_cor(cor_pie, cor_ori, edge_pie, edge_ori)
    letters += let_incr
    times += tim_incr

for cicle in range(0, 4):
    cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr = u2lateral_all(cor_pie, cor_ori, edge_pie, edge_ori)
    letters += let_incr
    times += tim_incr

cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr = lateral2u_edge(cor_pie, cor_ori, edge_pie, edge_ori)

letters += let_incr
times += tim_incr

cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr = y_cross(cor_pie, cor_ori, edge_pie, edge_ori)

letters += let_incr
times += tim_incr

cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr = y_cross_edges(cor_pie, cor_ori, edge_pie, edge_ori)

letters += let_incr
times += tim_incr

cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr = corner_in_place(cor_pie, cor_ori, edge_pie, edge_ori)

letters += let_incr
times += tim_incr

cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr = corner_orient(cor_pie, cor_ori, edge_pie, edge_ori)

letters += let_incr
times += tim_incr

scramble_print(letters, times)

state(cor_pie, cor_ori, edge_pie, edge_ori)