def file_operations(path, additional_info, start_pos, count_chars):
    # Відкриваємо файл для додавання інформації
    with open(path, 'a') as file:
        # Записуємо додаткову інформацію в кінець файлу
        file.write(additional_info)
    
    # Відкриваємо файл для читання
    with open(path, 'r') as file:
        # Переміщуємо позицію читання до start_pos
        file.seek(start_pos)
        # Зчитуємо рядок довжиною count_chars
        result = file.read(count_chars)
    
    return result


# Приклад використання
path = 'example.txt'
additional_info = 'This is additional information.'
start_pos = 10
count_chars = 20
result = file_operations(path, additional_info, start_pos, count_chars)
print(result)


'''
Реалізуйте функцію file_operations(path, additional_info, start_pos, count_chars),
яка додає додаткову інформацію в файл на шляху path з параметра additional_info,
і після цього повертає рядок з позиції start_pos довжиною count_chars.

Вимоги:

функція повинна відкривати файл за допомогою with за шляхом path в режимі додавання інформації
записувати в кінець файлу рядок additional_info
після запису функція має відкрити той самий файл для читання
прочитати та повернути рядок з позиції start_pos завдовжки count_chars за допомогою функції seek.
Важливо: для проходження завдання необхідно використовувати менеджер контексту with, методи seek, write та read.
'''