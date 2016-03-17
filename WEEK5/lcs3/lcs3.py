#Uses python3

import sys

def lcs3(a, b, c):
    #write your code here
    result = [[(len(a)+1)*[0] for i in range(0, len(b)+1)] for i in range(0, len(c)+1)]
    for i in range(1, len(c) + 1):
        for j in range(1, len(b)+1):
            for k in range(1, len(a)+1):
                first = result[i-1][j-1][k-1]
                second = result[i-1][j-1][k]
                third = result[i-1][j][k-1]
                fourth = result[i-1][j][k]
                fifth = result[i][j-1][k-1]
                sixth = result[i][j-1][k]
                seventh = result[i][j][k-1]
                if c[i-1] == b[j-1] and c[i-1] == a[k-1] and b[j-1] == a[k-1]:
                    result[i][j][k] = max(first + 1, second, third, fourth, fifth, sixth, seventh)
                else:
                    result[i][j][k] = max(first, second,third,fourth, fifth, sixth,seventh)
    return result[len(c)][len(b)][len(a)]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
