#!/usr/bin/env python3
def solve(arr, n):

    lds = [1] * n
    max = 0

    for i in range(1, n):
        for j in range(i):
            if (arr[i] < arr[j] and lds[i] < lds[j] + 1):
                lds[i] = lds[j] + 1

    for i in range(n):
        if (max < lds[i]):
            max = lds[i]

    print(max)
    return max    


if __name__ == '__main__':
    f_in = open("input.txt", "r")
    n = int(f_in.readline())
    seq = []

    for i in range(n):
        seq.append(int(f_in.readline()))        

    open("output.txt", "w").write(str(solve(seq,n)))
