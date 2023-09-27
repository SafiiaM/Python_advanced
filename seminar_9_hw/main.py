from pathlib import Path


from seminar_8_hw.task_4  import csv_to_json
from task_6_next import gen_csv_with_nums, quadratic_equation
from task_4 import factorial
from task_3 import product
from task_1 import two_numbers
from task_2 import two_numbers_two

if __name__ == '__main__':
    csv_to_json(Path('file_out.csv'), Path('json_in.json'))
    print(factorial(3))
    results = two_numbers(5, 30)
    print(results)
    results()
    two_numbers_two(5, 30)
    product(8, 9, temp=7, res=4, c=6, d=3)
    print(factorial(3))
    gen_csv_with_nums()
    quadratic_equation()
