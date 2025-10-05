# -*- coding:utf-8 -*-

import os.path


def is_file(file_path):
    """
    Проверяет является ли файлом переданный объект

    :param file_path: путь к файлу и имя файла
    :return: True или False
        """
    return os.path.isfile(file_path)


def is_file_exists(file_path):
    """
    Проверяет существует ли указанный файл

    :param file_path: путь к файлу и имя файла
    :return: True или False
    """
    return os.path.exists(file_path)


if __name__ == '__main__':
    test = r'D:\Work\EnCase\ItemExtractor\tests.py'
    print(is_file_exists(test))
