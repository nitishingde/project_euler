def solve(L, n):
    L = str(L)
    power = 1
    no = 2
    found = 0
    while True:
        no *= 2
        power += 1
        if no > 999999999999999:
            no //= 10
        if str(no)[:3] == L:
            found += 1
            print(no, found, power, end='\r')
            if found == n:
                print(' '*100, end='\r')
                return power

print(solve(123, 45))
# print(solve(123, 678910))
