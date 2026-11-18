def get_result(average):
    """Возвращает текстовый итог по среднему баллу."""
    if average is None:
        return "Невозможно определить итог: оценок пока нет."
    if average >= 4.5:
        return "Итог: отлично!"
    if average >= 3.5:
        return "Итог: хорошо."
    if average >= 2.5:
        return "Итог: удовлетворительно."
    return "Итог: стоит повторить материал."
