import numpy as np
import itertools
import matplotlib.pyplot as plt
from random import random
from math import floor

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

def get_variance(size, N):
    nsamples = 1000
    first_moment = 0
    second_moment = 0
    for _ in range(nsamples):
        subset = random_subset(size, N)
        numAPs = count_3APs(subset, N).real
        first_moment += numAPs
        second_moment += numAPs ** 2
    first_moment /= nsamples
    second_moment /= nsamples
    return second_moment - first_moment ** 2

def is_prime(n):
    for i in range(2, floor(n**0.5)):
        if n % i == 0:
            return False
    return True

def main():
    maxN = 211
    # maxN = 101

    xaxis = []
    yaxis = []
    for n in range(5, maxN):
        if is_prime(n):
            xaxis.append(n)
            yaxis.append(get_variance(n//3, n)**0.5)
            # yaxis.append(get_variance(n//3, n))
    plt.scatter(xaxis, yaxis)

    # xs = []
    # ys = []
    # for n in range(5, maxN):
    #     xs.append(n)
    #     ys.append(0.03 * n**2)
    #     # ys.append(0.3 * n**3)
    # plt.scatter(xs, ys, c="green")

    # plt.legend(["simulated values for prime N", "y = 0.03 * n^2"])
    # plt.legend(["simulated values", "y = 0.3 * n^3"])

    plt.xscale("linear")

    plt.xlabel("N")
    # plt.ylabel("Variance(number of 3APs in A | A has size N/2)")
    plt.ylabel("Variance(number of 3APs in A | A has size N/3)")
    # plt.title("Variance of number of 3APs controlling for subset size half of N")
    plt.title("Variance of number of 3APs controlling for subset size a third of N")
    plt.show()

if __name__ == "__main__":
    main()
