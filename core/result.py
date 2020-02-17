class Result:
    """Class that represents result

    0 – Препятствие выполнения
    1 – Успешное выполнение
    2 – Во время установки возникло исключение
    """
    def __init__(self, status, message=None):
        self.status, self.message = status, message
