# -*- coding:utf-8 -*-
from datetime import date


def get_ru_date_list():
    """
    Возвращает список в формате ['dd', 'mm', 'yyyy']

    :return: список
    """
    return [item for item in reversed(str(date.today()).split('-'))]


def get_ru_date_from_list(splitter='.'):
    """
        Возвращает строку с датой в русском формате с произвольным разделителем.

    :param splitter: разделитель в строке даты
    :return: строка с датой
        """
    ru_date = get_ru_date_list()
    return f'{splitter}'.join(ru_date)


if __name__ == '__main__':
    print(get_ru_date_from_list())
