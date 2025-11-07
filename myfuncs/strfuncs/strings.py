def is_int(number: int) -> bool:
    """
    Проверка целочисленного аргумента

    :param number: предолагается целое число
    :return: True или False
    """
    return isinstance(number, int)


def get_quoted_text(text, open_s=171, close_s=187):
    """

    Возвращает слово или текст, заключенный в пару символов

    :param text: входное слово или текст
    :param open_s: код открывающего символа
    :param close_s: код закрывающего символа
    :return: текст, заключенный в символы
    """
    return chr(open_s) + text.strip() + chr(close_s)


if __name__ == '__main__':
    assert get_quoted_text('test', open_s=ord(';'), close_s=ord(';')) == ';test;'
    assert is_int(5) == True
    assert is_int('') == False
    assert is_int(1.25) == False
    assert is_int('true') == False
    assert is_int(0) == True
