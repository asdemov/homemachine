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
    flag = None
    if isinstance(file_path, str):
        flag = os.path.exists(file_path)
    else:
        flag = os.path.exists(str(file_path))
    return flag

