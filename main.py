from core.game import TriviaGame

if __name__ == "__main__":
    gioco = TriviaGame()
    gioco.carica_dizionario("data/domande.txt")
    gioco.print_menu()
    gioco.play()