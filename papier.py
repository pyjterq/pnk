import random

STONE_SYMBOL = 'S'
SCISSORS_SYMBOL = 'SC'
PAPER_SYMBOL = 'P'
ALL_SYMBOLS = {STONE_SYMBOL, SCISSORS_SYMBOL, PAPER_SYMBOL}  # set

# nie dajemy do testow


def is_symbol(value):
    return value in ALL_SYMBOLS


def get_value_from_player(player):
    # input('daj wartość: ')
    user_value = None
    done = False
    while done is False:
        value = player.get_next_value()
        if is_symbol(value) is True:
            user_value = value
            done = True
        else:
            print("Poprawna wartość to ('S','SC', 'P'): ")
    return user_value


# dajemy do testow
def get_result(v1, v2):

    # cos oblicza
    if v1 == v2:
        return "draw"
    elif v1 == "S" and v2 == "SC":
        return "P1"
    elif v1 == "S" and v2 == "P":
        return "P2"
    elif v1 == "SC" and v2 == "S":
        return "P2"
    elif v1 == "SC" and v2 == "P":
        return "P1"
    elif v1 == "P" and v2 == "S":
        return "P1"
    elif v1 == "P" and v2 == "SC":
        return "P2"


class Player:

    def get_next_value(self):
        pass

    def info(self, result):
        pass


class ConsolePlayer(Player):

    # gracz konsolowy musi wiedziec czy jest graczem pierwszym czy drugim
    def __init__(self, nr):
        self.nr = nr

    def get_next_value(self):
        return input('daj wartosc: ')

    def info(self, result_nr):
        if self.nr == result_nr:
            print(self.nr, ' Brawo!')
        elif result_nr == "draw":
            print("The match ended in a draw.")
        else:
            print(self.nr, " You fall in a battle! :( ")

        # if result == 'P1'
        # czy jesteś pierwszym graczem
        # jeśli tak to wyświetl sobie gratulacje


class ComputerPlayer(Player):
    def __init__(self, nr):
        self.nr = nr

    def get_next_value(self):
        return random.choice(['S', 'SC', 'P'])

    # jak tworzysz nowa definicja klasy to rob to ze wzgledu na ZACHOWANIE


class TestPlayer(Player):

    def __init__(self, value):
        self.value = value

    def get_next_value(self):
        return self.value  # co podrzucic? co zwrocic?


def test_example():
    p1 = TestPlayer('S')  # Kamien
    p2 = TestPlayer('SC')  # Nozyce

    result = game(p1, p2)

    assert result == 'P1'


# nie dajemy do testow
def game(player1, player2):
    v1 = get_value_from_player(player1)
    # walidacja v1 i ewentualne ponowne pobranie

    v2 = get_value_from_player(player2)
    # walidacja v2 i ewentualne ponowne pobranie

    # jakas logika
    result = get_result(v1, v2)
    # if ...
    player1.info(result)
    player2.info(result)

    return result

    # player1.info(result)
    # player2.info(result)

    # wtedy to oznaka, ze klasy maja zly interfejs (balagan w abstrakcji)
    # player1.clear_screen()  # z mysla tylko o konsoli

    # print('rezultat gry:', result)


def main():
    p1 = ConsolePlayer('P1')
    p2 = ConsolePlayer('P2')
    game(p1, p2)

    p1 = ConsolePlayer('P1')
    p2 = ComputerPlayer('P2')
    game(p1, p2)

    # p1 = RemotePlayer('P1')
    # p2 = RemotePlayer('P2')
    # game(p1, p2)


# TESTY:

# 1. automatyczne

# PODSUMOWANIE:
# 1. oznaka jesli jest kontakt ze swiatem to pomysl o abstrakcji
# 2. pisz logike tak, zeby byla rozszerzalna (przyklad funkcja game)
# 3. dbaj o przejrzyste interfesy (np. blad z clear_screen)

# WYMAGANIA:
# osobno testy (osobny moduł)
# w mailu napisz jaka komenda odpali mi testy (molizwe do odpalanie z poziomu konsoli)
# gracze w konsoli
# p, n, k
