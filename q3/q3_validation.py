import unittest

from q3_solver import solve


def solve_O2(n, a_1):
    def update(pos):
        chairs[pos] = 0
        counter = 1
        for i in reversed(range(pos)):
            if(chairs[i] == None or counter < chairs[i]):
                chairs[i] = counter
            counter += 1

        counter = 1
        for i in range(pos + 1, n):
            if(chairs[i] == None or counter < chairs[i]):
                chairs[i] = counter
            counter += 1

    chairs = [None for i in range(n)]
    # 初期位置
    update(a_1 - 1)

    even_a_sum = 0
    for j in range(2, n + 1):
        max_idx = chairs.index(max(chairs))
        update(max_idx)

        if(j % 2 == 0):
            even_a_sum += max_idx + 1

    return even_a_sum


class Q3Test(unittest.TestCase):

    def test_corner_case(self):
        # n = 1, 2, 奇数、偶数でチェック
        test_n_a1 = [(1, 1), (2, 1), (2, 2), (7, 1), (7, 7), (8, 1), (8, 2)]
        for n, a_1 in test_n_a1:
            solv = solve(n, a_1)
            ans = solve_O2(n, a_1)
            self.assertEqual(solv, ans)

    def test_case(self):
        with open('q3_in.txt') as f:
            for line in f:
                n, a_1 = list(
                    map(lambda v: int(v), line.rstrip('\n').split(' ')))
                if(n > 10000):
                    continue
                print('processing', n, a_1)
                solv = solve(n, a_1)
                ans = solve_O2(n, a_1)
                self.assertEqual(solv, ans)


if __name__ == "__main__":
    unittest.main()
