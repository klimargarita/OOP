if __name__ == "__main__":
    class Metal:
        """
        Базовый класс для металлов.
        """

        def __init__(self, name: str, density: float, melting_point: float) -> None:
            """
            Инициализация металла.

            :param name: Название металла.
            :param density: Плотность металла.
            :param melting_point: Температура плавления металла.
            """
            self.name = name  # Публичный атрибут, доступный для чтения
            self.__density = density  # Инкапсуляция плотности для ограниченного доступа извне
            self.__melting_point = melting_point  # Инкапсуляция температуры плавления

        def __str__(self) -> str:
            """
            Возвращает строковое представление металла.

            :return: Строка с информацией о металле.
            """
            return f"{self.name}: Density = {self.__density}, Melting Point = {self.__melting_point}."

        def __repr__(self) -> str:
            """
            Возвращает официальное строковое представление металла.

            :return: Официальная строка.
            """
            return f"Metal(name='{self.name}', density={self.__density}, melting_point={self.__melting_point})"

        def is_malleable(self) -> bool:
            """
            Проверяет, является ли металл ковким.

            :return: True, если металл ковкий, иначе False.
            """
            # Для упрощения предположим, что все металлы в этом классе ковкие
            return True

    class Steel(Metal):
        """
                    Класс стали, наследующий признаки металлов.
                    """

        def __init__(self, name: str, density: float, melting_point: float, carbon_content: float) -> None:
            """
            Инициализация стали.

            :param name: Название стали.
            :param density: Плотность стали.
            :param melting_point: Температура плавления стали.
            :param carbon_content: Содержание углерода в стали.
            """
            super().__init__(name, density, melting_point)
            self.carbon_content = carbon_content  # Публичный атрибут содержания углерода

        def __str__(self) -> str:
            """
            Возвращает строковое представление стали.

            :return: Строка с информацией о стали.
            """
            return f"{super().__str__()} Carbon Content = {self.carbon_content}."

        def __repr__(self) -> str:
            """
            Возвращает официальное строковое представление стали.

            :return: Официальная строка.
            """
            return f"Steel(name='{self.name}', density={self._Metal__density}, melting_point={self._Metal__melting_point}, carbon_content={self.carbon_content})"

        def is_malleable(self) -> bool:
            """
            Проверяет, является ли сталь ковкой.

            Сталь может быть как ковкой, так и хрупкой в зависимости от содержания углерода.
            Если содержание углерода меньше 1%, сталь считается ковкой.

            :return: True, если сталь ковкая, иначе False.
            """
            return self.carbon_content < 1.0

    class CastIron(Metal):
        """
                    Класс чугуна, наследующий признаки металлов.
                    """

        def __init__(self, name: str, density: float, melting_point: float, silicon_content: float) -> None:
            """
            Инициализация чугуна.

            :param name: Название чугуна.
            :param density: Плотность чугуна.
            :param melting_point: Температура плавления чугуна.
            :param silicon_content: Содержание кремния в чугуне.
            """
            super().__init__(name, density, melting_point)
            self.__silicon_content = silicon_content  # Инкапсуляция содержания кремния

        def __str__(self) -> str:
            """
            Возвращает строковое представление чугуна.

            :return: Строка с информацией о чугуне.
            """
            return f"{super().__str__()} Silicon Content = {self.__silicon_content}."

        def __repr__(self) -> str:
            """
            Возвращает официальное строковое представление чугуна.

            :return: Официальная строка.
            """
            return f"CastIron(name='{self.name}', density={self._Metal__density}, melting_point={self._Metal__melting_point}, silicon_content={self.__silicon_content})"

        def is_malleable(self) -> bool:
            """
            Проверяет, является ли чугун ковким.

            Чугун обычно считается хрупким и нековким материалом.

            :return: False, так как чугун не является ковким.
            """
            return False

    pass
