import random

# Список известных людей и их даты рождения в формате 'dd.mm.yyyy'
people = {
    'В.И Ленин': '22.04.1870',
    'Марк Твен': '30.11.1835',
    'Исаак Ньютон': '04.01.1643',
    'Людвиг VI': '01.01.1328',
    'Рюрик': '01.01.830',
    'Альберт Эйнштейн': '14.03.1879',
    'Наполеон Бонапарт': '15.08.1769',
    'Уильям Шекспир': '26.04.1564',
    'Галилео Галилей': '15.02.1564',
    'Джордж Вашингтон': '22.02.1732'
}

# Преобразуем словарь в список кортежей для удобства работы с random.sample
people_list = list(people.items())


# Функция для преобразования даты рождения в читабельный формат
def format_birth_date(birth_date):
    day, month, year = birth_date.split('.')
    months = {
        '01': 'января', '02': 'февраля', '03': 'марта',
        '04': 'апреля', '05': 'мая', '06': 'июня',
        '07': 'июля', '08': 'августа', '09': 'сентября',
        '10': 'октября', '11': 'ноября', '12': 'декабря'
    }
    return f"{int(day)} {months[month]} {year} года"


# Основной цикл игры
while True:
    # Выбираем 5 случайных персон
    random_people = random.sample(people_list, 5)

    # Подготавливаем списки для имен и дат рождения выбранных персон
    selected_names = [person[0] for person in random_people]
    selected_birth_dates = [person[1] for person in random_people]

    # Счетчики правильных и неправильных ответов
    correct_count = 0
    total_questions = len(selected_names)

    print("Отгадайте даты рождения для следующих известных людей:")

    # Задаем вопросы пользователю
    for i in range(total_questions):
        name = selected_names[i]
        correct_birth_date = selected_birth_dates[i]

        print(f"{i + 1}. В каком году родился {name}? (введите в формате dd.mm.yyyy): ")
        user_input = input()

        if user_input == correct_birth_date:
            print("Правильно!")
            correct_count += 1
        else:
            print(f"Неправильно. Правильный ответ: {format_birth_date(correct_birth_date)}")

    # Выводим статистику результатов
    print(f'\nКоличество правильных ответов: {correct_count}')
    print(f'Количество неправильных ответов: {total_questions - correct_count}')
    print(f'Процент правильных ответов: {correct_count * (100 / total_questions)}%')
    print(f'Процент неправильных ответов: {(total_questions - correct_count) * (100 / total_questions)}%')

    # Предлагаем пользователю начать игру заново
    play_again = input('\nХотите начать игру заново? (Да/нет): ').strip().lower()
    if play_again != 'да' and play_again != 'yes':
        break