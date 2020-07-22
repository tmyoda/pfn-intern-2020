# -*- coding: utf-8 -*-
import numpy as np
import itertools
import math


def permutation(n, r):
    return math.factorial(n) // math.factorial(n - r)


def det_3x3(A):
    x_vec, y_vec, z_vec = A[0], A[1], A[2]
    det = (x_vec[0] * y_vec[1] * z_vec[2]) \
        + (x_vec[1] * y_vec[2] * z_vec[0]) \
        + (x_vec[2] * y_vec[0] * z_vec[1]) \
        - (x_vec[0] * y_vec[2] * z_vec[1]) \
        - (x_vec[1] * y_vec[0] * z_vec[2]) \
        - (x_vec[2] * y_vec[1] * z_vec[0])

    return det


def solve(x, y, d):
    vec3_list = []
    counter = 0
    # 8通り作成
    for i in range(2 ** 3):
        b_str = bin(i)[2:].zfill(3)
        num_list = list(map(lambda b_value: x if b_value == '0' else y, b_str))
        vec3_list.append(num_list)

    # 56通り重複なし選ぶ
    choose_list = list(itertools.combinations(vec3_list, 3))

    for mat in choose_list:
        det = det_3x3(mat)

        if(abs(det) == abs(d)):
            counter += 3

    if(d == 0):
        # 0は符号関係ないので倍にする
        counter *= 2
        # ベクトルが同じ向きの選ばれ方 ＝ 総数 - Permutaition
        counter += 2 ** (3 * 3) - permutation(2 ** 3, 3)

    return counter


if __name__ == "__main__":
    # in, outのテキスト同時に開く
    with open('q1_in.txt') as f_in, open('q1_out.txt', mode='w') as f_out:
        for line in f_in:
            x, y, d = list(map(lambda v: int(v), line.rstrip('\n').split(' ')))
            print('processing', x, y, d)
            solv = solve(x, y, d)
            f_out.write('{}\n'.format(solv))
