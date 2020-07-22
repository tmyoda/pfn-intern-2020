import numpy as np

# 対角化
A = np.array([[1, 1, 1], [1, 0, 0], [0, 1, 0]])
_, P = np.linalg.eig(A)
P_inv = np.linalg.inv(P)
Lambda = np.dot(np.dot(P_inv, A), P)


def get_n_mat(n):
    assert n > 0
    if(n == 3):
        return np.array([[0, 0, 1, 1], [0, 1, 0, 1], [1, 0, 0, 1]])
    if(n == 2):
        return np.array([[0, 1, 0, 1], [1, 0, 0, 1], [0, 0, 0, 0]])
    if(n == 1):
        return np.array([[1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]])

    n = n - 3
    init_s = np.array([[0, 0, 1, 1], [0, 1, 0, 1], [1, 0, 0, 1]])
    Lambda_n = Lambda ** n
    A_n = np.dot(np.dot(P, Lambda_n), P_inv)
    X = np.dot(A_n, init_s)
    X = np.around(X).astype(np.int)

    return X


def solve(k, p, q):

    stack = [(k, p, q)]
    a_sum, b_sum, c_sum = 0, 0, 0

    while(len(stack) > 0):
        k, p, q = stack.pop()
        X = get_n_mat(k)

        # 探索終了条件
        if(p == 1 and q == X[0, 3]):
            a, b, c, _ = X[0]
            a_sum += a
            b_sum += b
            c_sum += c
            continue

        sk3 = X[0, 3] - X[1, 3] - X[2, 3]
        sk2 = X[2, 3]
        sk2_line = sk3 + sk2

        # S_{k-3}, S_{k-2}で[p,q]跨いでいたら分割
        if(p <= sk3 and sk3 < q and q <= sk2_line):
            stack.append((k - 3, p, sk3))
            stack.append((k - 2, 1, q - sk3))

        # S_{k-3}, S_{k-2}, S_{k-1}3つで[p,q]跨いでいたら3つに分割
        elif(p <= sk3 and sk2_line < q):
            stack.append((k - 3, p, sk3))
            stack.append((k - 2, 1, sk2))
            stack.append((k - 1, 1, q - sk2_line))

        # S_{k-2}, S_{k-1}で[p,q]跨いでいたら分割
        elif(sk3 < p and p <= sk2_line and sk2_line < q):
            stack.append((k - 2, p - sk3, sk2))
            stack.append((k - 1, 1, q - sk2_line))

        # 区間跨いでないときそれぞれの要素へ[p,q]調整
        else:
            if(p <= sk3):
                stack.append((k - 3, p, q))
            elif(p <= sk2_line):
                stack.append((k - 2, p - sk3, q - sk3))
            else:
                stack.append((k - 1, p - sk2_line, q - sk2_line))

    return a_sum, b_sum, c_sum


if __name__ == "__main__":
    # in, outのテキスト同時に開く
    with open('q2_in.txt', mode='r') as f_in, open('q2_out.txt', mode='w') as f_out:
        for line in f_in:
            k, p, q = list(map(lambda v: int(v), line.rstrip('\n').split(' ')))
            print('processing ', k, p, q)
            a_sum, b_sum, c_sum = solve(k, p, q)
            f_out.write('a:{0},b:{1},c:{2}\n'.format(a_sum, b_sum, c_sum))
