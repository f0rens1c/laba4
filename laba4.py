import random
import calendar
from datetime import datetime, timedelta


# Задание 1
def generate_passwords(n, k):
    """
    Генерирует N различных паролей длиной K символов, состоящих из строчных и прописных латинских букв и цифр.
    """
    import string
    characters = string.ascii_letters + string.digits
    passwords = set()
    while len(passwords) < n:
        password = ''.join(random.choice(characters) for _ in range(k))
        passwords.add(password)
    return list(passwords)

# Задание 2
def get_exam_schedule(num_exams, disciplines):
    """
    Определяет время для каждого экзамена: день недели, полный номер билета.
    """
    weekdays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница']
    times = ['9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00']
    ticket_numbers = range(1, 21)

    disciplines = disciplines.split(', ')
    disciplines = list(set(disciplines))

    for discipline in disciplines:
        weekday = random.choice(weekdays)
        time = random.choice(times)
        ticket_number = random.choice(ticket_numbers)
        print(f"Экзамен по дисциплине «{discipline}» состоится в {weekday} время {time}. Ваш счастливый билет N {ticket_number}.")

# Задание 3
def convert_days_to_date(days):
    today = datetime.now().date()
    exam_date = today + timedelta(days=days)
    return exam_date.strftime("%d %B")

# Задание 4
def predict_exam_date(start_date, n):
    """
    Предсказывает счастливую дату экзамена.
    """
    start_date = datetime.strptime(start_date, '%Y/%m/%d')
    lucky_dates = []

    while len(lucky_dates) < 3:
        candidate_date = start_date
        weekday = candidate_date.weekday()
        if weekday != 0 and not (candidate_date.day % 4 == 0):
            lucky_dates.append(candidate_date)
        start_date += timedelta(days=n)

    for date in lucky_dates:
        print(f"{date.day} {calendar.month_name[date.month]}, {calendar.day_name[date.weekday()]}")

# Задание 5
def capitalize_first_letter(text):

    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)


def reverse_string(text):
    return text[::-1]


def count_vowels(text):

    vowels = 'aeiouаяуюоеёэиы'
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


# Задание 6
def filter_list(list_a, value_to_filter):
    list_b = [x for x in list_a if x != value_to_filter]
    return list_b

# Задание 7
def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    return total


def max_sum_of_digits(numbers):
    max_sum = 0
    max_num = None
    for num in numbers:
        curr_sum = sum_of_digits(num)
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_num = num
    return max_num


def main_program():


    # Задание 1
    print()
    print("Задание 1:")
    passwords = generate_passwords(5, 8)
    print(f"Сгенерированные пароли: {', '.join(passwords)}")
    print()

    # Задание 2
    print("Задание 2:")
    get_exam_schedule(5, "Математика, Физика, Информатика, Химия, Английский")
    print()

    # Задание 3
    print("Задание 3")
    # Example usage
    days_until_exam = 3

    exam_date = convert_days_to_date(days_until_exam)
    print(f"Экзамен будет через {days_until_exam} дня,  {exam_date}.")
    print()

    # Задание 4
    print("Задание 4:")
    predict_exam_date("2024/05/01", 7)
    print()

    # Задание 5
    print("Задание 5")
    text = "Если встретишь бога, скажи ему, чтобы он оставил меня в покое!"
    print(f"Строка с заглавными первыми буквами: {capitalize_first_letter(text)}")
    print(f"Строка в обратном порядке: {reverse_string(text)}")
    print(f"Количество гласных в строке: {count_vowels(text)}")
    print()


    # Задание 6
    print("Задание 6")
    # Example usage
    list_a = [1, 2, 3, 4, 5, 3, 2, 1]
    value_to_filter = 3
    list_b = filter_list(list_a, value_to_filter)
    print(list_b)

#Задание 7
print("Задание 7")
N = int(input("Введите количество чисел: "))
numbers = []
for _ in range(N):
    num = int(input("Введите число: "))
    numbers.append(num)

result = max_sum_of_digits(numbers)
print(f"Число с максимальной суммой цифр: {result}")
main_program()
