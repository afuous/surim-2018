import numpy as np
import itertools
import matplotlib.pyplot as plt

# abcd
# acbd
# adbc
def count_four_cycles(mat, n):
    count = 0
    for a in range(0, n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                for d in range(c+1, n):
                    if mat[a][b] and mat[b][c] and mat[c][d] and mat[d][a]:
                        count += 1
                    if mat[a][c] and mat[c][b] and mat[b][d] and mat[d][a]:
                        count += 1
                    if mat[a][d] and mat[d][b] and mat[b][c] and mat[c][a]:
                        count += 1
    return count

def random_adjacency_matrix(n):
    halfzero = np.array([[0]*i + [1]*(n-i) for i in range(1, n+1)])
    mat = np.random.randint(0, 2, (n, n))
    mat = np.multiply(mat, halfzero)
    sym = mat + mat.transpose()
    return sym

def main():
    nsamples = 50000
    n = 15
    four_cycle_counts = []
    for x in range(nsamples):
        if x % 1000 == 0:
            print("\r" + str(x), end="")
        mat = random_adjacency_matrix(n)
        four_cycle_counts.append(count_four_cycles(mat, n))
    print("\rdone           ")
    maxval = int(max(four_cycle_counts))
    all_counts = np.zeros(maxval+1)
    for count in four_cycle_counts:
        all_counts[int(count)] += 1.
    plt.plot(all_counts)
    plt.xlabel("Number of 4-cycles")
    plt.ylabel("Number of graphs")
    plt.title("Histogram of 4-cycles in random graphs on " + str(n) + " vertices (" + str(nsamples) + " samples)")
    plt.show()

if __name__ == "__main__":
    main()
