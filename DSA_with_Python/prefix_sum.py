n = int(input())
q = int(input())
v = [0] * n
for i in range(n):
    v[i] = int(input())
prefix_sum = [0] * n
prefix_sum[0] = v[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + v[i]
for _ in range(q):
    L = int(input())
    R = int(input())
    L -= 1
    R -= 1
    sum = 0
    if L == 0:
        sum = prefix_sum[R]
    else:
        sum = prefix_sum[R] - prefix_sum[L - 1]
    print(sum)