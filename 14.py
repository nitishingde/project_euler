'''
https://projecteuler.net/problem=14
'''

from lib import (
    Logger,
    ProjectEuler,
)
from sys import setrecursionlimit
DEBUG = False

class ProjectEuler14(ProjectEuler):

    def logic(self, *args, **kwargs):
        ans = 1

        # without memoization
        # def collatz(n):
        #     return 1 + collatz_chain(3*n+1 if n&1 else n//2) if n != 1 else 1
        dp = {
            1:1
        }
        def collatz(n):
            if n not in dp:
                dp[n] = 1+collatz(3*n+1 if n&1 else n//2)
            return dp[n]

        for no in range(2, 1000001):
            if dp[ans] < collatz(no):
                ans = no

        print(ans)
        return ans

if __name__ == '__main__':
    pe = ProjectEuler14()
    pe.solve()
