from moves import move
from scramble import scramble_print


def u2d(spot, piece):

    corres = [2, 1, 0, 3]
    temp_let_incr = ''
    temp_tim_incr = []
    if not corres[piece - 4] == spot and spot < 4:
        move_times = [1, 2, 3]
        target_6 = [3, 2, 1]
        target_5 = [0, 3, 2]
        target_4 = [1, 0, 3]
        target_7 = [2, 1, 0]
        targets = [target_4, target_5, target_6, target_7]
        target = targets[piece - 4]
        index = target.index(spot)
        temp_tim_incr = [move_times[index]]
        temp_let_incr = 'U'

    lateral_moves = ['F', 'R', 'B', 'L']
    temp_let_incr += lateral_moves[piece - 4]
    temp_tim_incr += [2]

    return temp_tim_incr, temp_let_incr


def lateral2u(spot):
    lateral_moves = ['R', 'L', 'R', 'L']
    lateral_times_1 = [1, 3, 3, 1]
    lateral_times_2 = [3, 1, 1, 3]
    temp_let_incr = ''
    temp_tim_incr = []

    temp_let_incr += lateral_moves[spot - 8]
    temp_tim_incr += [lateral_times_1[spot - 8]]
    temp_let_incr += 'U'
    temp_tim_incr += [1]
    temp_let_incr += lateral_moves[spot - 8]
    temp_tim_incr += [lateral_times_2[spot - 8]]

    return temp_tim_incr, temp_let_incr


def execute_move(cor_pie, cor_ori, edge_pie, edge_ori, letters, times):
    for turn in range(0, len(letters)):
        letter = letters[turn]
        for time in range(0, times[turn]):
            cor_pie, cor_ori, edge_pie, edge_ori = move(cor_pie, cor_ori, edge_pie, edge_ori, letter)

    return cor_pie, cor_ori, edge_pie, edge_ori


def pseudo_cross(cor_pie, cor_ori, edge_pie, edge_ori):
    pieces = [4, 5, 6, 7]
    let_incr = ''
    tim_incr = []
    lateral_moves = ['F', 'R', 'B', 'L']

    u_pieces = []
    lateral_pieces = []

    for piece in pieces:

        spot = edge_pie.index(piece)

        if spot == 0 or spot == 1 or spot == 2 or spot == 3:
            u_pieces += [piece]
        elif spot == 8 or spot == 9 or spot == 10 or spot == 11:
            lateral_pieces += [piece]

    for piece in u_pieces:
        spot = edge_pie.index(piece)

        temp_tim_incr, temp_let_incr = u2d(spot, piece)

        cor_pie, cor_ori, edge_pie, edge_ori = \
            execute_move(cor_pie, cor_ori, edge_pie, edge_ori, temp_let_incr, temp_tim_incr)

        tim_incr += temp_tim_incr
        let_incr += temp_let_incr

    for piece in lateral_pieces:
        spot = edge_pie.index(piece)

        temp_tim_incr, temp_let_incr = lateral2u(spot)

        tim_incr += temp_tim_incr
        let_incr += temp_let_incr

        cor_pie, cor_ori, edge_pie, edge_ori = \
            execute_move(cor_pie, cor_ori, edge_pie, edge_ori, temp_let_incr, temp_tim_incr)

        spot = edge_pie.index(piece)

        temp_tim_incr, temp_let_incr = u2d(spot, piece)

        cor_pie, cor_ori, edge_pie, edge_ori = \
            execute_move(cor_pie, cor_ori, edge_pie, edge_ori, temp_let_incr, temp_tim_incr)

        tim_incr += temp_tim_incr
        let_incr += temp_let_incr

    d_pieces = []

    for piece in pieces:

        spot = edge_pie.index(piece)
        if spot == 4 or spot == 5 or spot == 6 or spot == 7:
            if not spot == piece:
                d_pieces += [piece]

    for piece in d_pieces:
        spot = edge_pie.index(piece)

        temp_let_incr = lateral_moves[spot - 4]
        temp_tim_incr = [2]

        tim_incr += temp_tim_incr
        let_incr += temp_let_incr

        cor_pie, cor_ori, edge_pie, edge_ori = \
            execute_move(cor_pie, cor_ori, edge_pie, edge_ori, temp_let_incr, temp_tim_incr)

        spot = edge_pie.index(piece)

        temp_tim_incr, temp_let_incr = u2d(spot, piece)

        cor_pie, cor_ori, edge_pie, edge_ori = \
            execute_move(cor_pie, cor_ori, edge_pie, edge_ori, temp_let_incr, temp_tim_incr)

        tim_incr += temp_tim_incr
        let_incr += temp_let_incr

    for piece in pieces:
        if piece == edge_pie.index:
            pieces.remove(piece)

    return cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr


