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
    print(get_quoted_text('test'))
