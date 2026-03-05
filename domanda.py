from dataclasses import dataclass

@dataclass
class Domanda:
    __domanda: str
    __punteggio: int
    __opzione_corretta: str
    __opzioni: list[str]

    @property
    def domanda(self):
        return self.__domanda

    @domanda.setter
    def domanda(self, value: str):
        self.__domanda = value

    @property
    def punteggio(self):
        return self.__punteggio

    @punteggio.setter
    def punteggio(self, value: int):
        self.__punteggio = value

    @property
    def opzione_corretta(self):
        return self.__opzione_corretta

    @opzione_corretta.setter
    def opzione_corretta(self, value: str):
        self.__opzione_corretta = value

    @property
    def opzioni(self):
        return self.__opzioni

    @opzioni.setter
    def opzioni(self, value: list[str]):
        self.__opzioni = value


