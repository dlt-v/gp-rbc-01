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

# def sprawdz_modulo(a, b):
#     if b == 0:
#         print("Nie można dzielić przez zero.")
#     else:
#         if a % b == 0:
#             print("Liczba jest podzielna całkowicie.")
#         else:
#             print("Liczba nie jest dzielna całkowicie.")
    
# sprawdz_modulo(4, 0)


"""
Zadanie 2:
Napisz funkcję, która zapyta użytkownika o hasło i login. Funkcja ma zwrócić True, jeśli podano poprawne hasło i login lub False w innym przypadku.
Czas do 14:20

return True
print("Coś")

wynik = dodaj(a, b)
print(wynik)

"""


# print(login("Ada", "1111"))
# print(login("Adam123", "1234"))

"""
Zadanie 2.5
Wykorzystaj powyższą funkcję w funkcji, która pozwala na n prób logowań. Zwraca True jeśli udało się zalogować lub False jeśli przekroczono liczbę prób. 
Funkcja również musi przyjmować poprawne hasło i login.
Wprowadzenie niepoprawnej wartości n powinno zostać obsłużone (zapytanie
jednorazowe dla takich przypadków).
"""
def login(nick, haslo, popr_nick, popr_haslo):

    return nick == popr_nick and haslo == popr_haslo

def cycle_login(popr_nick = "Adam123", popr_haslo = "1234"):

    while True:
        n = int(input("Podaj liczbę prób logowań: "))
        if n < 10 and n > 0:
            break
        else:
            print("Niepoprawna wartość n, spróbuj ponownie.")
    
    proby = n # Liczba niepoprawnych logowań

    while proby > 0:
        nick = input("Podaj nick: ")
        haslo = input("Podaj hasło: ")

        if login(nick, haslo, popr_nick, popr_haslo):
            print("Poprawnie się zalogowałeś!")
            break
        else:
            proby -= 1
            print("Niepoprawne dane logowania.")
            print(f"Zostało {proby}/{n} prób.")

    if proby == 0:
        print("Konto zablokowane.")
    else:
        print(f"Witaj {popr_nick}!")

cycle_login()