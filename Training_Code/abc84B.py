# beginners selectionにあったので解きました
# https://atcoder.jp/contests/abc084/submissions/56176166

import re

a,b = map(int, input().split(' '))

s = input()

p = f'\\d{{{a}}}-\\d{{{b}}}'

r = re.search(p, s)

if r:
    if r.group() == s:
        print('Yes')
    else:
        print('No')
else:
    print('No')