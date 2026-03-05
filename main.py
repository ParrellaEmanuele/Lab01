from game import TriviaGame

if __name__ == "__main__":
    TriviaGame.carica_dizionario("domande.txt")
    TriviaGame.print_menu()
    TriviaGame.play()