from dataclasses import dataclass

class Player:
    __name: str = ""
    __points: int = 0

    def __init__(self) -> None:
        pass

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def points(self) -> int:
        return self.__points

    @points.setter
    def points(self, value: int) -> None:
        self.__points = value