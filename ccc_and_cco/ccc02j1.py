import sys
input = sys.stdin.readline

def f(x):
    return {
        9: ' * * *\n*     *\n*     *\n*     *\n * * *\n      *\n      *\n      *\n * * *',
        8: ' * * *\n*     *\n*     *\n*     *\n * * *\n*     *\n*     *\n*     *\n * * *',
        7: ' * * *\n      *\n      *\n      *\n\n      *\n      *\n      *\n',
        6: ' * * *\n*\n*\n*\n * * *\n*     *\n*     *\n*     *\n * * *',
        5: ' * * *\n*\n*\n*\n * * *\n      *\n      *\n      *\n * * *',
        4: '*     *\n*     *\n*     *\n * * *\n      *\n      *\n      *',
        3: ' * * *\n      *\n      *\n      *\n * * *\n      *\n      *\n      *\n * * *',
        2: ' * * *\n      *\n      *\n      *\n * * *\n*\n*\n*\n * * *',
        1: '      *\n      *\n      *\n      *\n      *\n      *',
        0: ' * * *\n*     *\n*     *\n*     *\n\n*     *\n*     *\n*     *\n * * *'
    }[x]

print (f(int(input())))
