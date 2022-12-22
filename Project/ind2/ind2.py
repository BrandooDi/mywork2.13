#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys
from package.add import get_plat
from package.list import display_plats
from package.select import select_plats
from package.help import help


def main():
    """
    Главная функция программы.
    """
    # Список самолетов.
    plats = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == "exit":
            break

        elif command == "add":
            # Запросить данные о самолете.
            plat = get_plat()

            # Добавить словарь в список.
            plats.append(plat)
            # Отсортировать список в случае необходимости.
            if len(plats) > 1:
                plats.sort(key=lambda item: item.get("raspol", ""))

        elif command == "list":
            # Отобразить все платежи.
            display_plats(plats)

        elif command.startswith("select "):
            # Разбить команду на части для выделения .
            part = command.split(" ", maxsplit=1)
            com = part[1]

            # Выбрать платежи заданного типа
            selected = select_plats(plats, com)
            # Отобразить выбранные платежи
            display_plats(selected)

        elif command == "help":
            help()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == "__main__":
    main()
