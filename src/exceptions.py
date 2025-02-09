class ZeroQuantityProduct(Exception):
    """Класс ошибки при нулевом количестве товара"""
    def __init__(self, message=None):
        super().__init__(message)
