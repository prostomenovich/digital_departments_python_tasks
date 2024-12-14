class SimpleCalc:
    """
    Класс описывает простейший калькулятор, осуществляющий
    примитивные арифметические операции над двумя числами
    """
    def __init__(self, first_arg: float, second_arg: float):
        """
        Инициализация экземпляра класса

        :param first_arg: Первое число, которое будет учавствовать в арифметических операциях
        :param second_arg: Первое число, которое будет учавствовать в арифметических операциях
        """
        self.first_arg = None
        self.second_arg = None

        self.set_first_arg(first_arg)
        self.set_second_arg(second_arg)


    def set_first_arg(self, num: float) -> None:
        """
        Позволяет установить корректное значение первого операнда для участия в арифметических операциях

        :param num: новое значение first_arg

        Example:
            >>> calc = SimpleCalc(1,2)
            >>> calc.set_first_arg(100)
            >>> print(f"first_arg = {calc.first_arg}")
            first_arg = 100
        """
        #Проверка типа переданного в метод аргумента, если строка -> ошибка
        self.first_arg = num

    def set_second_arg(self, num: float) -> None:
        """
        Позволяет установить корректное значение второго операнда для участия в арифметических операциях

        :param num: новое значение second_arg

        Example:
            >>> calc = SimpleCalc(1,2)
            >>> calc.set_second_arg(10)
            >>> print(f"second_arg = {calc.second_arg}")
            second_arg = 10
        """

        # Проверка типа переданного в метод аргумента, если строка -> ошибка
        self.second_arg = num

    def mult(self) -> float:
        """
        Выполняет сложение атрибутов first_arg и second_arg, возвращает результат сложения

        Example:
            >>> calc = SimpleCalc(4,2)
            >>> print(calc.mult())
            6
        """

        return self.first_arg + self.second_arg

    def substraction(self) -> float:
        """
        Вычитает атрибут second_arg из атрибута first_arg и возвращает результат

        Example:
            >>> calc = SimpleCalc(1, 2)
            >>> print(calc.substraction())
            -1
        """

        return  self.first_arg - self.second_arg



class Character:
    """Класс описывает некоторого персонажа и его физические действия"""
    def __init__(self, height: float, weight: float, age: int, sex: str):
        """
        Инициализация экземпляра класса

        :param height: Рост персонажа (см)
        :param weight: Вес персонажа (кг)
        :param age: Возраст персонажа (года)
        :param sex: пол персонажа
        """

        self.height = height #Необходима проверка на то, что число неотрицательное
        self.weght = weight #Необходима проверка на то, что число неотрицательное
        self.age = age #Проверка на неотрицательное число
        self.sex = sex
        self.strong = 0 #Сила персонажа
        self.money = 0 #Капитал персонажа

    def go_to_work(self) -> None:
        """Отправляет персонажа на работу, прибавляет 100 к атрибуту money"""
        pass

    def make_push_ups(self) -> None:
        """Персонаж выполняет отжимание, прибавляет 1 к силе"""
        pass

    def have_fun(self) -> None:
        """Отправляет персонажа на развлечение (минус 100 от атрибута money)"""
        pass


class Car:
    """Класс,описывающий машину"""
    def __init__(self, model: str, price: float, max_speed: int, mileage: float):
        """
        Инициализация экземпляра класса

        :param model: Модель автомобиля
        :param price: Цена автомобиля
        :param max_speed: Максимальная скорость (км/ч)
        :param mileage: Пробег
        """

        self.model = model #Проверка на строку
        self.price = price #Проверка на неотрицательное число
        self.max_speed = max_speed #Проверка на неотрицательное целое число
        self.mileage = mileage #Проверка на неотрицательное число

    def modify(self) -> None:
        """Тюнинг автомобиля увеличивает стоимость на два и максимальную скорость на 10%"""
        pass

    def ride(self) -> None:
        """Покататься на автомобиле (плюс 1 км к пробегу и минус 1% стоимости)"""
        pass

    def go_to_races(self):
        """Учавствовать в гонках (увеличивате стоимость на 20% и пробег на 20 км)"""
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()


