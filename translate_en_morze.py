import random

morze = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}

print('Сегодня мы потренируемся расшифровывать морзянку.')
words = ['Google', 'Hello', 'Table', 'Door', 'Telephone']

while True:
    words_list = ', '.join(words)
    print(f'Вот список слов : {words_list}.')
    remove_append = input('Хочешь ли добавить или удалить какое-то слово?\n')
    remove_append = remove_append.lower()
    if remove_append == 'добавить':
        append_ = input('Какое слово добавить?\n')
        words.append(append_)
    elif remove_append == 'удалить':
        remove_ = input('Какое слово удалить?\n')
        remove_ = remove_.title()
        if remove_ in words:
            words.remove(remove_)
        else:
            print('Не нашёл такого слова')
            continue
    elif remove_append == 'нет':
        break
    else:
        print('Ответ может быть только: добавить/удалить/нет.')
        continue

question = int(input('Выбери, сколько вопросов задать и начнаем!\n'))
answers = []
false_answers = []


def random_(list_):
    item = random.sample(list_, 1)
    word = ''.join(item)
    # Вывод выбранного слова
    # print(word)
    return word


'''
Вывод случайного слова из списка
'''


def en_morze(word):
    result = []
    translate = 0
    word = word.lower()
    for letter in word:
        k = morze.get(letter, ' ')  # Перевод буквы
        if k != ' ':  # Если слово одно
            translate = k + " "
            result.append(translate)  # Запись в список результата
        else:  # Если несколько слов
            translate = ' '
            result.append(translate)
    output = "".join(result)  # Вывод строкой
    return output


'''
Переводчик с английского на азбуку морзе
'''


def check(word):
    print(en_morze(word))
    answer = input()
    if answer.lower() == word.lower():
        answers.append(True)
        print(f'Верно, это {word}\n')
    else:
        answers.append(False)
        false_answers.append(word)
        print(f'Неверно, это {word}\n')


'''
Проверка ответов
'''


def statistics():
    print(f'Правильных ответов: {answers.count(True)}')
    print(f'Неправильных ответов: {answers.count(False)}')
    print(f'Всего вопросов: {len(answers)}\n')


'''
Подсчёт правильных/неприавльных ответов
'''

while len(answers) != question:
    word = random_(words)
    check(word)
statistics()

# Вывод списка с неправильными ответами
# print(false_answers)
if len(false_answers) > 0:
    print('Отработать слова, на которые ответил неправильно?')
    false_answer = input('Yes or No?\n')
    false_answer = false_answer.lower()

for i in range(len(false_answers)):  # Вывод теста на неправильные ответы
    if false_answer == 'yes':
        word = random_(false_answers)
        check(word)
    elif false_answer == 'no':
        break
    else:
        continue
print('На этом всё.')
