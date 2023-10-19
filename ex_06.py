def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if start_letter not in riddle:
        return ''

    if reverse:
        start_index = riddle.rfind(start_letter)
        result = riddle[start_index:start_index - word_length:-1]
    else:
        start_index = riddle.find(start_letter)
        result = riddle[start_index:start_index + word_length]

    return result


riddle_1 = 'mi1rewopret'
riddle_2 = 'mi1powerret'

print(solve_riddle(riddle_1, 5, 'p', reverse=True))
print(solve_riddle(riddle_2, 5, 'p', reverse=False))
print(solve_riddle('aaatttrrr', 5, 'p', True))



'''
Всі ви, можливо, стикалися з ребусами "Знайди слово". Вони існують як текстові варіанти, так і як програми для мобільних додатків.
Нагадаємо коротко суть ребуса. У великому квадраті з набором букв необхідно знайти слово по горизонталі та інколи по вертикалі.

Реалізуйте функцію solve_riddle(riddle, word_length, start_letter, reverse=False) для знаходження слова, що шукається в рядку ребуса.

Параметри функції:

riddle - рядок із зашифрованим словом.
word_length – довжина зашифрованого слова.
start_letter - літера, з якої починається слово (мається на увазі, що до початку слова літера не зустрічається в рядку).
reverse - вказує, у якому порядку записане слово. За замовчуванням — в прямому.
Для значення True слово зашифроване у зворотньому порядку, наприклад, у рядку 'mi1rewopret' зашифроване слово 'power'.
Функція повинна повертати перше знайдене слово. Якщо слово не знайдене, повернути пустий рядок.
'''