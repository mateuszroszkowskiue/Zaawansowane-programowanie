def polacz_i_przeksztalc(lista1: list, lista2: list) -> list:
    unikalne_elementy = set(lista1 + lista2)
    
    wynikowa_lista = [x ** 3 for x in unikalne_elementy]
    
    return wynikowa_lista

l1 = [1, 2, 3, 2]
l2 = [3, 4, 5]

wynik = polacz_i_przeksztalc(l1, l2)
print(wynik)