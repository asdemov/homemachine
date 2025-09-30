# -*- coding: utf-8 -*-

def get_num_list(high_number, low_number=0, step=-1):
    """
    Возвращает список чисел в убывающем порядке

    :param high_number: стартовое число
    :param low_number: конечное число
    :param step: шаг чисел (по умолчанию числа уменьшаются на 1)
    :return: список чисел, упорядоченный по убыванию
    """
    return [i for i in range(high_number, low_number, step)]


if __name__ == '__main__':
    print(get_num_list(100, step=-20))
