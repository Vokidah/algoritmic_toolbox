# Uses python3
def edit_distance(s, t):
    #write your code here
    s = " "+s
    t = " "+t
    result = [len(s)*[0] for i in range(0, len(t))]
    print('')
    for j in range(0, len(result[0])):
        result[0][j] = j
    for j in range(0, len(result)):
        result[j][0] = j
    for i in range(1, len(t)):
        for j in range(1, len(s)):
            insertion = result[i][j-1] + 1
            deletion = result[i-1][j] + 1
            match = result[i-1][j-1]
            mismatch = result[i-1][j-1] + 1
            if t[i] == s[j]:
                result[i][j] = min(insertion, deletion, match)
            else:
                result[i][j] = min(insertion, deletion, mismatch)
    return result[len(t)-1][len(s)-1]


def min(a, b, c):
    if a <=b and a <=c:
        return a
    if b <= a and b <= c:
        return b
    if c <= a and c <= b:
        return c

if __name__ == "__main__":
    print(edit_distance(input(), input()))
