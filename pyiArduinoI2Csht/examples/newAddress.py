# ПРИМЕР СМЕНЫ АДРЕСА МОДУЛЯ:

# Подключаем библиотеку для работы с датчиком температуры и влажности
from pyiArduinoI2Csht import *
import sys

# Объявляем объект sht для работы с функциями и методами библиотеки pyiArduinoI2Csht.
# Если при объявлении объекта указать адрес, например, sht(0xBB),
# то пример будет работать с тем модулем, адрес которого был указан.
sht = pyiArduinoI2Csht(None, NO_BEGIN)

# Если сценарию не были переданы аргументы
if len(sys.argv) < 2:
    # Назначаем модулю адрес (0x07 < адрес < 0x7F).
    newAddress = 0x09

# Иначе
else:
    # Новый адрес - первый аргумент
    newAddress = int(sys.argv[1])

# Если датчик найден
if sht.begin():
    print("Найден датчик %#.2x" % sht.getAddress())

    # Если адрес удалось изменить
    if sht.changeAddress(newAddress):
            print("Адрес изменён на %#.2x" % sht.getAddress())

    else:
            print("Адрес не изменён!")

else:
    print("Датчик не найден!")
