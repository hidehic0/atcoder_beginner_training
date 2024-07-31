# 全探索の練習で解きました
# https://atcoder.jp/contests/abc155/submissions/56133085

from collections import defaultdict

n = int(input())

d = defaultdict(int)

for _ in [0]*n:
    d[input()] += 1

d = dict(d)

m = max(list(d.values()))


d = {k:v for k,v in d.items() if v == m}


print('\n'.join(sorted(list(d.keys()))))

