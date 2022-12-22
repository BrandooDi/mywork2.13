#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def select_plats(staff, sum):
    """
    Выбрать сумму с данным типом.
    """
    # Сформировать список  платежей.
    result = [plat for plat in staff if sum == plat.get("sum", 0)]

    # Возвратить список выбранных платежей.
    return result
