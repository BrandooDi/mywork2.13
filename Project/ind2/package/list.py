#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def display_plats(staff):
    """
    Отобразить список платежей.
    """
    # Проверить, что список платежей не пуст.
    if staff:
        # Заголовок таблицы.
        line = "+-{}-+-{}-+-{}-+-{}-+".format("-" * 4, "-" * 30, "-" * 35, "-" * 45)
        print(line)
        print(
            "| {:^4} | {:^30} | {:^35} | {:^45} |".format(
                "No",
                "Расчётный счёт платильщика",
                "Расчётный счет получателя",
                "Перечисляемая сумма в руб",
            )
        )
        print(line)

        # Вывести данные о всех платежах.
        for idx, plat in enumerate(staff, 1):
            print(
                "| {:>4} | {:<30} | {:<35} | {:>45} |".format(
                    idx,
                    plat.get("raspol", ""),
                    plat.get("raspl", ""),
                    plat.get("sum", 0),
                )
            )

        print(line)

    else:
        print("Список платежей пуст")
