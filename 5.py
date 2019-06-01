'''
https://projecteuler.net/problem=5

@math gcd, lcm

@note https://cp-algorithms.com/algebra/euclid-algorithm.html
'''

from lib import (
    calculate_execution_time,
    lcm,
    Logger,
    prime_factorization,
    ProjectEuler,
)
DEBUG = False

class ProjectEuler5(ProjectEuler):

    def logic(self, *args, **kwargs):
        ans = 1
        if len(args):
            N = args[0]
        else:
            N = kwargs['N'] if 'N' in kwargs else 20

        def logic1():
            '''
            Algorithm:
            - Get every prime factor and their count of every no from 1 to N
            - Store only the maximum count corresponding to the prime
                - Every no can be represented by product of prime numbers(of some power)
                - So to get lcm, we need every prime number used to represent number 2 to N
                - Also we need the max count, because that ensures divisiblity by prime**(less power)
                    - e.g 2**4 implies it will be divisible by 2(2**1), 4(2**2), 8(2**3), 16(2**4), 12(3*2*2) (though we need 3, 2**4 satisfies 2**2)
            - product of every prime**(corresponding max power required) will give the lcm
            TC : O(N*root(N))
            '''
            lcm = 1
            dp = {} # key: prime, value:count
            for no in range(1, N+1):
                for prime, count in prime_factorization(no):
                    dp[prime] = max(dp[prime], count) if prime in dp else count
            if DEBUG: Logger.info(f'Dict[prime, count]:\n{dp}')

            for prime, count in dp.items():
                lcm *= (prime**count)

            print(lcm)
            return lcm

        def logic2():
            '''
            Algorithm
            - lcm(a,b) = (a*b) / gcd(a,b)
            '''
            _lcm = 1
            for no in range(2, N+1):
                _lcm = lcm(_lcm, no)
            print(_lcm)
            return _lcm

        if DEBUG:
            calculate_execution_time(logic1)()
            ans = calculate_execution_time(logic2)()
        else:
            ans = logic2()

        return ans

if __name__ == '__main__':
    pe = ProjectEuler5()
    pe.solve(10)
    pe.solve(20)