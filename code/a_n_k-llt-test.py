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

def random_set(k, n):
    result = np.zeros(n)
    total = 0
    for i in range(0, n):
        if random() < (k - total) / (n - i):
            result[i] = 1
            total += 1
    return result

def main():
    nsamples = 200000
    n = 101
    AP3counts = []
    for x in range(nsamples):
        if x % 10000 == 0:
            print("\r" + str(x), end="")
        A = random_set((n+1)/2, n)
        AP3counts.append((count_3APs(A,n).real-(n+1)/2)/2)
    print("\r" + "done               ")
    maxAPct = int(round(max(AP3counts)))
    minAPct = int(round(min(AP3counts)))
    all_counts = np.zeros(maxAPct-minAPct+1)
    for ct in AP3counts:
        all_counts[int(round(ct))-minAPct] += 1.
    plt.plot(all_counts / nsamples)
    plt.xlabel("Number of 3APs")
    plt.ylabel("Frequency")
    plt.title("Histogram of 3APs in subsets of Z/" + str(n) + "Z, fixing k=" + str((n+1)//2))
    plt.show()

if __name__ == "__main__":
    main()
