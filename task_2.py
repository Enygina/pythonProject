import argparse
import logging

FILE = 'task_2.log'

logging.basicConfig(filename=FILE, filemode='a', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)


def pars():
    parser = argparse.ArgumentParser(prog='Задача №2.3 ДЗ 15',
                                     epilog='Пример: --count 5 -> [0, 1, 1, 2, 3]',
                                     description=f'Данный модуль служит для генерации чисел Фибоначчи. Принимает '
                                                f'в качестве параметра количество выведенных чисел. '
                                                 f'Модуль осуществляет запись полученных списков в файл {FILE}')

    parser.add_argument('-c', '--count', default=5, help='количество выведенных чисел Фибоначчи')
    arg = parser.parse_args()
    return fibonacci(arg.count)


def fibonacci_gen(max_count: int):
    fib1, fib2 = 0, 1
    yield fib1
    yield fib2

    count = 2

    while count < max_count:
        count += 1
        fib = fib1 + fib2
        fib1, fib2 = fib2, fib
        yield fib


def fibonacci(count):
    try:
        count = int(count)
        fibo_list = []
        for num in fibonacci_gen(count):
            fibo_list.append(num)
        logger.info(f'{count}: {fibo_list}')
    except ValueError:
        logger.error(f'{count} должно быть целым числом!')


if __name__ == '__main__':
    pars()