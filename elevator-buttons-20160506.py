import numpy as np
from collections import defaultdict

def ride(n, k):
    choices = defaultdict()
    for i in range(k):
        c = np.random.choice(n)
        choices[c] = True
    return len(choices.keys())


def e_value(n, k, n_iter=10000):
    c = [0] * n
    for i in range(n_iter):
        r = ride(n, k) - 1
        c[r] += 1
    val = 0
    for i, v in enumerate(c):
        val += (i+1) * v / n_iter
    return val

def calc(n, m):
    return m * (1 - (1 - (1/m))**n)

if __name__ == '__main__':
    for i in range(40):
        n = np.random.randint(1, 100)
        m = np.random.randint(1, 100)
        val1 = e_value(n, m)
        val2 = calc(n, m)
        print(val1, val2)
