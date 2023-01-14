n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
print(f'n={n}, m={m}, k={k}, x={x}, y={y}, z={z}, t={t}, a={a}, ')
z = z - t
x = x - t
y = y - t
n = n - x - z - t
m = m - x - y - t
k = k - z - y - t
print(f'n={n}, m={m}, k={k}, x={x}, y={y}, z={z}, t={t}, a={a}, ')
print(n + m + k)
print(z + y + x)
print(a - n - m - k - z - y - x - t)
