# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def func_1(type_="max"):
    def func_2(lst):
        if type_ == "max":
            return max(lst)
        else:
            return min(lst)

    return func_2
