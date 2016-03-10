# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    average = []
    super_hash = {}
    for i in range(0, len(weights)):
        data = values[i]/ weights[i]
        average.append(data)
        super_hash[data] = weights[i]
    average.sort(reverse=True)
    for i in range(0, len(weights)):
        if capacity==0:
            break
        elif capacity < super_hash[average[i]]:
            value += capacity*average[i]
            break
        else:
            value += super_hash[average[i]]*average[i]
            capacity -= super_hash[average[i]]
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
