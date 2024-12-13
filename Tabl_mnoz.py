import random
def generate_example():  #функція генерації
    """Генерує випадковий приклад на множення."""
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2

def calculate_grade(correct, total):
    """Обчислює оцінку за 12-бальною шкалою."""
    if total == 0:
        return 0
    percentage = (correct / total) * 12
    if percentage >= 12:
        return 12
    elif percentage >= 10:
        return 10
    elif percentage >= 8:
        return 8
    elif percentage >= 6:
        return 6
    elif percentage >= 4:
        return 4
    else:
        return 2

def main():
    """Основна функція програми."""
    print("ТАБЛИЦЯ МНОЖЕННЯ")
    correct_answers = 0
    total_questions = 0
    max_questions = 15 # Максимальна кількість питань

    while total_questions < max_questions:
        num1, num2 = generate_example()
        print(f"Скільки буде {num1} * {num2}?")
        try:
            answer = int(input("Введіть вашу відповідь: "))
            total_questions += 1
            if answer == num1 * num2:
                print("Правильно! Молодець!")
                correct_answers += 1
            else:
                print(f"Неправильно. Правильна відповідь: {num1 * num2}")
        except ValueError:
            print("Будь ласка, введіть число.")

        # Перевірка, чи досягнуто максимальну кількість питань
        if total_questions >= max_questions:
            print("Досягнуто максимальну кількість питань.")
            break

        # Запит на продовження
        cont = input("Хочете продовжити? (так/ні): ").strip().lower()
        if cont != "так":
            break

    grade = calculate_grade(correct_answers, total_questions)
    print(f"Дякую за гру! Ви відповіли правильно на {correct_answers} із {total_questions} питань.")
    print(f"Ваша оцінка за 12-бальною шкалою: {grade}")

if __name__ == "__main__":
    main()