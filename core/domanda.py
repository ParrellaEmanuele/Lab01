from dataclasses import dataclass

@dataclass
class Domanda:
    domanda: str
    punteggio: int
    opzione_corretta: str
    opzioni: list[str]