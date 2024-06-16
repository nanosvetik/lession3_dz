# Функция для получения списка уникальных элементов
def get_unique_elements(input_list):
    # Словарь для подсчета вхождений каждого элемента
    element_counts = {}
    for element in input_list:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1

    # Создаем список уникальных элементов
    unique_elements = [element for element in element_counts if element_counts[element] == 1]
    return unique_elements

# Получаем ввод от пользователя
user_input = input("Введите элементы списка через запятую, точку с запятой или слэш: ")

# Определяем используемый разделитель
if ',' in user_input:
    delimiter = ','
elif ';' in user_input:
    delimiter = ';'
elif '/' in user_input:
    delimiter = '/'
else:
    raise ValueError("Неправильный формат ввода. Используйте только запятую, точку с запятой или слэш в качестве разделителя.")

# Разделяем строку на элементы и преобразуем их в целые числа
input_list = [int(x) for x in user_input.split(delimiter)]

# Получаем список уникальных элементов
unique_elements = get_unique_elements(input_list)

# Выводим результат
print("Результат:", unique_elements)