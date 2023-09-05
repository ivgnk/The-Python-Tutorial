import math
import inspect

def round_data():
    # round(number, ndigits=None)
    # https://docs.python.org/3.11/library/functions.html#round
    print(round(.1 + .1 + .1, 10) == round(.3, 10))

def as_integer_ratio():
    n = 13
    x = round(math.pi, n)
    # x = 3.14159
    print(f'{x = }')
    x_i = x.as_integer_ratio()
    print( x_i, type(x_i))
    print(f'{x_i[0]=}  {x_i[1]=}')
    dat = x_i[0]/x_i[1]
    print(dat)
    print( x == dat )
    print( x ==  round(x_i[0]/x_i[1],n ))

def summa_func():
    function_name = inspect.currentframe().f_code.co_name
    print(f'{function_name=}')
    llst = [0.1] * 10
    print(f'   {llst = }')
    print('Традиционная сумма = ',sum(llst) == 1.0)        #  False
    print('Сумма из математики = ',math.fsum(llst) == 1.0) #    True

def divmod_func():
    # Return the tuple (x//y, x%y). Invariant: div*y + mod == x.
    function_name = inspect.currentframe().f_code.co_name
    print(f'{function_name=}')
    data = 2 ** 56
    print(f'{data=}')
    ydiv = 10
    q, r = divmod(data, ydiv)
    print(f'{q=}')
    print(f'{r=}')
    the_restore_ = q*ydiv + r
    print(f'{the_restore_=}')
    print(the_restore_ == data)

if __name__ == "__main__":
    # round_data()
    # as_integer_ratio()
    # summa_func()
    divmod_func()