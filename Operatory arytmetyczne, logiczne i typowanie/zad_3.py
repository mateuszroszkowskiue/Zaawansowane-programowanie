def czy_parzysta(liczba: int) -> bool:
    return liczba % 2 == 0

czy_parzysta_1 = czy_parzysta(6)

if czy_parzysta_1:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")