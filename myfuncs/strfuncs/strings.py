def isint(number: int) -> bool:
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
    assert isint(5) == True
    assert isint('') == False
    assert isint(1.25) == False
    assert isint('true') == False
    assert isint(0) == True
