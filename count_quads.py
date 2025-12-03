from math import gcd
from collections import defaultdict
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
       
        t = defaultdict(lambda: defaultdict(int))
        v = defaultdict(lambda: defaultdict(int))

        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                 
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy

                 
                g = gcd(dx, abs(dy))
                sx = dx // g
                sy = dy // g

                 
                des = sx * y1 - sy * x1

                 
                key1 = (sx, sy)

                 
                key2 = (dx, dy)

                 
                t[key1][des] += 1
                v[key2][des] += 1

        
        return self.count_pairs(t) - self.count_pairs(v) // 2

     
    def count_pairs(self, mp):
        total = 0
        for inner in mp.values():
            counts = list(inner.values())
            s = sum(counts)
            run = s
            for c in counts:
                run -= c
                total += c * run
        return total
