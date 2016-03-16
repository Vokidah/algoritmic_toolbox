# Uses python3
import sys

def optimal_sequence(n):
    if n == 1:
        return [1]
    operations = [0, 0]
    which_op = []
    for w in range(2, n + 1):
        operation = operations[w - 1]
        operation += 1
        wh = 1
        op = 1 + w % 2 + operations[int(w/2)]
        if op < operation:
            operation = op
            wh = 2
        op = 1 + w % 3 + operations[int(w/3)]
        if op < operation:
            operation = op
            wh = 3
        which_op.append(wh)
        operations.append(operation)
    x = n
    sequence = [x]
    while x > 1:
        if which_op[x-2] == 3:
            x = int(x/3)
        elif which_op[x-2] == 2:
            x = int(x/2)
        elif which_op[x-2] == 1:
            x -= 1
        sequence.append(x)
        print(sequence)
    return sequence


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
sequence.sort()
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')


'''
def optimal_sequence(n):
    countOperationArray = []
    orderOfOperation = []
    countOperationArray.append(0)
    countOperationArray.append(0)

    orderOfOperation.append(1)
    orderOfOperation.append(1)

    for i in range(2,n+1):
        tmp1 = (i) - 1
        tmp2 = int(i / 2) if (i) % 2 == 0 else tmp1
        tmp3 = int(i / 3) if (i) % 3 == 0 else tmp1
        k = min(countOperationArray[tmp1],countOperationArray[tmp2],countOperationArray[tmp3])
        countOperationArray.append(k+1)
        t = tmp1 if countOperationArray[tmp1] <= countOperationArray[tmp2] and countOperationArray[tmp1] <= countOperationArray[tmp3] else tmp2 if countOperationArray[tmp2] <= countOperationArray[tmp1] and countOperationArray[tmp2] <= countOperationArray[tmp3] else tmp3 if countOperationArray[tmp3] <= countOperationArray[tmp2] and countOperationArray[tmp3] <= countOperationArray[tmp1] else tmp3
        orderOfOperation.append(t)
    #print(str(countOperationArray[len(countOperationArray)-1]))
    index = len(orderOfOperation) - 1
    arr = []
    while index != 1:
      arr.append(orderOfOperation[index])
      index = orderOfOperation[index]
    arr.reverse()
    arr.append(n)
    return arr
'''