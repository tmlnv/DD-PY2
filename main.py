import doctest


class User:
    def __init__(self, username: str, password: str, email: str):
        """
        Создание и подготовка к работе объекта "User"

        :param username: Имя пользователя
        :param password: Пароль пользователя
        :param email: Email пользователя

        Примеры:
        >>> user_a = User('Andy','qwerty1234', 'andy@gmail.com')  # инициализация экземпляра класса
        """
        if len(username) < 1:
            raise ValueError("Имя пользователя не может быть короче 1 символа")
        self.username = username

        if len(password) < 1:
            raise ValueError("Пароль пользователя не может быть короче 1 символа")
        self.passsword = password

        if len(email) < 1:
            raise ValueError("Почта пользователя не может быть пустой")
        if '@' not in email:
            raise ValueError("Почта пользователя должга иметь @")
        self.email = email

    def change_user_password(self, new_password: str) -> None:
        """
        Добавление нового юзера.
        :param new_password: Новый пароль

        :raise ValueError: Если пароль не соответсвует критериям, вызываем ошибку

        Примеры:
        >>> user_a = user_a = User('Andy','qwerty1234', 'andy@gmail.com')
        >>> user_a.change_user_password('admin')
        """
        if len(new_password) < 1:
            raise ValueError("Пароль пользователя не может быть короче 1 символа")
        if new_password == self.passsword:
            raise ValueError("Новый пароль должен иметь значение, отличное от старого")
        ...

    def add_user_age(self, age: int) -> None:
        """
        Добавления возраста пользователю.

        :param age: Возраст
        :raise ValueError: Если возраст не соответствует параметрам, вызываем ошибку.

        :return: Объем реально извлеченной жидкости

        Примеры:
        >>> user_a = user_a = User('Andy','qwerty1234', 'andy@gmail.com')
        >>> user_a.add_user_age(33)
        """
        if age < 0:
            raise ValueError("Возраст не может быть меньше 0")
        ...


class Headphones:
    def __init__(self, manufacturer: str, size: str, color: str):
        """
        Создание и подготовка к работе объекта "User"

        :param manufacturer: Производитель
        :param size: Размер
        :param color: Цвет

        Примеры:
        >>> airpods = Headphones('Apple','small', 'white')  # инициализация экземпляра класса
        """
        self.manufacurer = manufacturer
        self.size = size
        self.color = color

    def put_on(self) -> None:
        """
        Надеть.

        Примеры:
        >>> airpods = Headphones('Apple','small', 'white')
        >>> airpods.put_on()
        """
        ...

    def set_volume(self, value: int) -> None:
        """
        Выбрать громкость.

        :param value: Величина
        :raise ValueError: Если величина громкости не соответсвует параметрам, вызываем ошибку.

        Примеры:
        >>> airpods = Headphones('Apple','small', 'white')
        >>> airpods.set_volume(50)
        """
        if value > 100:
            raise ValueError("Громкость не может быть больше 100")
        if value < 0:
            raise ValueError("Громкость не может быть больше 100")
        ...


class Microwave:
    def __init__(self, heating_power: float, size: str, color: str):
        """
        Создание и подготовка к работе объекта "Microwave"

        :heating_power: Мощность нагрева
        :param size: Размер
        :param color: Цвет

        Примеры:
        >>> lg_microwave = Microwave(77.77,'big', 'black')  # инициализация экземпляра класса
        """
        if heating_power < 0:
            raise ValueError("Мощность нагрева не может быть меньше 0")
        self.heating_power = heating_power
        self.size = size
        self.color = color

    def turn_on(self) -> None:
        """
        Включить.

        Примеры:
        >>> lg_microwave = Microwave(77.77,'big', 'black')
        >>> lg_microwave.turn_on()
        """
        ...

    def open_mw(self, value_of_open: float) -> None:
        """
        Открыть.

        :param value_of_open: Величина открытия дверцы
        :raise ValueError: Если величина открытия дверцы не соответсвует параметрам, вызываем ошибку.

        Примеры:
        >>> lg_microwave = Microwave(77.77,'big', 'black')
        >>> lg_microwave.open_mw(0.5)
        """
        if value_of_open > 1:
            raise ValueError("Нельзя открыть дверцу больше, чем целиком")
        if value_of_open < 0:
            raise ValueError("Нельзя открыть дверцу слишком мало")
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    
