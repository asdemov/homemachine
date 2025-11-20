from myfuncs.file_finctions.check_file_attr import is_file


def test_file_exists_positive():
    test_file = r'D:\Work\homemachine\myfuncs\tests\pytests\test_file_functions.py'
    assert is_file(test_file) == True


def test_file_exists_negative():
    test_file = r'D:\Work\homemachine\myfuncs\tests\pytests\test_file_functions12.py'
    assert is_file(test_file) == False


def test_file_exists_emptystring():
    s = ''
    assert is_file(s) == False


def test_file_exists_number():
    assert is_file(1) == True