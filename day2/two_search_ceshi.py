#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def binary_search(data_list, find_num):
    mid_pos = int(len(data_list) / 2)  # find the middle position of the list
    mid_val = data_list[mid_pos]  # get the value by it's position
    print(data_list)
    if len(data_list) > 1:
        if mid_val > find_num:  # means the find_num is in left hand of mid_val
            print("[%s] should be in left of [%s]" % (find_num, mid_val))
            binary_search(data_list[:mid_pos], find_num)
        elif mid_val < find_num:  # means the find_num is in the right hand of mid_val
            print("[%s] should be in right of [%s]" % (find_num, mid_val))
            binary_search(data_list[mid_pos:], find_num)
        else:  # means the mid_val == find_num
            print("Find ", find_num)

    else:
        print("cannot find [%s] in data_list" % find_num)


if __name__ == '__main__':
    primes = list(range(1,100))
    binary_search(primes, 90)