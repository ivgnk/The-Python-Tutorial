import glob
import inspect
import math
import os
import shutil
import sys
import numpy as np

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
    print(sys.stderr.write('Warning, log file not found,\nstarting a new one\n'))


if __name__ == "__main__":
    # with_os_module_func()
    # wildcard_func()
    # insys_func()
    print(math.ulp(0.1))
