import glob
import inspect
import math
import os
import shutil
import sys
import numpy as np
from timeit import Timer
import doctest

def with_os_module_func():
    function_name = inspect.currentframe().f_code.co_name
    print(f'{function_name=}')

    # s = os.getcwd() # Return the current working directory
    # print(s)
    print(s:= os.getcwd())  # Моржовый оператор

    name_f_list = dir(shutil)
    numf = len(name_f_list)

    print(f'Число функций = {numf}') # returns a list of all module functions

    # Разбиваем список на части для удобства просмотра
    # https://python-lab.ru/kak-razdelit-spisok-na-chasti-v-python
    numsect = numf // 8
    splits = np.array_split(name_f_list, numsect)
    print(f'Список функций')
    for array in splits:
        print(list(array))
    # print(f'Список функций = {name_f_list}')

def wildcard_func():
    function_name = inspect.currentframe().f_code.co_name
    print(f'{function_name=} \n')
    print('Files in directory = ',glob.glob('*.py'))


def insys_func():
    function_name = inspect.currentframe().f_code.co_name
    print(f'{function_name=} \n')
    # print(sys.stderr.write('Warning, log file not found,\nstarting a new one\n'))

    print(sys.argv)

def performance_measurement():
    # In contrast to timeit’s fine level of granularity, the profile and pstats modules
    # provide tools for identifying time critical sections in larger blocks of code.
    time1 = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
    print(f' {time1 = } ')
    time2 = Timer('a,b = b,a', 'a=1; b=2').timeit()
    print(f' {time2 = } ')

## def quality_control
## def average(values):
##     """Computes the arithmetic mean of a list of numbers.
##     >>> print(average([20, 30, 70]))
##     40.0
##     """
##     return sum(values) / len(values)


#if __name__ == "__main__":
    # with_os_module_func()
    # wildcard_func()
    # insys_func()
    # performance_measurement()
   ## doctest.testmod()