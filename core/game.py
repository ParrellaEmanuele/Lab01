from core.domanda import Domanda
from core.player import Player
import random

class TriviaGame:
    def __init__(self) -> None:
        self.lista_domande: list[Domanda] = []

    def carica_dizionario(self, file_name: str) -> None:
        with open(file_name, "r") as f:
            cnt = 1
            testo_domanda: str = ""
            punteggio: int = 0
            opzione_corretta: str = ""
            opzioni: list[str] = []

            for line in f.readlines():
                line = line.strip()

                if cnt == 1:
                    testo_domanda = line

                elif cnt == 2:
                    punteggio = int(line)

                elif cnt == 3:
                    opzione_corretta = line
                    opzioni.append(opzione_corretta)

                elif cnt < 6:
                    opzioni.append(line)

                elif cnt == 6:
                    opzioni.append(line)
                    nuova_domanda = Domanda(testo_domanda, punteggio, opzione_corretta, opzioni)
                    self.lista_domande.append(nuova_domanda)

                else:
                    opzioni = []
                    cnt = 0

                cnt += 1

    def print_menu(self) -> None:
        print(
            f"-" * 45,
            "\nBenvenutx in Trivia Game, iniziamo a giocare!\n",
            "-" * 45,
            sep = ""
        )

    def salva_punteggio(self, n: str, p: int, file_name: str) -> None:
        storico = []

        with open(file_name, "r") as f:
            for line in f.readlines():
                line = line.strip()

                if line:
                    parti = line.split()

                    if len(parti) == 2:
                        nome_storico = parti[0]
                        punti_storico = int(parti[1])
                        storico.append((nome_storico, punti_storico))

        storico.append((n, p))
        storico.sort(key=lambda x: x[1], reverse=True)

        with open(file_name, "w") as f:
            for record in storico:
                f.write(f"{record[0]} {record[1]}\n")

    def play(self) -> None:
        player = Player()
        punteggio_max = 0
        vinto = False
        domande_per_difficolta: dict[str, list[str]] = {}

        for domanda_obj in self.lista_domande:
            punteggio_domanda = domanda_obj.punteggio

            if punteggio_domanda > punteggio_max:
                punteggio_max = punteggio_domanda

            if punteggio_domanda not in domande_per_difficolta:
                domande_per_difficolta[punteggio_domanda] = []

            domande_per_difficolta[punteggio_domanda].append(domanda_obj)

        while True:
            domanda_pescata = random.choice(domande_per_difficolta[player.points])

            risposta_corretta = domanda_pescata.opzione_corretta
            risposte_domanda = list(domanda_pescata.opzioni)

            random.shuffle(risposte_domanda)
            indice_risposta_corretta = risposte_domanda.index(risposta_corretta) + 1

            print(f"Livello {player.points}) {domanda_pescata.domanda}")
            for i in range(4):
                print(f"        {i + 1}. {risposte_domanda[i]}")

            risposta_selezionata = int(input("Inserisci la risposta: "))

            if risposta_selezionata == indice_risposta_corretta:
                player.points += 1
                print("Risposta corretta!")

                if player.points > punteggio_max:
                    vinto = True
                    break

            else:
                break

        print(f"Hai totalizzato {player.points} punti!")
        player.name = input("Inserisci tu nickname: ")

        self.salva_punteggio(player.name, player.points, "data/punti.txt")