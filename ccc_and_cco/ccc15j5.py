def solve(n, k):
    if n < k:
        return 0
    if k == 1 or k == n:
        return 1
    if mem[n][k] != -1:
        return mem[n][k]
    mem[n][k] = solve(n - 1, k - 1) + solve(n - k, k)
    return mem[n][k]
mem = [[-1 for _ in range(251)] for _ in range(251)]
print solve(int(raw_input()), int(raw_input()))
