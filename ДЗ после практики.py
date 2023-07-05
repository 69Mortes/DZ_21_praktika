# Условие задачи:
# 1. В текстовом файле посчитать количество строк.
# 2. Для каждой отдельной строки определить количество символов и слов в ней.

# Подготавливаем переменные для удобства работы:
eng_alfavit = "abcdefghijklmnopqrstuvwxyz"              # Английский алфавит
rus_alfavit = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"       # Русский алфавит
a1 = []                                                 # Создаем пустой список для повторяющихся слов
set1 = ""                                               # Создаем пустую строку, для сохранения слов без символов
set2 = ""                                               # Создаем пустую строку, для сохранения пробельных символов
strok = 0                                               # Переменная для сохранения числа/порядкового номера строк

# Открываем ранее сохраненный файл в кодировке utf-8 (для работы с русскими буквами):
with open("hello.txt", "r", encoding='utf-8') as file:
        list1 = file.readlines()                        # Создаем переменную и сохраняем в ней функция для просмотра строк из файла
        for cikl1 in list1:                             # Создаем цикл для подсчета строк и вывода на экран 1 раз
                strok += 1                              # Сохраняем в переменную итоговое число
        print(f"1. Количество строк в файле равно {strok}\n") # Выводим на экран полученный ответ
        strok = 0                                             # Обнуляем переменную для отображения порядкового номера строки

        for cikl_1 in list1:                            # Создаем цикл для прогона строк
                strok += 1                              # Сохраняем порядковый номер строк
                small = str(cikl_1).lower()             # Делаем все символы нижнего регистра
                zamena = cikl_1.replace("\n", "")       # Удаляем артикль

                for cikl_2 in small:                    # Создаем цикл для подсчета слов и количества букв в них
                        for cikl_3 in rus_alfavit:      # Перебираем буквы русского алфавита
                                if cikl_2 == cikl_3:    # Создаем условия для поиска букв русского алфавита
                                        set1 += cikl_2  # Сохраняем полученный результат
                        for cikl_4 in eng_alfavit:      # Перебираем буквы английского алфавита
                                if cikl_2 == cikl_4:    # Создаем условия для поиска букв английского алфавита
                                        set1 += cikl_2  # Сохраняем полученный результат

                        if cikl_2 == " ":               # Создаем условие: находим в нашем списке пробельные символы
                                set1 += cikl_2          # Сохраняем вместе со словами
                                set2 += cikl_2          # Сохраняем в отдельную переменную, для подсчета

                        elif cikl_2 == "\n":            # создаем условие: находим в нашем списке конец строки
                                s1 = set1.split()       # Разбиваем нашу строку на слова
                                a1.append(s1)           # Сохраняем наши слова в список
                                slova = s1              # Сохраняем только слова в переменную
                                slov = len(slova)       # Сохраняем количество слов в переменную
                                simv = len(zamena)      # Сохраняем количество символов в строке без артикля
                                bukv = 0                # Создаем переменную для подсчета букв
                                for g in s1:            # Создаем цикл для прогона слов
                                    bukv += len(g)      # Сохраняем сумму букв из слов в строке
                                set1 = ""               # Чистим строку от предыдущих значений
                                probel = len(set2)      # Сохраняем количество пробельных символов в переменную
                                znak = simv - bukv - probel # Сохраняем в переменную количество знаков препинания
                print(f"2. Символов в строке {strok} равно: {simv}, из них:\n" # Выводим ответ на экран
                      f"слов: {slov}, букв: {bukv}, пробельных символов: {probel}, знаков препинания: {znak}")
                set2 = ""                               # Чистим строку от сохраненных ранее пробельных символов