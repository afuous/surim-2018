import numpy as np
import itertools
import matplotlib.pyplot as plt
from random import random
from math import exp, pi, sqrt

def count_3APs(A,N):
    Ahat = np.fft.fft(A)
    APtot = 0
    for a in range(N):
        APtot += (Ahat[a])**2 * (Ahat[(-2*a % N)])
    return APtot / N

def random_set(k, n):
    result = np.zeros(n)
    total = 0
    for i in range(0, n):
        if random() < (k - total) / (n - i):
            result[i] = 1
            total += 1
    return result

def doit(n, k, nsamples):
    AP3counts = []
    for x in range(nsamples):
        if x % 10000 == 0:
            print("\r" + str(x), end="")
        A = random_set(k, n)
        AP3counts.append(int(round((count_3APs(A,n).real-k)/2)))
    print("\r" + "done               ")
    maxAPct = max(AP3counts)
    minAPct = min(AP3counts)
    all_counts = np.zeros(maxAPct-minAPct+1)
    for ct in AP3counts:
        all_counts[ct-minAPct] += 1.
    return (list(range(minAPct, maxAPct+1)), all_counts / nsamples)

memoize = {}

def combinations(n, k):
    if k == 0 or n == k:
        return 1
    if (n, k) not in memoize:
        memoize[(n, k)] = combinations(n - 1, k - 1) + combinations(n - 1, k)
    return memoize[(n, k)]

def gaussian(n, k):
    return combinations(n, k) / 2**n
    # return exp(-(k-n/2)**2/(2*n))/sqrt(2*pi*n)

def main():
    nsamples = 10000
    n = 53

    size = 30
    plt.rc("font", size=size)
    plt.rc("axes", titlesize=size)
    plt.rc("xtick", labelsize=size*2/3)
    plt.rc("ytick", labelsize=size*2/3)

    for k in range(0, n+1):
        a, b = doit(n, k, nsamples)
        plt.plot(a, b * gaussian(n, k))

    plt.gca().set_xlim(left=-10, right=800)
    plt.xlabel("Number of 3APs")
    plt.ylabel("Frequency")
    plt.title("Histogram of 3APs in subsets of Z/" + str(n) + "Z, conditioned on k=0 to " + str(n))
    plt.show()

if __name__ == "__main__":
    main()
