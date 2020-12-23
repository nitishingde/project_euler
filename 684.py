mod = (10**9)+7
def S(N):
    if N == 0: return 0
    q = N//9
    r = N%9
    # print(q, r)
    # 5*(r^2 + 3r + 12)*10^(q-1) - 9*q - r - 6
    factor = pow(10, q-1, mod) if q else pow(10, q-1)
    ans = 5*(r*r+3*r+12)*factor-9*q-r-6
    return ans%mod



def solve(N):
    fib = [0 for _ in range(N+1)]
    fib[1] = 1
    for i in range(2, N+1):
        fib[i] = fib[i-1] + fib[i-2]


    total = 0
    for no in fib[2:]:
        total += S(no)
        total %= mod

    return total

print(solve(90))
