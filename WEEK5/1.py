__author__ = 'vokidah'




def fibbo(n, hash):
    if n in hash:
        return hash[n]
    else:
        hash[n] = fibbo(n-1, hash)+fibbo(n-2, hash)
    return hash[n]


f1, f2, n = [int(x) for x in input().split()]
hash = {}
hash[f1], hash[f2] = 0, 1

print(fibbo(n, hash))

