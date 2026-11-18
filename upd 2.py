def calculate_average(grades):
    """Вычисляет средний балл. Если оценок нет, возвращает None."""
    if len(grades) == 0:
        return None
    return sum(grades) / len(grades)
