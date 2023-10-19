def data_preparation(list_data):
    result = []

    for main_item in list_data:
        tmp_list = sorted(main_item)

        if len(tmp_list) > 2:
            tmp_list = tmp_list[1:-1]

        result.extend(tmp_list)
        
    result = sorted(result, reverse=True)

    # for sublist in list_data:
    #     if len(sublist) > 2:
    #         sublist.remove(max(sublist))
    #         sublist.remove(min(sublist))
    #     result.extend(sublist)

    # result.sort(reverse=True)

    return result


print(data_preparation([[1,2,3],[3,4], [5,6]]))



'''
У четвертому модулі розв'язували завдання нормалізації даних. Розширимо її.

При аналізі даних часто виникає необхідність позбавитися екстремальних значень, перш ніж почати працювати з даними далі.
Напишіть функцію data_preparation, яка приймає набір даних, список списків (Приклад: [[1,2,3],[3,4], [5,6]]).

Функція повинна видаляти з переданих списків найбільше і найменше значення, але якщо розмір списку понад два елементи.
Після видалення даних з кожного списку необхідно злити їх разом в один список, відсортувати його за зменшенням
та повернути отриманий список як результат (Для прикладу вище результат буде наступним: [6, 5, 4, 3, 2]).
'''