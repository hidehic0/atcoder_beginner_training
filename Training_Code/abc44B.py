# beginners selectionにあったので解きました
# https://atcoder.jp/contests/abc044/submissions/56176325

from collections import defaultdict
import sys

d = defaultdict(int)

for t in input():
    d[t] += 1


for i in dict(d).values():
    if int(i) % 2 == 0:
        continue
    else:
        print('No')
        sys.exit()

print('Yes')