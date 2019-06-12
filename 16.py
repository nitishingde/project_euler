'''
https://projecteuler.net/problem=16

@note https://www.geeksforgeeks.org/left-shift-right-shift-operators-c-cpp/
'''

from lib import (
    calculate_execution_time,
    Logger,
    pow,
    ProjectEuler,
    sum,
)
DEBUG = False

class ProjectEuler16(ProjectEuler):

    def logic(self, *args, **kwargs):
        ans = None
        if len(args):
            N = args[0]
        else:
            N = kwargs['N'] if 'N' in kwargs else 1000

        # Python handles big integers internally

        def logic1():
            return sum([int(digit) for digit in str(pow(2, N))])

        def logic2():
            # Faster way of calculating powers of 2 by using left shift
            return sum([int(digit) for digit in str(1<<N)])

        if DEBUG:
            calculate_execution_time(logic1)()
            calculate_execution_time(logic2)()
        else:
            ans = logic2()

        print(ans)
        return ans

if __name__ == '__main__':
    pe = ProjectEuler16()
    pe.solve(15)
    pe.solve(1000)
