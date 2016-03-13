# Uses python3
import sys
'''
def optimal_sequence(n):
    if n == 1:
        return [1]
    operations = [0, 0]
    which_op = []
    for w in range(2, n + 1):
        operation = operations[w - 1]
        operation += 1
        wh = 1
        if w > 1:
            op = 1 + w % 2 + operations[int(w/2)]
            if op < operation:
                operation = op
                wh = 2
        if w > 2:
            op = 1 + w % 3 + operations[int(w/3)]
            if op < operation:
                operation = op
                wh = 3
        which_op.append(wh)
        operations.append(operation)
    operations.remove(operations[0])
    operations.remove(operations[0])
    j = operations[-1]
    new_array = []
    for i in range(0, len(operations)):
        if operations[-(i+1)] == j:
            j -= 1
            new_array.append(which_op[-(i+1)])
    sequence = [1]
    for i in range(0, len(new_array)):
        if new_array[-(i+1)] == 1:
            sequence.append(sequence[-1]+1)
        elif new_array[-(i+1)] == 2:
            sequence.append(sequence[-1]*2)
        elif new_array[-(i+1)] == 3:
            sequence.append(sequence[-1]*3)
    return sequence

# Uses python3
import sys
'''
def optimal_sequence(n):
    if n == 1:
        return [1]
    operations = [0, 0]
    which_op = []
    for w in range(2, n + 1):
        operation = operations[w - 1]
        operation += 1
        wh = 1
        if w > 1:
            op = 1 + w % 2 + operations[int(w/2)]
            if op < operation:
                operation = op
                wh = 2
        if w > 2:
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
    return sequence

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
sequence.sort()
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
