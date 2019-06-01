'''
https://projecteuler.net/problem=4

Iterting in reverse properly
@math Factorization
Palindrome
'''

from lib import (
    calculate_execution_time,
    is_palindrome,
    Logger,
    ProjectEuler,
)
DEBUG = False

class ProjectEuler4(ProjectEuler):

    def logic(self, *args, **kwargs):
        ans = -1
        if len(args):
            N = args[0]
        else:
            N = kwargs['N'] if 'N' in kwargs else 3

        def logic1():
            '''
            Algorithm:
            - Generate product of every pair of N-digit numbers (in reverse)

            Note:
            - palindrome, mfactor1, mfactor2 where palindrome = mfactor1*mfactor2
            - factor2 <= factor1 and mfactor2 <= mfactor1 always (i.e we keep it that way)
            '''
            if DEBUG: iters = 0
            n_digit_lower, n_digit_upper = (10**(N-1))-1, (10**N)-1
            mx = (0, 0, 0)   # represents: (palidrome, mfactor1, mfactor2) where palindrome = mfactor1*mfactor2 and mfactor2 <= mfactor1
            for factor1 in range(n_digit_upper, n_digit_lower, -1):
                # factor2 upper limit should be lowest N-digit number until we find a palindrome, then the lower limit will be factor2 of that palindrome
                for factor2 in range(factor1, max(n_digit_lower, mx[2]), -1):
                    product = factor1*factor2
                    if DEBUG: iters += 1
                    if is_palindrome(str(product)):
                        mx = max(mx, (product, factor1, factor2))
                        break;
                # if factor1 < mfactor2 then factor1, factor2 < mfactor2. Therefore any palindrome generated (factor1*factor2) will be lesser than the already that we found
                if factor1 < mx[2]:
                    break

            if DEBUG: Logger.info(f'Palindrome: {product} {N}-Digit factors ({factor1}, {factor2})')
            if DEBUG: Logger.info(f'Logic1 Total iterations : {iters}')
            print(mx[0])
            return mx[0]

        def logic2():
            """
            Algorithm:
            - Generate palindromes in descending order
            - Iterate over N-digit numbers TC : O(10**N)
                - Check if number|palimndrome to qualify as one of the N-digit factor of palindrome
                    - Check if other factor (palindrome/number) is N-Digit
            """
            n_digit_lower, n_digit_upper = (10**(N-1))-1, (10**N)-1
            if DEBUG: iters = 0
            for half in range(n_digit_upper, n_digit_lower, -1):
                palindrome = int(str(half)+str(half)[::-1])
                for number in range(n_digit_upper, n_digit_lower, -1):
                    if DEBUG: iters += 1
                    if palindrome % number == 0 and len(str(palindrome // number)) == N:
                        if DEBUG: Logger.info(f'Palindrome: {palindrome} {N}-Digit factors ({number}, {palindrome//number})')
                        if DEBUG: Logger.info(f'Logic2 Total iterations : {iters}')
                        print(palindrome)
                        return palindrome

        if DEBUG:
            ans = calculate_execution_time(logic1)()
            ans = calculate_execution_time(logic2)()
        else:
            ans = logic1()

        return ans

if __name__ == '__main__':
    pe = ProjectEuler4()
    pe.solve(2)
    pe.solve(3)
    # pe.solve(4)
    # pe.solve(5)
    # pe.solve(6)
    # pe.solve(7)
    # pe.solve(8)