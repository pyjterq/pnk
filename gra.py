import random

STONE_SYMBOL = 'S'
SCISSORS_SYMBOL = 'SC'
PAPER_SYMBOL = 'P'
ALL_SYMBOLS = {STONE_SYMBOL, SCISSORS_SYMBOL, PAPER_SYMBOL}  # set


# nie dajemy do testow

def is_symbol(value):
    return value in ALL_SYMBOLS


# open() as f:


text = translator.translate('hi')
print(text)


# ogolnie myslec - nie narzucaj konkretnej implementacji
#
# 1) klasa bazowa juz mialaby zdefiniowane zrodlo (np. taka metoda load(self, filename), load(self, url), load(self, a, b)
# 2) WSKAZOWKA: robiac klasy bazowe koncentruj sie na zachowaniach, a nie danych wewnatrz

class Translator:

    def translate(self, code):
        pass


class DictTranslator(Translator):

    def __init__(self, values):
        self.values = values

    def translate(self, code):
        pass


def create_dict_translator(lang):
    # na podstawie lang wybieramy odpowiedni dict
    # luka mozliwa na jakies zmiany
    return DictTranslationProvider(dajemy_dicta)


def create_dict_translator_from_ini(lang, filename):
    # wczytujesz ini
    # zmieniasz go na dict
    return DictTranslationProvider(dajemy_dicta)


class Player:

    def get_next_value(self):
        pass

    def info(self, result):
        pass

    def alert_invalid_value(self):
        pass

    def info_win(self):
        pass

    def info_draw(self):
        pass

    def info_fail(self):
        pass


class TestPlayer(Player):

    def __init__(self, value):
        self.value = value

    def get_next_value(self):
        return self.value  # co podrzucic? co zwrocic?


# NOTATKA: iteratory

# Exception

# ValueError
#
# LookupError
# * KeyError
# * IndexError


class NoNextValue(Exception):
    pass


# raise NoNextValue()


class Point:

    def __init__(x, y):
        self.x = x
        self.y = y


#  0   1   2
# [0, 10, 20]

# i == len(val

class SequenceTestPlayer(Player):
    def __init__(self, values):
        self._values = values
        self._i = 0

    def get_next_value(self):
        if self._i == len(self._values):
            raise NoNextValue()
        value = self._values[self._i]  # 1
        self._i += 1
        return value

        # <---
        # value = self.values[0]


# p = SequenceTestPlayer([1, 10, 20])

# print(p.get_next_value()) # 1
# print(p.get_next_value()) # 10
# print(p.get_next_value()) # 20

# p.get_next_value() # poleci wyjatek NoNextValue

def is_symbol(value):
    return value in ALL_SYMBOLS


def get_value_from_player(player):
    while True:
        value = player.get_next_value()
        if is_symbol(value):
            return value
        else:
            player.alert_invalid_value()


def test_stone_value():
    player = TestPlayer(STONE_SYMBOL)
    value = get_value_from_player(player)
    assert value == STONE_SYMBOL


def test_invalid_value():
    player = SequenceTestPlayer(['XYZ', 'ABC', STONE_SYMBOL])
    value = get_value_from_player(player)
    assert value == STONE_SYMBOL


# silniejsza : slabsza
# RULES = {
#     STONE_SYMBOL: SCISSORS_SYMBOL,
# }


# dajemy do testow
def get_result(v1, v2):
    # cos oblicza
    if v1 == v2:
        return "draw"
    elif v1 == STONE_SYMBOL and v2 == "SC":
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
    else:
        raise ValueError()


class ConsolePlayer(Player):

    # gracz konsolowy musi wiedziec czy jest graczem pierwszym czy drugim
    def __init__(self, nr):
        self.nr = nr

    def get_next_value(self):
        # TODO: obsluga, pytamy gracza czy na pewno chce wyjść: y/n Ctrl+C
        return input('daj wartosc: ')

    def info_win(self):
        print(self.nr, 'Brawo!')

    def info_draw(self):
        print(self.nr, 'The match ended in a draw.')

    def info_fail(self):
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


# # nie dajemy do testow
def game(player1, player2):
    v1 = get_value_from_player(player1)
    # walidacja v1 i ewentualne ponowne pobranie

    v2 = get_value_from_player(player2)
    # walidacja v2 i ewentualne ponowne pobranie

    # jakas logika
    result = get_result(v1, v2)

    if result == 'P1':
        player1.info_win()
        player2.info_fail()
    elif result == 'P2':
        player1.info_fail()
        player2.info_win()
    else:
        player1.info_draw()
        player2.info_draw()

    return result

    # player1.info(result)
    # player2.info(result)

    # wtedy to oznaka, ze klasy maja zly interfejs (balagan w abstrakcji)
    # player1.clear_screen()  # z mysla tylko o konsoli

    # print('rezultat gry:', result)


if __name__ == '__main__':
    translator = create_dict_translator('en')
    p1 = SequenceTestPlayer([STONE_SYMBOL])
    p2 = SequenceTestPlayer([SCISSORS_SYMBOL])
    print(game(p1, p2))

    # p1 = ConsolePlayer(translator)

# translations.py(w środku dwa słowniki, a każdy o nazwie: PL, EN)

# 1. Obsługa języka EN / PL . Tylko na początku.


# def main():
#     p1 = ConsolePlayer('P1')
#     p2 = ConsolePlayer('P2')
#     game(p1, p2)

#     p1 = ConsolePlayer('P1')
#     p2 = ComputerPlayer('P2')
#     game(p1, p2)

#     # p1 = RemotePlayer('P1')
#     # p2 = RemotePlayer('P2')
#     # game(p1, p2)