import random


# random.randint - Random Integer
# print(random.randint(0, 10))

# Zadanie:
# Wydrukuj 10 liczb losowych za pomocą funkcji random.randint().

# a = 1
# while a <= 10:
#     print(random.randint(0, 10))
#     a += 1

# Zadanie:
# Gra, gdzie gracz zgaduje wylosowaną liczbę. Jeżeli ją zgadł to gra się kończy.

# losowa_liczba = random.randint(0, 10)

# while True:
#     # Jak wyjść z pętli?
#     odp = int(input("Zgadnij liczbę od 0 do 10: "))
#     if odp == losowa_liczba:
#         # Liczba odgadnięta
#         print("Zgadłeś!")
#         break; # nowa instrukcja - wychodzi z pętli
#     else:
#         print("Nie zgadłeś, spróbuj ponownie.")
#         if odp > losowa_liczba:
#             print("Spróbuj niżej.")
#         else:
#             print("Spróbuj wyżej.")
            

# print("Koniec gry.")

"""
Kiedy użytkownik pyta i nie zgadł poprawnej wartości, podpowiedz mu czy wylosowana liczba jest wyżej, czy niżej tego co od napisał.
np.
wylosowana liczba = 6
on zgadł = 4
"Nie zgadłeś, liczba jest wyżej."

"""


"""
Napisz program, który wczyta od użytkownika liczbę całkowitą.
Wyświetli na ekranie dokładnie tyle komunikatów “Giganci Programowania”.

Osoby, które skończą niech napiszą na czacie.
"""

ilosc = int(input("Podaj ilosć powtarzanych wiadomości: "))
a = 0
while a < ilosc:
    print("Giganci Programowania")
    a += 1