from multiprocessing import Pool
import numpy as np
import time
import tqdm

from q1_solver import solve
from q1_validation import bruteforce


def check_all(args):
    x, y, d = args
    try:
        assert bruteforce(x, y, d) == solve(x, y, d)
    except:
        print(x, y, d, bruteforce(x, y, d), solve(x, y, d))


if __name__ == "__main__":
    with Pool(12) as p:
        all = [(x, y, d) for x in range(-10, 10)
                for y in range(-10, 10)
                for d in range(-1000, 1000)]

        bar = tqdm.tqdm(total=len(all))
        for _ in tqdm.tqdm(p.imap_unordered(check_all, all)):
            bar.update(1)


