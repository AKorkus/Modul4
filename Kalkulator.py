import logging
from os import name

# Ustawiam log:
logging.basicConfig(level=logging.DEBUG)
# , format='%(asctime)s %(message)s'), filename="logfile.log")

# Definiuję działania:


def dodawanie(pierwsza, druga, *args):
    suma = pierwsza + druga
    for ingredient in args:
        suma += ingredient
    return suma


def odejmowanie(pierwsza, druga):
    return pierwsza - druga


def mnozenie(pierwsza, druga, *args):
    product = pierwsza * druga
    for member in args:
        product *= member
    return product


def dzielenie(licznik, mianownik):
    return licznik/mianownik


slownik_dzialan = {
    1: [dodawanie, "Dodaję"],
    2: [odejmowanie, "Odejmuję"],
    3: [mnozenie, "Mnożę"],
    4: [dzielenie, "Dzielę"]
}


def konwerter(liczba):
    '''
    Konwerter przetwarza string "liczba" na float liczba., potrafi czytać ",", ".", "/"):
    >>> print(konwerter(23,2))
    23.2
    >>> print(konwerter(2.3))
    2.3
    >>> print(konwerter(3/2))
    1.5
    '''

    liczba = liczba.replace(",", ".")
    # Gdyby ktoś wpisał ułamek zwykły:
    if "/" in liczba:
        a, b = liczba.split("/")
        liczba = float(a)/float(b)
    liczba = float(liczba)
    return liczba


def zaczyt_liczb(dzialanie):
    """
    Funkcja zaczytuje liczby z inputu użytkownika w zależności od działania:
    1,3 (dodawanie, mnożenie):
    Dowolna ilość argumentów.
    2,4 (odejmowanie, dzielenie):
    Funkcja zaczytuje maksymalnie 2 argumenty.
    Zaczytywanie argumentów można zakończyć pustym inputem (sam enter).
    Wygenerowane inputy przetworzy na listę floatów (przy pomocy konwertera).
    Przy nieprawidłowym wprowadzeniu liczby raczy poinformować użytkownika o błędzie i zapyta jeszcze raz.
    """

    print("Podaj kolejne liczby, by zakończyć wprowadzanie, wciśnij enter bez podania następnej liczby:")
    print("Możesz podawać liczby całkowite oraz ułamki dziesiętne (, lub .) i ułamki zwykłe z jednym /, powodzenia!")
    i = 1
    liczby = []
    while True:
        liczba = input(f"Podaj składnik {i}:")
        # Gdyby ktoś pisał ułamek z przecinkiem:
        if len(liczba) == 0:
            break
        # Tu mogą pojawić się błędy:
        try:
            liczba = konwerter(liczba)
            liczby.append(liczba)
            i += 1
        except:
            logging.warning("Podana wartość nie jest liczbą!!!")
        # Tutaj ustawiam ogranicznik dzielenia i odejmowania:
        if dzialanie % 2 == 0 and i > 2:
            break
    return liczby


def wybor_dzialania():
    """
    Funkcja służy do wyboru jednego z 4 podstawowych działań:
    1: dodawanie
    2: odejmowanie
    3: mnożenie
    4: dzielenie
    Użytkownik musi wpisać jedną z 4 liczb.
    """
    while True:
        dzialanie = 0
        try:
            dzialanie = int(input(
                "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
        except ValueError:
            pass
        if dzialanie in slownik_dzialan:
            return dzialanie
        else:
            logging.warning("Wpisz jedną z tych liczb: 1, 2, 3, 4!")


def raportowanie(dzialanie, liczby):
    """
    Funkcja służy informowaniu użytkownika, jakie liczby są składane w działaniu.
    """
    raport = f"{slownik_dzialan[dzialanie][1]} "
    for i in liczby:
        raport += f"{i} i "
    if raport[-3:] == " i ":
        raport = raport[:-3]
    logging.debug(raport)
    return raport


def kalkulator():
    """
    Kalkulator składa się z kilku kroków:
    Wybór działania na podstawie jednego inputu - wywołanie funkcji wybor_dzialania.
    Wybór argumentów na podstawie serii inputów - wywołanie funkcji zaczyt_liczb.
    Raportowanie użytkownika o dokonywanym działaniu - wywołanie funkcji raportowanie.
    Obliczanie wyniku - wywołanie odpowiedniego działania z argumentami, logowanie o wyniku, zwrócenie wyniku.
    """

    dzialanie = wybor_dzialania()
    liczby = zaczyt_liczb(dzialanie)
    raportowanie(dzialanie, liczby)

    # Obliczanie wyniku:
    try:
        wynik = slownik_dzialan[dzialanie][0](*liczby)
        logging.debug(f"Wynik to: {wynik}")
        return wynik
    except:
        logging.debug("Wybrano za mało argumentów!!!")


# Wypróbowanie:
if __name__ == "__main__":
    print(kalkulator())
