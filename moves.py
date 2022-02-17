import random

def move(cor_pie, cor_ori, edge_pie, edge_ori, move):

    new_cor_pie = cor_pie.copy()
    new_cor_ori = cor_ori.copy()
    new_edge_pie = edge_pie.copy()
    new_edge_ori = edge_ori.copy()

    if move == 'R':

        new_cor_pie[0] = cor_pie[1]
        new_cor_pie[1] = cor_pie[4]
        new_cor_pie[4] = cor_pie[5]
        new_cor_pie[5] = cor_pie[0]

        vec1 = [1, 2, 0]
        vec2 = [2, 0, 1]

        new_cor_ori[0] = vec1[cor_ori[1]]
        new_cor_ori[4] = vec1[cor_ori[5]]
        new_cor_ori[1] = vec2[cor_ori[4]]
        new_cor_ori[5] = vec2[cor_ori[0]]

        new_edge_pie[1] = edge_pie[8]
        new_edge_pie[8] = edge_pie[5]
        new_edge_pie[5] = edge_pie[10]
        new_edge_pie[10] = edge_pie[1]

        new_edge_ori[1] = edge_ori[8]
        new_edge_ori[8] = edge_ori[5]
        new_edge_ori[5] = edge_ori[10]
        new_edge_ori[10] = edge_ori[1]

    elif move == 'L':

        new_cor_pie[2] = cor_pie[3]
        new_cor_pie[3] = cor_pie[6]
        new_cor_pie[6] = cor_pie[7]
        new_cor_pie[7] = cor_pie[2]

        vec1 = [1, 2, 0]
        vec2 = [2, 0, 1]

        new_cor_ori[2] = vec1[(cor_ori[3])]
        new_cor_ori[6] = vec1[(cor_ori[7])]
        new_cor_ori[3] = vec2[(cor_ori[6])]
        new_cor_ori[7] = vec2[(cor_ori[2])]

        new_edge_pie[3] = edge_pie[11]
        new_edge_pie[11] = edge_pie[7]
        new_edge_pie[7] = edge_pie[9]
        new_edge_pie[9] = edge_pie[3]

        new_edge_ori[3] = edge_ori[11]
        new_edge_ori[11] = edge_ori[7]
        new_edge_ori[7] = edge_ori[9]
        new_edge_ori[9] = edge_ori[3]

    elif move == 'U':

        new_cor_pie[0] = cor_pie[3]
        new_cor_pie[1] = cor_pie[0]
        new_cor_pie[2] = cor_pie[1]
        new_cor_pie[3] = cor_pie[2]

        new_cor_ori[0] = cor_ori[3]
        new_cor_ori[1] = cor_ori[0]
        new_cor_ori[2] = cor_ori[1]
        new_cor_ori[3] = cor_ori[2]

        new_edge_pie[0] = edge_pie[3]
        new_edge_pie[1] = edge_pie[0]
        new_edge_pie[2] = edge_pie[1]
        new_edge_pie[3] = edge_pie[2]

        new_edge_ori[0] = edge_ori[3]
        new_edge_ori[1] = edge_ori[0]
        new_edge_ori[2] = edge_ori[1]
        new_edge_ori[3] = edge_ori[2]

    elif move == 'D':

        new_cor_pie[4] = cor_pie[7]
        new_cor_pie[5] = cor_pie[4]
        new_cor_pie[6] = cor_pie[5]
        new_cor_pie[7] = cor_pie[6]

        new_cor_ori[4] = cor_ori[7]
        new_cor_ori[5] = cor_ori[4]
        new_cor_ori[6] = cor_ori[5]
        new_cor_ori[7] = cor_ori[6]

        new_edge_pie[4] = edge_pie[7]
        new_edge_pie[5] = edge_pie[4]
        new_edge_pie[6] = edge_pie[5]
        new_edge_pie[7] = edge_pie[6]

        new_edge_ori[4] = edge_ori[7]
        new_edge_ori[5] = edge_ori[4]
        new_edge_ori[6] = edge_ori[5]
        new_edge_ori[7] = edge_ori[6]

    elif move == 'F':

        new_cor_pie[1] = cor_pie[2]
        new_cor_pie[2] = cor_pie[7]
        new_cor_pie[4] = cor_pie[1]
        new_cor_pie[7] = cor_pie[4]

        vec1 = [1, 2, 0]
        vec2 = [2, 0, 1]

        new_cor_ori[1] = vec1[cor_ori[2]]
        new_cor_ori[2] = vec2[cor_ori[7]]
        new_cor_ori[4] = vec2[cor_ori[1]]
        new_cor_ori[7] = vec1[cor_ori[4]]

        new_edge_pie[2] = edge_pie[9]
        new_edge_pie[8] = edge_pie[2]
        new_edge_pie[4] = edge_pie[8]
        new_edge_pie[9] = edge_pie[4]

        vec3 = [1, 0]

        new_edge_ori[2] = vec3[edge_ori[9]]
        new_edge_ori[8] = vec3[edge_ori[2]]
        new_edge_ori[4] = vec3[edge_ori[8]]
        new_edge_ori[9] = vec3[edge_ori[4]]

    elif move == 'B':

        new_cor_pie[0] = cor_pie[5]
        new_cor_pie[3] = cor_pie[0]
        new_cor_pie[5] = cor_pie[6]
        new_cor_pie[6] = cor_pie[3]

        vec1 = [2, 0, 1]
        vec2 = [1, 2, 0]

        new_cor_ori[0] = vec1[(cor_ori[5])]
        new_cor_ori[3] = vec2[(cor_ori[0])]
        new_cor_ori[5] = vec2[(cor_ori[6])]
        new_cor_ori[6] = vec1[(cor_ori[3])]

        new_edge_pie[0] = edge_pie[10]
        new_edge_pie[11] = edge_pie[0]
        new_edge_pie[6] = edge_pie[11]
        new_edge_pie[10] = edge_pie[6]

        vec3 = [1, 0]

        new_edge_ori[0] = vec3[edge_ori[10]]
        new_edge_ori[11] = vec3[edge_ori[0]]
        new_edge_ori[6] = vec3[edge_ori[11]]
        new_edge_ori[10] = vec3[edge_ori[6]]

    return new_cor_pie, new_cor_ori, new_edge_pie, new_edge_ori

