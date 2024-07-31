# 普通にソートしました
# https://atcoder.jp/contests/abc142/submissions/56148544

int(input())

l = list(map(int, input().split(" ")))

l = [(n, i + 1) for i, n in enumerate(l)]

l = sorted(l, key=lambda x: x[0])

print(" ".join([str(n) for _, n in l]))
