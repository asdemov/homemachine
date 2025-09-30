# -*- coding: utf-8 -*-

def get_num_list(high_number, low_number=0, step=-1):
    return [i for i in range(high_number, low_number, step)]


if __name__ == '__main__':
    print(get_num_list(100, step=-20))