def w_cross(cor_pie, cor_ori, edge_pie, edge_ori):

    pieces = [4, 5, 6, 7]
    lateral_moves_1 = ['F', 'R', 'B', 'L']
    lateral_moves_2 = ['R', 'B', 'L', 'F']
    let_incr = ''
    tim_incr = []
    temp_let_incr = ''
    temp_tim_incr = []

    for piece in pieces:
        if edge_ori[piece] == 1:
            temp_let_incr += lateral_moves_1[piece - 4]
            temp_tim_incr += [3]
            temp_let_incr += 'D'
            temp_tim_incr += [1]
            temp_let_incr += lateral_moves_2[piece - 4]
            temp_tim_incr += [3]
            temp_let_incr += 'D'
            temp_tim_incr += [3]

        cor_pie, cor_ori, edge_pie, edge_ori = execute_move(cor_pie, cor_ori, edge_pie, edge_ori, temp_let_incr,
                                                            temp_tim_incr)

        tim_incr += temp_tim_incr
        let_incr += temp_let_incr

        temp_let_incr = ''
        temp_tim_incr = []

    return cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr


def u2d_cor_1(spot, piece):
    temp_let_incr = ''
    temp_tim_incr = []
    corres = [1, 0, 3, 2]
    if not corres[piece - 4] == spot and spot < 4:
        move_times = [1, 2, 3]
        target_6 = [2, 1, 0]
        target_5 = [3, 2, 1]
        target_4 = [0, 3, 2]
        target_7 = [1, 0, 3]
        targets = [target_4, target_5, target_6, target_7]
        target = targets[piece - 4]
        index = target.index(spot)
        temp_tim_incr += [move_times[index]]
        temp_let_incr += 'U'

    lateral_moves = ['R', 'B', 'L', 'F']
    temp_let_incr += lateral_moves[piece - 4]
    temp_tim_incr += [1]

    temp_let_incr += 'U'
    temp_tim_incr += [1]

    temp_let_incr += lateral_moves[piece - 4]
    temp_tim_incr += [3]

    return temp_tim_incr, temp_let_incr


def u2d_cor_2(spot, piece):
    temp_let_incr = ''
    temp_tim_incr = []
    corres = [2, 1, 0, 3]
    if not corres[piece - 4] == spot and spot < 4:
        move_times = [1, 2, 3]
        target_6 = [3, 2, 1]
        target_5 = [0, 3, 2]
        target_4 = [1, 0, 3]
        target_7 = [2, 1, 0]
        targets = [target_4, target_5, target_6, target_7]
        target = targets[piece - 4]
        index = target.index(spot)
        temp_tim_incr += [move_times[index]]
        temp_let_incr += 'U'

    lateral_moves = ['R', 'B', 'L', 'F']
    temp_let_incr += lateral_moves[piece - 4]
    temp_tim_incr += [1]

    temp_let_incr += 'U'
    temp_tim_incr += [3]

    temp_let_incr += lateral_moves[piece - 4]
    temp_tim_incr += [3]

    return temp_tim_incr, temp_let_incr


