# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    result = []
    segments.sort(key=lambda x: x[1])
    for s in segments:
        points.append(s.start)
        points.append(s.end)
        if s.start == s.end and s.start not in result:
            result.append(s.start)
    i = 0
    while i < int(len(points)/2):
        start = points[2*i+1]
        while i < int(len(points)/2)-1:
            if start >= points[2*(i+1)]:
                if start not in result:
                    result.append(start)
                i += 1
            else:
                if start not in result:
                    result.append(start)
                break
        i+=1
    if start >= points[2*i-2]:
        if start not in result:
            result.append(start)
    result.sort()
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
