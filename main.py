from add_grade import add_grade
from calculate_average import calculate_average
from get_result import get_result


def main():
    grades = []

    while True:
        print("\n===== ДНЕВНИК ОЦЕНОК =====")
        print("1 — Добавить оценку")
        print("2 — Показать средний балл")
        print("3 — Показать итог")
        print("0 — Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            try:
                grade = int(input("Введите оценку от 2 до 5: "))
                grades = add_grade(grades, grade)
                print("Оценка добавлена.")
            except ValueError as error:
                print("Ошибка:", error)

        elif choice == "2":
            average = calculate_average(grades)
            if average is None:
                print("Оценок пока нет.")
            else:
                print(f"Средний балл: {average:.2f}")

        elif choice == "3":
            average = calculate_average(grades)
            print(get_result(average))

        elif choice == "0":
            print("Работа программы завершена.")
            break

        else:
            print("Неизвестная команда. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()