def u2d_cor_0(spot, piece):

    temp_let_incr = ''
    temp_tim_incr = []
    corres = [1, 0, 3, 2]

    if not corres[piece - 4] == spot and spot < 4:
        move_times = [1, 2, 3]
        target_6 = [2, 1, 0]
        target_5 = [3, 2, 1]
        target_4 = [0, 3, 2]
        target_7 = [1, 0, 3]
        targets = [target_4, target_5, target_6, target_7]
        target = targets[piece - 4]
        index = target.index(spot)
        temp_tim_incr += [move_times[index]]
        temp_let_incr += 'U'

    lateral_moves = ['R', 'B', 'L', 'F']
    temp_let_incr += lateral_moves[piece - 4]
    temp_tim_incr += [1]

    temp_let_incr += 'U'
    temp_tim_incr += [2]

    temp_let_incr += lateral_moves[piece - 4]
    temp_tim_incr += [3]

    temp_let_incr += 'U'
    temp_tim_incr += [3]

    temp_let_incr += lateral_moves[piece - 4]
    temp_tim_incr += [1]

    temp_let_incr += 'U'
    temp_tim_incr += [1]

    temp_let_incr += lateral_moves[piece - 4]
    temp_tim_incr += [3]

    return temp_tim_incr, temp_let_incr


def d2u(spot):
    temp_let_incr = ''
    temp_tim_incr = []
    lateral_moves = ['R', 'B', 'L', 'F']
    temp_let_incr += lateral_moves[spot - 4]
    temp_tim_incr += [1]

    temp_let_incr += 'U'
    temp_tim_incr += [1]

    temp_let_incr += lateral_moves[spot - 4]
    temp_tim_incr += [3]

    return temp_tim_incr, temp_let_incr


def u2d_cor(cor_pie, cor_ori, edge_pie, edge_ori):
    pieces = [4, 5, 6, 7]

    tim_incr = []
    let_incr = ''

    for piece in pieces:
        spot = cor_pie.index(piece)

        if spot == 0 or spot == 1 or spot == 2 or spot == 3:

            if cor_ori[spot] == 1:

                temp_tim_incr, temp_let_incr = u2d_cor_1(spot, piece)

                cor_pie, cor_ori, edge_pie, edge_ori = execute_move(cor_pie, cor_ori, edge_pie, edge_ori,
                                                                    temp_let_incr,
                                                                    temp_tim_incr)
                tim_incr += temp_tim_incr
                let_incr += temp_let_incr

            elif cor_ori[spot] == 2:

                temp_tim_incr, temp_let_incr = u2d_cor_2(spot, piece)

                cor_pie, cor_ori, edge_pie, edge_ori = execute_move(cor_pie, cor_ori, edge_pie, edge_ori,
                                                                    temp_let_incr,
                                                                    temp_tim_incr)

                tim_incr += temp_tim_incr
                let_incr += temp_let_incr

            elif cor_ori[spot] == 0:

                temp_tim_incr, temp_let_incr = u2d_cor_0(spot, piece)

                cor_pie, cor_ori, edge_pie, edge_ori = execute_move(cor_pie, cor_ori, edge_pie, edge_ori,
                                                                    temp_let_incr,
                                                                    temp_tim_incr)

                tim_incr += temp_tim_incr
                let_incr += temp_let_incr

    return cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr


