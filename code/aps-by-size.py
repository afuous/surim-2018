import numpy as np
import itertools
import matplotlib.pyplot as plt
from random import random

def count_3APs(A,N):
    Ahat = np.fft.fft(A)
    APtot = 0
    for a in range(N):
        APtot += (Ahat[a])**2 * (Ahat[(-2*a % N)])
    return APtot / N

def random_subset(size, N):
    result = np.zeros(N)
    remaining = size
    for i in range(N):
        if random() < remaining / (N - i):
            result[i] = 1
            remaining -= 1
    return result

def main():
    nsamples = 30
    N = 211
    AP3counts = []
    sizes = []
    for size in range(N + 1):
        sizes.append(size)
        count_sum = 0
        for _ in range(nsamples):
            A = random_subset(size, N)
            count_sum += count_3APs(A, N).real
        AP3counts.append(count_sum / nsamples)
    plt.scatter(sizes, AP3counts)

    xs = []
    ys = []
    for x in range(N + 1):
        xs.append(x)
        ys.append(0.0048 * x**3)
    plt.scatter(xs, ys, c="green")

    plt.legend(["simulated values", "y = 0.0048 * n^3"])

    plt.xlabel("Size of subset of Z/" + str(N) + "Z")
    plt.ylabel("Expected number of 3 long arithmetic progressions")
    plt.title("Number of arithmetic progressions versus subset size")
    plt.show()


if __name__ == "__main__":
    main()

def count_4APs(A,N):
    APtot = 0
    for a,b in itertools.product(range(N),repeat=2):
        APtot += A[a] * A[(a+b)%N] * A[(a+2*b)%N] * A[(a+3*b)%N]
    return APtot

def max_AP(A,N):
    setA = set(np.where(A==1)[0])
    max_length = 1
    for n,k in itertools.product(range(N),repeat=2):
        if k == 0:
            continue
        lenAP = 0
        pos = n
        while pos in setA:
            pos += k
            pos = pos % N
            lenAP += 1
        if lenAP > max_length:
            max_length = lenAP
    return max_length
