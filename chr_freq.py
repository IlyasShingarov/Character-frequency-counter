sorted_alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' #Отсортированный алфавит

text = open('in.txt', encoding="utf8") # Открытие текстового файла
T = [] # Массив для хранения данных о тексте

# Считывание текста в массив символов
for line in text:
    T.extend(list(line.lower().strip()))

# Удаление недопустимых символов
length = len(T)
i = 0
while i != length:
    if not T[i].isalpha():
        T.pop(i)
        length -= 1
    else:
        i += 1

char_count = len(T) # Общее кол-во символов
# Словарь для хранения пар (символ:количество)
alpha_count = {'а': 0, 'б': 0, 'в': 0, 'г': 0, 
        'д': 0, 'е': 0, 'ё': 0, 'ж': 0, 'з': 0, 
        'и': 0 ,'й': 0,'к': 0, 'л': 0, 
        'м': 0, 'н': 0, 'о': 0, 'п': 0, 
        'р': 0, 'с': 0, 'т': 0, 'у': 0,
        'ф': 0 ,'х': 0, 'ц': 0, 'ч': 0,
        'ш': 0, 'щ': 0, 'ь':0, 'ы': 0,
        'ъ': 0, 'э': 0, 'ю': 0, 'я': 0}

# Словарь для хранения пар (символ:частота)
alpha_freq = alpha_count.copy()

# Заполнение данных с словарях
for char in alpha_count.keys():
    alpha_count[char] = T.count(char)
    alpha_freq[char] = T.count(char) / char_count

row_count = len(sorted_alpha) # Количество строк -- кол-во букв в алфавите

# Вывод таблицы №1
print(' {:^34} '.format('Таблица 1'))
print(' {:^17} {:^17} '.format('Символ', 'Частота'))
print(chr(9484), chr(9472) * 17, chr(9516), chr(9472) * 17, chr(9488), sep='')
for char in sorted_alpha:
    print(chr(9474),'{:^17}'.format(char),chr(9474),'{:^17.6f}'.format(alpha_freq[char]), chr(9474),sep='')
print(chr(9492), chr(9472) * 17, chr(9524), chr(9472) * 17, chr(9496), sep='')

# Массив кортежей (символ, кол-ву), отсортированный по убыванию кол-ва
sorted_by_freq = sorted(alpha_count.items(), key=lambda tup: tup[1], reverse=True)

# Вывод таблицы №2
print(' {:^34} '.format('Таблица 2'))
print(' {:^17} {:^17} '.format('Символ', 'Частота'))
print(chr(9484), chr(9472) * 17, chr(9516), chr(9472) * 17, chr(9488), sep='')
for i in range(row_count):
    print(chr(9474),'{:^17}'.format(sorted_by_freq[i][0]),chr(9474),'{:^17.6f}'.format(alpha_freq[sorted_by_freq[i][0]]), chr(9474),sep='')
print(chr(9492), chr(9472) * 17, chr(9524), chr(9472) * 17, chr(9496), sep='')

text.close() # Закрытие файла