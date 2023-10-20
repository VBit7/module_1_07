def get_employees_by_profession(path, profession):
    # Відкриваємо файл для читання
    with open(path, 'r') as file:
        # Отримуємо рядки з файлу
        lines = file.readlines()

    # Шукаємо рядки, де є вказана професія
    matching_lines = [line for line in lines if profession in line]

    # Об'єднуємо відповідні рядки в один рядок
    result = ''.join(matching_lines)

    # Прибираємо символи перенесення рядків та зайві прогалини
    result = result.replace('\n', '').strip()

    # Замінюємо значення profession на порожній рядок
    result = result.replace(profession, "")
    result = result.strip()

    return result


# Приклад використання
path = 'employees.txt'
profession = 'cook'
matching_employees = get_employees_by_profession(path, profession)
print(matching_employees)



'''
Є файл зі списком працівників компанії.
У кожному рядку файлу записано інформацію лише одного співробітника.
Формат запису, в межах навчання приймемо спрощений, такий як: ім'я співробітника, символ пропуску та його посада, тобто, ким він працює.

John courier
Pipe cook

Створіть функцію get_employees_by_profession(path, profession).
Функція повинна у файлі (параметр path) знайти всіх співробітників зазначеної професії (параметр profession)

Вимоги:

відкрийте файл за допомогою with для читання
отримайте рядки з файлу за допомогою методу readlines()
за допомогою методу find знайдіть усі рядки у файлі, де є вказана profession, та помістіть записи до списку
об'єднайте всі ці рядки в списку в один рядок за допомогою методу join
(пам'ятайте про символ перенесення рядків '\n' та зайві прогалини, які треба прибрати)
приберіть значення змінної 'profession' (замініть на порожній рядок "" методом replace)
поверніть отриманий рядок із файлу
'''