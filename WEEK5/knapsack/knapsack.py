# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = 0
    values = [(W+1)*[0] for i in range(0, len(w)+1)]
    i = 1
    while i <= len(w):
        weight = 1
        while weight <= W:
            values[i][weight] = values[i - 1][weight]
            if w[i-1] <= weight:
                val = values[i-1][weight - w[i-1]] + w[i-1]
                if val > values[i][weight]:
                    values[i][weight] = val
            weight += 1
        i += 1
    result = values[-1][-1]
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
'''

'''