def czy_zawiera_liczbe(lista: list, liczba: int) -> bool:
    return liczba in lista

liczby = [4, 8, 2, 7, 10]

wynik_1 = czy_zawiera_liczbe(liczby, 8)
print(wynik_1)

wynik_2 = czy_zawiera_liczbe(liczby, 5)
print(wynik_2)