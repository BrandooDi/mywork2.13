# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from modul import func_1

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 65, 6]

    max_func = func_1()
    min_func = func_1("min")

    print(max_func(a))
    print(min_func(a))
