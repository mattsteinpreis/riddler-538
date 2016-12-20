import math
import matplotlib.pyplot as plt


def ncr(n, r):
    if r == 0: return 1
    numer = math.factorial(n)
    denom = math.factorial(r) * math.factorial(n-r)
    return numer//denom


def p_ncr(n, r):
    return ncr(n, r) / 2**n


def prob_i_decide(n):
    if n == 0:
        return 1
    if n == 1:
        return 0.5
    return p_ncr(n, n//2)


probs = [prob_i_decide(N) for N in range(10000)]
plt.plot(probs)
plt.plot(probs[:11])