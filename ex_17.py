def encode(data):
    if not data:
        return []

    def encode_recursive(data, current_element, count):
        if not data:
            return [current_element, count] if count > 0 else [current_element]

        if data[0] == current_element:
            return encode_recursive(data[1:], current_element, count + 1)
        else:
            encoded = [current_element, count] if count > 0 else [current_element]
            encoded.extend(encode_recursive(data[1:], data[0], 1))
            return encoded

    if isinstance(data, str):
        data = list(data)

    return encode_recursive(data[1:], data[0], 1)


# Приклад використання
# input_data = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]
input_data = 'XXXXXZXYYYYZZ'
encoded_list = encode(input_data)
print(encoded_list)



'''
Повернемося до попереднього завдання та виконаємо зворотне.
Напишіть рекурсивну функцію encode для кодування списку або рядка.
Як аргумент функція приймає список ( наприклад ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ])
або рядок (наприклад, "XXXZZXXYYYZZ").
Функція повинна повернути закодований список елементів (наприклад ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).
'''