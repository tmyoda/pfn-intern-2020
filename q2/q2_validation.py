import unittest
import numpy as np

from q2_solver import solve

table = [' ', 'a', 'b', 'c']


def make_table():
    for i in range(4, 39 + 1):
        table.append(table[i - 3] + table[i - 2] + table[i - 1])

def dp(k, p, q):
    a_sum, b_sum, c_sum = 0, 0, 0
    for char in table[k][p-1:q]:
        if(char == 'a'):
            a_sum += 1
        elif(char == 'b'):
            b_sum += 1
        elif(char == 'c'):
            c_sum += 1

    return a_sum, b_sum, c_sum


class Q2Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        make_table()

    def test_corner_case(self):
        solv = solve(1, 1, 1)
        ans = dp(1, 1, 1)
        self.assertEqual(solv, ans)

    def test_all_seven_case(self):
        #(k, p, q)
        k = 7
        for p in range(1, 17+1):
            for q in range(p, 17+1):
                solv = solve(k, p, q)
                ans = dp(k, p, q)
                self.assertEqual(solv, ans)

    def test_case(self):
        with open('q2_in.txt') as f:
            for line in f:
                k, p, q = list(
                    map(lambda v: int(v), line.rstrip('\n').split(' ')))
                if(k > 39):
                    continue
                print('processing ', k, p, q)
                solv = solve(k, p, q)
                ans = dp(k, p, q)
                self.assertEqual(solv, ans)


if __name__ == "__main__":
    unittest.main()
