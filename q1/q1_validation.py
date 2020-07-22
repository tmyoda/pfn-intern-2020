import unittest
import numpy as np

from q1_solver import solve, det_3x3


# 総当り
def bruteforce(x, y, d, N=3):
    counter = 0

    for i in range(2 ** (N * N)):
        b_str = bin(i)[2:].zfill(N * N)
        num_list = list(map(lambda b_value: x if b_value == '0' else y, b_str))

        A = np.array(num_list, dtype=np.int16).reshape(N, N)
        det = det_3x3(A)

        if(det == d):
            counter += 1

    return counter


class Q1Test(unittest.TestCase):
    def setUp(self):
        self.test_xy = [(2, 4), (-2, 4), (-2, -4), (0, 2)]

    def test_d_zero(self):
        d = 0
        for x, y in self.test_xy:
            self.assertEqual(solve(x, y, d), bruteforce(x, y, d))

    def test_d_plus(self):
        d = 8
        for x, y in self.test_xy:
            self.assertEqual(solve(x, y, d), bruteforce(x, y, d))

    def test_d_minus(self):
        d = -8
        for x, y in self.test_xy:
            self.assertEqual(solve(x, y, d), bruteforce(x, y, d))

    def test_case(self):
        with open('q1_in.txt') as f:
            for line in f:
                x, y, d = list(
                    map(lambda v: int(v), line.rstrip('\n').split(' ')))
                print('processing', x, y, d)
                solv = solve(x, y, d)
                ans = bruteforce(x, y, d)
                self.assertEqual(solv, ans)


if __name__ == "__main__":
    unittest.main()