def d2u_all(cor_pie, cor_ori, edge_pie, edge_ori):
    pieces = [4, 5, 6, 7]

    let_incr = ''
    tim_incr = []

    for piece in pieces:
        spot = cor_pie.index(piece)
        if spot == 4 or spot == 5 or spot == 6 or spot == 7:
            if not piece == spot:

                temp_tim_incr, temp_let_incr = d2u(spot)

                cor_pie, cor_ori, edge_pie, edge_ori = execute_move(cor_pie, cor_ori, edge_pie, edge_ori, temp_let_incr,
                                                                    temp_tim_incr)

                tim_incr += temp_tim_incr
                let_incr += temp_let_incr

            elif piece == spot and not cor_ori[spot] == 0:

                temp_tim_incr, temp_let_incr = d2u(spot)

                cor_pie, cor_ori, edge_pie, edge_ori = execute_move(cor_pie, cor_ori, edge_pie, edge_ori, temp_let_incr,
                                                                    temp_tim_incr)

                tim_incr += temp_tim_incr
                let_incr += temp_let_incr

    return cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr


def u2lateral_adjust(spot, corres_piece):
    temp_let_incr = ''
    temp_tim_incr = []

    if not corres_piece == spot and spot < 4:
        move_times = [1, 2, 3]
        target_0 = [3, 2, 1]
        target_1 = [0, 3, 2]
        target_2 = [1, 0, 3]
        target_3 = [2, 1, 0]
        targets = [target_0, target_1, target_2, target_3]
        target = targets[corres_piece]
        index = target.index(spot)
        temp_tim_incr += [move_times[index]]
        temp_let_incr += 'U'

    return temp_tim_incr, temp_let_incr


def u2lateral(perm_edge, piece):
    temp_let_incr = ''
    temp_tim_incr = []

    if perm_edge == 0:
        lateral_moves_1 = ['R', 'F', 'B', 'L']
        lateral_moves_2 = ['F', 'L', 'R', 'B']

        temp_let_incr += lateral_moves_1[piece - 8]
        temp_tim_incr += [1]

        temp_let_incr += 'U'
        temp_tim_incr += [3]

        temp_let_incr += lateral_moves_1[piece - 8]
        temp_tim_incr += [3]

        temp_let_incr += 'U'
        temp_tim_incr += [3]

        temp_let_incr += lateral_moves_2[piece - 8]
        temp_tim_incr += [3]

        temp_let_incr += 'U'
        temp_tim_incr += [1]

        temp_let_incr += lateral_moves_2[piece - 8]
        temp_tim_incr += [1]

    elif perm_edge == 1:
        lateral_moves_1 = ['F', 'L', 'R', 'B']
        lateral_moves_2 = ['R', 'F', 'B', 'L']

        temp_let_incr += lateral_moves_1[piece - 8]
        temp_tim_incr += [3]

        temp_let_incr += 'U'
        temp_tim_incr += [1]

        temp_let_incr += lateral_moves_1[piece - 8]
        temp_tim_incr += [1]

        temp_let_incr += 'U'
        temp_tim_incr += [1]

        temp_let_incr += lateral_moves_2[piece - 8]
        temp_tim_incr += [1]

        temp_let_incr += 'U'
        temp_tim_incr += [3]

        temp_let_incr += lateral_moves_2[piece - 8]
        temp_tim_incr += [3]

    return temp_tim_incr, temp_let_incr


def u2lateral_all(cor_pie, cor_ori, edge_pie, edge_ori):

    pieces = [8, 9, 10, 11]
    let_incr = ''
    tim_incr = []

    for piece in pieces:
        spot = edge_pie.index(piece)
        if spot == 0 or spot == 1 or spot == 2 or spot == 3:
            if edge_ori[spot] == 1:
                corres = [3, 1, 3, 1]
                corres_piece = corres[piece - 8]
                perm_edge_type = [0, 1, 1, 0]
                perm_edge = perm_edge_type[piece - 8]
            else:
                corres = [0, 0, 2, 2]
                corres_piece = corres[piece - 8]
                perm_edge_type = [1, 0, 0, 1]
                perm_edge = perm_edge_type[piece - 8]

            temp_tim_incr, temp_let_incr = u2lateral_adjust(spot, corres_piece)

            cor_pie, cor_ori, edge_pie, edge_ori = execute_move(cor_pie, cor_ori, edge_pie, edge_ori, temp_let_incr,
                                                                temp_tim_incr)

            tim_incr += temp_tim_incr
            let_incr += temp_let_incr

            temp_tim_incr, temp_let_incr = u2lateral(perm_edge, piece)

            cor_pie, cor_ori, edge_pie, edge_ori = execute_move(cor_pie, cor_ori, edge_pie, edge_ori, temp_let_incr,
                                                                temp_tim_incr)

            tim_incr += temp_tim_incr
            let_incr += temp_let_incr

    return cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr


