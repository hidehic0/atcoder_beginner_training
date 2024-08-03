# 普通にif文で解きました 2:14
# https://atcoder.jp/contests/abc365/submissions/56240682

i = int(input())

if i % 4 == 0 and i % 100 != 0:
    print(366)
elif i % 400 == 0:
    print(366)
else:
    print(365)
