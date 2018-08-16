import numpy as np
import itertools
import matplotlib.pyplot as plt
from random import randint

def count_descents(p, n):
    count = 0
    for i in range(0, n-1):
        if p[i] > p[i+1]:
            count += 1
    return count

def random_permutation(n):
    result = []
    for i in range(0, n):
        a = randint(1, n - i)
        result.append(a)
    return result

def main():
    nsamples = 500000
    n = 1000
    counts = []
    for _ in range(nsamples):
        perm = random_permutation(n)
        counts.append(int(count_descents(perm, n).real))
    max_count = max(counts)
    min_count = min(counts)
    all_counts = np.zeros(max_count - min_count + 1)
    xs = np.arange(min_count, max_count + 1)
    ys = np.zeros(max_count - min_count + 1)
    for count in counts:
        ys[count - min_count] += 1
    plt.plot(xs, ys)
    plt.xlabel("Number of descents")
    plt.ylabel("Number of occurrences")
    plt.title("Histogram of descents in random permutations on " + str(n) + " elements (" + str(nsamples) + " trials)")
    plt.show()

if __name__ == "__main__":
    main()