def lateral2u_edge(cor_pie, cor_ori, edge_pie, edge_ori):

    pieces = [8, 9, 10, 11]
    let_incr = ''
    tim_incr = []

    for piece in pieces:

        temp_let_incr = ''
        temp_tim_incr = []

        spot = edge_pie.index(piece)
        if spot == 8 or spot == 9 or spot == 10 or spot == 11:
            if not spot == piece:
                temp_tim_incr, temp_let_incr = u2lateral(0, piece)
            elif spot == piece and edge_ori[piece] == 1:
                temp_tim_incr, temp_let_incr = u2lateral(0, piece)

        cor_pie, cor_ori, edge_pie, edge_ori = execute_move(cor_pie, cor_ori, edge_pie, edge_ori, temp_let_incr,
                                                            temp_tim_incr)

        tim_incr += temp_tim_incr
        let_incr += temp_let_incr

        cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr = u2lateral_all(cor_pie, cor_ori, edge_pie, edge_ori)

    return cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr


def y_cross(cor_pie, cor_ori, edge_pie, edge_ori):

    let_incr = ''
    tim_incr = []
    if edge_ori[0] == 1 or edge_ori[1] == 1 or edge_ori[2] == 1 or edge_ori[3] == 1:
        if edge_ori[0] == 0 and edge_ori[2] == 0:

            let_incr += 'U'
            tim_incr += [1]

            let_incr += 'FRURUF'
            tim_incr += [1, 1, 1, 3, 3, 3]

        elif edge_ori[1] == 0 and edge_ori[3] == 0:

            let_incr += 'FRURUF'
            tim_incr += [1, 1, 1, 3, 3, 3]
        elif edge_ori[0] == 0 and edge_ori[3] == 0:

            let_incr += 'FRURURURUF'
            tim_incr += [1, 1, 1, 3, 3, 1, 1, 3, 3, 3]

        elif edge_ori[2] == 0 and edge_ori[3] == 0:

            let_incr += 'U'
            tim_incr += [1]

            let_incr += 'FRURURURUF'
            tim_incr += [1, 1, 1, 3, 3, 1, 1, 3, 3, 3]

        elif edge_ori[2] == 0 and edge_ori[1] == 0:

            let_incr += 'U'
            tim_incr += [2]

            let_incr += 'FRURURURUF'
            tim_incr += [1, 1, 1, 3, 3, 1, 1, 3, 3, 3]

        elif edge_ori[0] == 0 and edge_ori[1] == 0:

            let_incr += 'U'
            tim_incr += [3]

            let_incr += 'FRURURURUF'
            tim_incr += [1, 1, 1, 3, 3, 1, 1, 3, 3, 3]
        else:
            let_incr += 'FRURURURUF'
            tim_incr += [1, 1, 1, 3, 3, 1, 1, 3, 3, 3]

            let_incr += 'U'
            tim_incr += [1]

            let_incr += 'FRURUF'
            tim_incr += [1, 1, 1, 3, 3, 3]

    cor_pie, cor_ori, edge_pie, edge_ori = execute_move(cor_pie, cor_ori, edge_pie, edge_ori, let_incr,
                                                        tim_incr)

    return cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr


