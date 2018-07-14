import numpy as np
import itertools
import matplotlib.pyplot as plt

def count_3APs(A,N):
    Ahat = np.fft.fft(A)
    APtot = 0
    for a in range(N):
        APtot += (Ahat[a])**2 * (Ahat[(-2*a % N)])
    return APtot / N

def main():
    nsamples = 10000
    N = 101
    AP3counts = []
    for _ in range(nsamples):
        A = np.random.randint(2, size=N)
        AP3counts.append(count_3APs(A,N).real)
    maxAPct = int(max(AP3counts))
    all_counts = np.zeros(maxAPct+1)
    for ct in AP3counts:
        all_counts[int(ct)] += 1.
    plt.plot(all_counts / nsamples)
    plt.xlabel("Number of 3APs")
    plt.ylabel("Frequency")
    plt.title("Histogram of 3APs in subsets of Z/101Z")
    plt.show()

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

if __name__ == "__main__":
    main()
