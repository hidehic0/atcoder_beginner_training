# problemsのtrainingにあったので解きました
# https://atcoder.jp/contests/abc150/submissions/56157642

from itertools import permutations
import sys

l = list(permutations(list(range(1,int(input())+1))))

a = tuple(map(int, sys.stdin.readline().split()))
b = tuple(map(int, sys.stdin.readline().split()))

print(abs((l.index(a)+1) - (l.index(b)+1)))