def y_cross_edges(cor_pie, cor_ori, edge_pie, edge_ori):
    pieces = [0, 1, 2, 3]

    for times in range(0, 4):
        temp_let_incr = ''
        temp_tim_incr = []
        correct_pieces = []
        for piece in pieces:
            if edge_pie.index(piece) == piece:
                correct_pieces += [piece]

        if len(correct_pieces) == 1:
            pieces2swap = [0, 1, 2, 3]
            pieces2swap.remove(correct_pieces[0])
            lateral_moves = ''
            move = []

            if edge_pie[pieces2swap[0]] == pieces2swap[1]:
                lateral_moves = ['R', 'F', 'L', 'B']
                move = [3, 1]

            elif edge_pie[pieces2swap[1]] == pieces2swap[0]:
                lateral_moves = ['L', 'B', 'R', 'F']
                move = [1, 3]

            temp_let_incr += lateral_moves[correct_pieces[0]]
            temp_tim_incr += [move[0]]

            temp_let_incr += 'U'
            temp_tim_incr += [move[0]]

            temp_let_incr += lateral_moves[correct_pieces[0]]
            temp_tim_incr += [move[1]]

            temp_let_incr += 'U'
            temp_tim_incr += [move[0]]

            temp_let_incr += lateral_moves[correct_pieces[0]]
            temp_tim_incr += [move[0]]

            temp_let_incr += 'U'
            temp_tim_incr += [2]

            temp_let_incr += lateral_moves[correct_pieces[0]]
            temp_tim_incr += [move[1]]

        elif len(correct_pieces) == 2:
            if correct_pieces[0] == 0 and correct_pieces[1] == 2:
                temp_let_incr += 'RURURUR'
                temp_tim_incr += [1, 1, 3, 1, 1, 2, 3]
            elif correct_pieces[0] == 1 and correct_pieces[1] == 3:
                temp_let_incr += 'RURURUR'
                temp_tim_incr += [1, 1, 3, 1, 1, 2, 3]
            else:
                temp_let_incr += 'U'
                temp_tim_incr += [1]

        elif len(correct_pieces) == 4:
            break
        else:
            temp_let_incr += 'U'
            temp_tim_incr += [1]

        cor_pie, cor_ori, edge_pie, edge_ori = \
            execute_move(cor_pie, cor_ori, edge_pie, edge_ori, temp_let_incr, temp_tim_incr)

    return cor_pie, cor_ori, edge_pie, edge_ori, temp_tim_incr, temp_let_incr


