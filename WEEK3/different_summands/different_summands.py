# Uses python3
import sys

def optimal_summands(n):
    #write your code here
    if n == 1 or n == 2:
        return [n]
    i = 1
    summands = []
    while n > 0:
        if n - i == 0:
            summands.append(i)
            return summands
        if n - i > i:
            n -= i
            summands.append(i)
        i += 1
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    string = ""
    for x in summands:
        string += " %s"%x
    print(string)
