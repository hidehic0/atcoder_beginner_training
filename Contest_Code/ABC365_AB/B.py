# 普通に降順にソートして書きました
# https://atcoder.jp/contests/abc365/submissions/56248278

# ↓意味のないinput
input()

L = list(map(int, input().split(" ")))

T = sorted(L, reverse=True)

print(L.index(T[1]) + 1)
