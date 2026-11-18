def add_grade(grades, grade):
    """Добавляет оценку в список и возвращает обновлённый список."""
    if grade < 2 or grade > 5:
        raise ValueError("Оценка должна быть от 2 до 5.")
    return grades + [grade]
