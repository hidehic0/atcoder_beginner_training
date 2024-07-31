# 普通にbeginners selectionにあったので解きました
# https://atcoder.jp/contests/abs/submissions/56135219

n = int(input())

l = list(map(int, input().split(" ")))

l.sort(reverse=True)

a, b = (0, 0)

for i in range(1, n + 1):
    if i  % 2 == 1:
        a += l[0]
        del l[0]
    else:
        b += l[0]
        del l[0]


print(a-b)
