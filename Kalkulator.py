import logging
from os import name
import numpy

# Ustawiam log:
logging.basicConfig(level=logging.DEBUG)
# , format='%(asctime)s %(message)s'), filename="logfile.log")


# Definiuję działania:
def dodawanie(liczby):
    return(sum(liczby))


def odejmowanie(liczby):
    l1 = liczby[0]
    l2 = liczby[1]
    return l1-l2


def mnozenie(liczby):
    return(numpy.product(liczby))


def dzielenie(liczby):
    l1 = liczby[0]
    l2 = liczby[1]
    return l1/l2


# Definiuję kalkulator:
def kalkulator():

    slownik_dzialan = {
        1: [dodawanie, "dodaję"],
        2: [odejmowanie, "odejmuję"],
        3: [mnozenie, "mnożę"],
        4: [dzielenie, "dzielę"]
    }
# Kontrola, czy działanie prawidłowe:
    while True:
        try:
            dzialanie = int(input(
                "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
        except ValueError:
            logging.warning("Nieprawidłowe działanie!!!")
        if dzialanie in slownik_dzialan.keys():
            break
        else:
            logging.warning("Nieprawidłowe działanie!!!")
    # Tutaj wchodzi zaczyt liczb:
    # Instrukcja:
    print("Podaj kolejne liczby, by zakończyć wprowadzanie, wciśnij enter bez podania następnej liczby:")
    print("Możesz podawać liczby całkowite oraz ułamki dziesiętne (, lub .) i ułamki zwykłe z jednym /, powodzenia!")
    i = 1
    liczby = []
    while True:
        liczba = input(f"Podaj składnik {i}:")
        # Gdyby ktoś pisał ułamek z przecinkiem:
        liczba = liczba.replace(",", ".")
        if len(liczba) == 0:
            break
        # Gdyby ktoś wpisał ułamek zwykły:
        # Tu mogą pojawić się błędy:
        try:
            if "/" in liczba:
                liczba = float(liczba.split(
                    "/")[0]) / float(liczba.split("/")[1])
            liczba = float(liczba)
            liczby.append(liczba)
            i += 1
        except:
            logging.warning("Podana wartość nie jest liczbą!!!")
        # Tutaj ustawiam ogranicznik dzielenia i odejmowania:
        if dzialanie % 2 == 0 and i > 2:
            break
    # Gdyby ktoś podał jeden składnik w dzieleniu/odejmowaniu:
    if dzialanie % 2 == 0 and len(liczby) < 2:
        liczby.append(0+int(dzialanie/4))
    # Ustawiam raport:
    raport = f"{slownik_dzialan[dzialanie][1]} "
    for i in liczby:
        raport += f"{i} i "
    raport = raport[:-3]
    logging.debug(raport)
    # Obliczanie wyniku:
    wynik = slownik_dzialan[dzialanie][0](liczby)
    logging.debug(f"Wynik to: {wynik}")
    return wynik


# Wypróbowanie:
if __name__ == "__main__":
    print(kalkulator())
