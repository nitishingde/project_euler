'''
https://projecteuler.net/problem=10
'''

from lib import (
    build_sieve,
    Logger,
    ProjectEuler,
    sum,
)
DEBUG = False

class ProjectEuler10(ProjectEuler):

    def logic(self, *args, **kwargs):
        ans = None
        if len(args):
            N = args[0]
        else:
            N = kwargs['N'] if 'N' in kwargs else 2000000

        primes, _ = build_sieve(N)
        ans = sum(primes)

        print(ans)
        return ans

if __name__ == '__main__':
    pe = ProjectEuler10()
    pe.solve(10)
    pe.solve(2000000)
