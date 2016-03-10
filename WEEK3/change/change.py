# Uses python3
import sys

def get_change(n):
    #write your code here
    money = [10, 5, 1]
    result = 0
    for each in money:
        if n / each >= 1:
            data = int(n/each)
            result += data
            n -= (data*each)
        if n == 0:
            break
    return int(result)

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
