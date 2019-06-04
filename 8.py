'''
https://projecteuler.net/problem=8

@dp
@ad_hoc
'''

from lib import (
    calculate_execution_time,
    Logger,
    max,
    mul,
    ProjectEuler,
    reduce,
)
DEBUG = False

class ProjectEuler8(ProjectEuler):

    def logic(self, *args, **kwargs):
        ans = None
        N = str(args[0] if len(args) else kwargs['N'])
        digits = args[1] if len(args) == 2 else kwargs['digits']

        def logic1():
            '''
            Algorithm (Bruteforce):
            - N is str
            - Slice N[i:digits]
                - Iterate over the digits, and get their product
            '''
            mx = -1
            for i in range(0, len(N)-digits+1):
                if DEBUG: Logger.info(f'product({N[i:i+digits]}) : {reduce(mul, [int(digit) for digit in N[i:i+digits]], 1)}')
                mx = max(mx, reduce(mul, [int(digit) for digit in N[i:i+digits]], 1))
                if DEBUG: Logger.info(f'max : {mx}')
            print(mx)
            return mx

        def logic2():
            '''
            ALgorithm:
            - previous_product = x(i)*x(i+1)...x(i+digits-1)
            - next_product = (previous_product // x(i)) * x(i-digits)
            - handle case seperately when a digit is '0'
            '''
            mx = product = reduce(mul, [int(digit) for digit in N[:digits]], 1)
            for i in range(digits, len(N)):
                product = product//int(N[i-digits]) if N[i-digits] != '0' else reduce(mul, [int(digit) for digit in N[i-digits+1:i]])
                product *= int(N[i])
                if DEBUG: Logger.info(f'product({N[i:i+digits]}) : {product}')
                mx = max(mx, product)
                if DEBUG: Logger.info(f'max : {mx}')
            print(mx)
            return mx

        if DEBUG:
            ans = calculate_execution_time(logic1)()
            ans = calculate_execution_time(logic2)()
        else:
            ans = logic2()

        return ans

if __name__ == '__main__':
    pe = ProjectEuler8()
    no = '73167176531330624919225119674426574742355349194934'\
        '96983520312774506326239578318016984801869478851843'\
        '85861560789112949495459501737958331952853208805511'\
        '12540698747158523863050715693290963295227443043557'\
        '66896648950445244523161731856403098711121722383113'\
        '62229893423380308135336276614282806444486645238749'\
        '30358907296290491560440772390713810515859307960866'\
        '70172427121883998797908792274921901699720888093776'\
        '65727333001053367881220235421809751254540594752243'\
        '52584907711670556013604839586446706324415722155397'\
        '53697817977846174064955149290862569321978468622482'\
        '83972241375657056057490261407972968652414535100474'\
        '82166370484403199890008895243450658541227588666881'\
        '16427171479924442928230863465674813919123162824586'\
        '17866458359124566529476545682848912883142607690042'\
        '24219022671055626321111109370544217506941658960408'\
        '07198403850962455444362981230987879927244284909188'\
        '84580156166097919133875499200524063689912560717606'\
        '05886116467109405077541002256983155200055935729725'\
        '71636269561882670428252483600823257530420752963450'
    pe.solve(no, 4)
    pe.solve(no, 13)