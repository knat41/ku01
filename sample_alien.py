count = 0
n, a, b, r = [int(x) for x in input().split()]
for _ in range(n):
    m, n = [int(x) for x in input().split()]
    if ((m - a)**2 + (n - b)**2) <= r**2:
        count += 1
print(count)
