#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def get_plat():
    """
    Запросить данные о платежах.
    """
    raspol = input("Расчётный счёт платильщика: ")
    raspl = input("Расчётный счет получателя: ")
    sum = input("Перечисляемая сумма в руб: ")

    # Создать словарь.
    return {
        "raspol": raspol,
        "raspl": raspl,
        "sum": sum,
    }
