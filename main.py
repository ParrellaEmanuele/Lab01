class Domanda:
    domanda: str
    punteggio: int
    opzione_corretta: str
    opzioni: [str]

    def __init__(self, domanda: str, punteggio: int, opzione_corretta: str, opzioni: [str]):
        self.domanda = domanda
        self.punteggio = punteggio
        self.opzione_corretta = opzione_corretta
        self.opzioni = opzioni
