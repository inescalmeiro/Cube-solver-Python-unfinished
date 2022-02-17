import random


def solved(cor_pie, cor_ori, edge_pie, edge_ori):
    control = 0
    for number in range(0,8):
        if not number == cor_pie[number]:
            control = 1
            break
        if not cor_ori[number] == 0:
            control = 1
            break
    for number in range(0,12):
        if not number == edge_pie[number]:
            control = 1
            break
        if not edge_ori[number] == 0:
            control = 1
            break
    return control


def scramble():
    letters = ''
    type = []
    options = 'RLUDFB'
    rand = -1
    for turns in range(0, 20):
        rand_previous = rand
        while rand_previous == rand:
            rand = random.randint(0, 5)

        letter = options[rand]
        letters += letter
        randtype = random.randint(1, 3)
        type += [randtype]
    return letters, type


def scramble_print(letters, times):

    scrambleprint = ''

    if not len(times) == 0:
        for letter in range(0, len(letters)):
            scrambleprint += letters[letter]
            typespot = times[letter]
            if typespot == 2:
                scrambleprint += '2'
            elif typespot == 3:
                scrambleprint += "'"

            scrambleprint += ' '

    print(scrambleprint)


def state(cor_pie, cor_ori, edge_pie, edge_ori):

    centers = [4, 13, 22, 31, 40, 49]

    colors = ['Y', 'O', 'B', 'R', 'G', 'W']

    scheme = [' '] * 54

    for index in range(0, 6):
        color = colors[index]
        center = centers[index]
        scheme[center] = color

    ori_1_Y = ['G', 'R', 'B', 'O']
    ori_2_Y = ['R', 'B', 'O', 'G']
    ori_1_W = ['B', 'R', 'G', 'O']
    ori_2_W = ['R', 'G', 'O', 'B']
    cor0 = [2, 36, 29]
    cor1 = [8, 27, 20]
    cor2 = [6, 18, 11]
    cor3 = [0, 9, 38]
    cor4 = [47, 26, 33]
    cor5 = [53, 35, 42]
    cor6 = [51, 44, 15]
    cor7 = [45, 17, 24]

    corners = [cor0, cor1, cor2, cor3, cor4, cor5, cor6, cor7]

    for spot in range(0, 8):
        corner = corners[spot]
        piece = cor_pie[spot]
        ori = cor_ori[spot]
        if piece < 4:
            sticker1 = 'Y'
            sticker2 = ori_1_Y[piece]
            sticker3 = ori_2_Y[piece]
            if ori == 0:
                scheme[corner[0]] = sticker1
                scheme[corner[1]] = sticker2
                scheme[corner[2]] = sticker3
            elif ori == 1:
                scheme[corner[0]] = sticker3
                scheme[corner[1]] = sticker1
                scheme[corner[2]] = sticker2
            elif ori == 2:
                scheme[corner[0]] = sticker2
                scheme[corner[1]] = sticker3
                scheme[corner[2]] = sticker1
        else:
            sticker1 = 'W'
            sticker2 = ori_1_W[piece - 4]
            sticker3 = ori_2_W[piece - 4]
            if ori == 0:
                scheme[corner[0]] = sticker1
                scheme[corner[1]] = sticker2
                scheme[corner[2]] = sticker3
            elif ori == 1:
                scheme[corner[0]] = sticker3
                scheme[corner[1]] = sticker1
                scheme[corner[2]] = sticker2
            elif ori == 2:
                scheme[corner[0]] = sticker2
                scheme[corner[1]] = sticker3
                scheme[corner[2]] = sticker1

    ori_1 = ['G', 'R', 'B', 'O']
    ori_2 = ['B', 'R', 'G', 'O']
    ori_3 = ['R', 'O']

    edge_0 = [1, 37]
    edge_1 = [5, 28]
    edge_2 = [7, 19]
    edge_3 = [3, 10]
    edge_4 = [46, 25]
    edge_5 = [50, 34]
    edge_6 = [52, 43]
    edge_7 = [48, 16]
    edge_8 = [23, 30]
    edge_9 = [21, 14]
    edge_10 = [39, 32]
    edge_11 = [41, 12]

    edges = [edge_0, edge_1, edge_2, edge_3, edge_4, edge_5, edge_6, edge_7, edge_8, edge_9, edge_10, edge_11]

    for spot in range(0, 12):
        edge = edges[spot]
        piece = edge_pie[spot]
        ori = edge_ori[spot]
        if piece < 4:
            sticker1 = 'Y'
            sticker2 = ori_1[piece]
            if ori == 0:
                scheme[edge[0]] = sticker1
                scheme[edge[1]] = sticker2
            elif ori == 1:
                scheme[edge[0]] = sticker2
                scheme[edge[1]] = sticker1
        elif piece > 3 and piece < 8:
            sticker1 = 'W'
            sticker2 = ori_2[piece - 4]
            if ori == 0:
                scheme[edge[0]] = sticker1
                scheme[edge[1]] = sticker2
            elif ori == 1:
                scheme[edge[0]] = sticker2
                scheme[edge[1]] = sticker1
        elif piece > 7 and piece < 10:
            sticker1 = 'B'
            sticker2 = ori_3[piece - 8]
            if ori == 0:
                scheme[edge[0]] = sticker1
                scheme[edge[1]] = sticker2
            elif ori == 1:
                scheme[edge[0]] = sticker2
                scheme[edge[1]] = sticker1
        elif piece > 9:
            sticker1 = 'G'
            sticker2 = ori_3[piece - 10]
            if ori == 0:
                scheme[edge[0]] = sticker1
                scheme[edge[1]] = sticker2
            elif ori == 1:
                scheme[edge[0]] = sticker2
                scheme[edge[1]] = sticker1

    scheme1 = f'       {scheme[0]} {scheme[1]} {scheme[2]}'
    scheme2 = f'       {scheme[3]} {scheme[4]} {scheme[5]}'
    scheme3 = f'       {scheme[6]} {scheme[7]} {scheme[8]}'
    scheme4 = f'{scheme[9]} {scheme[10]} {scheme[11]}  {scheme[18]} {scheme[19]} {scheme[20]}  {scheme[27]} {scheme[28]} ' \
              f'{scheme[29]}  {scheme[36]} {scheme[37]} {scheme[38]}'
    scheme5 = f'{scheme[12]} {scheme[13]} {scheme[14]}  {scheme[21]} {scheme[22]} {scheme[23]}  {scheme[30]} {scheme[31]} ' \
              f'{scheme[32]}  {scheme[39]} {scheme[40]} {scheme[41]}'
    scheme6 = f'{scheme[15]} {scheme[16]} {scheme[17]}  {scheme[24]} {scheme[25]} {scheme[26]}  {scheme[33]} {scheme[34]} ' \
              f'{scheme[35]}  {scheme[42]} {scheme[43]} {scheme[44]}'
    scheme7 = f'       {scheme[45]} {scheme[46]} {scheme[47]}'
    scheme8 = f'       {scheme[48]} {scheme[49]} {scheme[50]}'
    scheme9 = f'       {scheme[51]} {scheme[52]} {scheme[53]}'

    print(scheme1)
    print(scheme2)
    print(scheme3)
    print(scheme4)
    print(scheme5)
    print(scheme6)
    print(scheme7)
    print(scheme8)
    print(scheme9)
    print('')