import numpy as np
import sys

FILE = 'output.txt'

def main():
    threshold = float(sys.argv[1])
    n = 2000

    dists = np.zeros((n, n), dtype='bool')

    with open(FILE, 'r') as f:
        for line in f.readlines():
            i, j, d = line.split(',')
            i = int(i)
            j = int(j)
            d = float(d.replace('[','').replace(']',''))
            dists[i,j] = dists[j,i] = d < threshold

    np.savetxt('distancies.txt', dists)

if __name__ == '__main__':
    main()
