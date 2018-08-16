import numpy as np
import itertools
import matplotlib.pyplot as plt
from random import random

def count_3APs(A,N):
    total = 0
    for a in range(0, N):
        for b in range(1, (N-1)//2):
            total += A[a] * A[(a + b) % N] * A[(a + 2 * b) % N]
    return total

def main():
    nsamples = 1000000
    N = 23
    x = 10
    AP3counts = []
    for a in range(nsamples):
        if a % 10000 == 0:
            print("\r" + str(a), end="")
        A = []
        for _ in range(N):
            A.append(random())
        AP3counts.append(count_3APs(A,N).real * x)
    print("\rdone          ")
    minAPct = int(min(AP3counts))
    maxAPct = int(max(AP3counts))
    all_counts = np.zeros(maxAPct-minAPct+1)
    for ct in AP3counts:
        all_counts[int(ct) - minAPct] += 1.
    plt.plot([b/x for b in range(minAPct, maxAPct+1)], all_counts / nsamples)
    plt.xlabel("\"Number of 3APs\"")
    plt.ylabel("Frequency")
    plt.title("Histogram of continuous 3APs in subsets of Z/" + str(N) + "Z")
    plt.show()

if __name__ == "__main__":
    main()
