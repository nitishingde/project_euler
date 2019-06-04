'''
https://projecteuler.net/problem=9

@ad_hoc
@note https://en.wikipedia.org/wiki/Pythagorean_triple
'''

from lib import (
    Logger,
    ProjectEuler,
)
DEBUG = False

class ProjectEuler9(ProjectEuler):

    def logic(self, *args, **kwargs):
        '''
        a < b < c
        a + b + c = 1000
        a**2 + b**2 == c**2
        Algotrithm:
        - Iterate a from 1 to 1000
            - Then iterate b from a+1 to (1000-a)/2
            because
            c = 1000-a-b
            b < c
            b < 1000-a-b
            b < (1000-a)/2
                - c = 1000-a-b
                - check if a**2 + b**2 == c**2
        '''
        ans = None
        for a in range(1, 1001):
            for b in range(a+1, 1+(1000-a)//2):
                c = 1000 - a - b
                if c*c == (a*a+b*b):
                    ans = a*b*c
                    if DEBUG: Logger.info(f'a : {a}, b : {b}, c : {c}, a+b+c : {a+b+c}, abc : {ans}')
                    print(ans)
                    return ans

if __name__ == '__main__':
    pe = ProjectEuler9()
    pe.solve()