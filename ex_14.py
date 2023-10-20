def to_indexed(source_file, output_file):
    # Відкриваємо вхідний файл для читання
    with open(source_file, 'r') as in_file:
        # Відкриваємо вихідний файл для запису
        with open(output_file, 'w') as out_file:
            # Ініціалізуємо лічильник рядків
            line_number = 0

            # Читаємо рядки з вхідного файлу
            for line in in_file:
                # Форматуємо рядок з порядковим номером та текстом
                indexed_line = f"{line_number}: {line}"

                # Записуємо отриманий рядок у вихідний файл
                out_file.write(indexed_line)

                # Збільшуємо лічильник рядків
                line_number += 1


# Приклад використання
source_file = 'input.txt'
output_file = 'output.txt'
to_indexed(source_file, output_file)



'''
Напишіть функцію to_indexed(source_file, output_file), яка зчитуватиме вміст файлу,
додаватиме до прочитаних рядків порядковий номер і зберігати їх у такому вигляді у новому файлі.

Кожний рядок у створеному файлі повинен починатися з його номера,
двокрапки та пробілу, після чого має йти текст рядка з вхідного файлу.

Нумерація рядків іде від 0.
'''