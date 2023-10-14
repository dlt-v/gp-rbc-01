"""
Zadanie 1:

Napisz funkcję, która otrzyma dwa argumenty

pierwszym będzie liczba, którą chcemy podzielić bez reszty
a drugim argumentem będzie dzielnik. 

Należy sprawdzić czy można dokonać dzielenia

a jeśli tak zwrócić informację czy liczba jest podzielna bez reszty czy nie.

% - procent - operacja modulo

Czas do 14:05

"""

def sprawdz_modulo(a, b):
    if b == 0:
        print("Nie można dzielić przez zero.")
    else:
        if a % b == 0:
            print("Liczba jest podzielna całkowicie.")
        else:
            print("Liczba nie jest dzielna całkowicie.")
    
sprawdz_modulo(4, 0)


"""
Zadanie 2:
Napisz funkcję, która zapyta użytkownika o hasło i login. Funkcja ma zwrócić True, jeśli podano poprawne hasło i login lub False w innym przypadku.

"""