def corner_in_place(cor_pie, cor_ori, edge_pie, edge_ori):

    spots = [0, 1, 2, 3]
    correct = 0

    temp_let_incr = ''
    temp_tim_incr = []
    let_incr = ''
    tim_incr = []

    for spot in spots:
        if spot == cor_pie[spot]:
            correct += 1

    if correct == 0:
        piece = 1
        spot = cor_pie.index(piece)
        if spot == 2:
            temp_let_incr += 'LURULURU'
            temp_tim_incr += [1, 3, 3, 1, 3, 3, 1, 1]
        elif spot == 3:
            temp_let_incr += 'RULURULU'
            temp_tim_incr += [1, 3, 3, 1, 3, 3, 1, 1]
        elif spot == 0:
            temp_let_incr += 'RULURULU'
            temp_tim_incr += [3, 1, 1, 3, 1, 1, 3, 3]

    cor_pie, cor_ori, edge_pie, edge_ori = execute_move(cor_pie, cor_ori, edge_pie, edge_ori, temp_let_incr, temp_tim_incr)

    tim_incr += temp_tim_incr
    let_incr += temp_let_incr
    temp_let_incr = ''
    temp_tim_incr = []

    correct_pieces = []

    for spot in spots:
        if spot == cor_pie[spot]:
            correct_pieces += [spot]

    if len(correct_pieces) == 1:
        correct_piece = correct_pieces[0]
        if correct_piece == 0:
            if cor_pie[2] == 1:
                temp_let_incr = 'LURULURU'
                temp_tim_incr = [1, 3, 3, 1, 3, 3, 1, 1]
            if cor_pie[2] == 3:
                temp_let_incr = 'FUBUFUBU'
                temp_tim_incr = [3, 1, 1, 3, 1, 1, 3, 3]
        if correct_piece == 1:
            if cor_pie[3] == 2:
                temp_let_incr = 'BUFUBUFU'
                temp_tim_incr = [1, 3, 3, 1, 3, 3, 1, 1]
            if cor_pie[3] == 0:
                temp_let_incr = 'LURULURU'
                temp_tim_incr = [3, 1, 1, 3, 1, 1, 3, 3]
        if correct_piece == 2:
            if cor_pie[0] == 3:
                temp_let_incr = 'RULURULU'
                temp_tim_incr = [1, 3, 3, 1, 3, 3, 1, 1]
            if cor_pie[0] == 1:
                temp_let_incr = 'BUFUBUFU'
                temp_tim_incr = [3, 1, 1, 3, 1, 1, 3, 3]
        if correct_piece == 3:
            if cor_pie[1] == 0:
                temp_let_incr = 'FUBUFUBU'
                temp_tim_incr = [1, 3, 3, 1, 3, 3, 1, 1]
            if cor_pie[2] == 2:
                temp_let_incr = 'RULURULU'
                temp_tim_incr = [3, 1, 1, 3, 1, 1, 3, 3]

    cor_pie, cor_ori, edge_pie, edge_ori = execute_move(cor_pie, cor_ori, edge_pie, edge_ori, temp_let_incr, temp_tim_incr)

    tim_incr += temp_tim_incr
    let_incr += temp_let_incr
    return cor_pie, cor_ori, edge_pie, edge_ori, temp_tim_incr, temp_let_incr


def corner_orient(cor_pie, cor_ori, edge_pie, edge_ori):
    let_incr = ''
    tim_incr = []

    for times in range(0, 4):
        for time in range(0, 2):
            if cor_pie[1] < 4 and not cor_ori[1] == 0:
                temp_let_incr = 'RDRDRDRD'
                temp_tim_incr = [3, 3, 1, 1, 3, 3, 1, 1]

                cor_pie, cor_ori, edge_pie, edge_ori = execute_move(cor_pie, cor_ori, edge_pie, edge_ori, temp_let_incr,
                                                                    temp_tim_incr)

                tim_incr += temp_tim_incr
                let_incr += temp_let_incr

        temp_let_incr = 'U'
        temp_tim_incr = [1]

        cor_pie, cor_ori, edge_pie, edge_ori = execute_move(cor_pie, cor_ori, edge_pie, edge_ori, temp_let_incr,
                                                            temp_tim_incr)

        tim_incr += temp_tim_incr
        let_incr += temp_let_incr

    return cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr


def solve(cor_pie, cor_ori, edge_pie, edge_ori):
    letters = ''
    times = []

    for cicle in range(0, 4):
        cor_pie, cor_ori, edge_pie, edge_ori, temp_times, temp_letter = pseudo_cross(cor_pie, cor_ori, edge_pie,
                                                                                     edge_ori)
        letters += temp_letter
        if not temp_times == []:
            for index in range(0, len(temp_times)):
                times += [temp_times[index]]

    cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr = w_cross(cor_pie, cor_ori, edge_pie, edge_ori)

    letters += let_incr
    times += tim_incr

    for cicle in range(0, 2):
        cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr = u2d_cor(cor_pie, cor_ori, edge_pie, edge_ori)
        letters += let_incr
        times += tim_incr

        cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr = d2u_all(cor_pie, cor_ori, edge_pie, edge_ori)

        letters += let_incr
        times += tim_incr

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

    cor_pie, cor_ori, edge_pie, edge_ori, tim_incr, let_incr = u2lateral_all(cor_pie, cor_ori, edge_pie, edge_ori)
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

    return letters, times
