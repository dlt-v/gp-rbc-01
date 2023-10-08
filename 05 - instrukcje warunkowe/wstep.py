# # if - pl. jeżeli - instrukcja warunkowa

# gotowka = 20
# wiek = 13

# wynik = gotowka >= 10 and wiek >= 16

# # print(f"Czy możesz wejść do kina na horror: {wynik}")

# if gotowka >= 10 and wiek >= 16: # po ifie musimy mieć dwukropek
#     # ten fragment kodu wykona się tylko wtedy gry warunek w ifie jest prawdziwy'

#     # indentacja - to jest sposób tworzenia fragmentów kodu w Pythonie
#     print("Możesz wejść do kina.")
# else: # "w przeciwnym wypadku"
#     print("Nie możesz wejść do kina.")

# print("To nie jest już if.")


"""
Zadanie:
Napisz program, który pobiera od użytkownika jego wzrost i sprawdził czy jest powyżej 155cm oraz poniżej 215cm. I poinformował użytkownika o tych informacjach.
Zadanie do 10:55

"""

# wartosc = int(input("Podaj swój wzrost: "))

# if wartosc > 155 and wartosc < 215:
#     print("Mieścisz się w warunku.")
# else:
#     print("Nie mieścisz się w warunku.")

"""
Zadanie 1
Napisz program, który sprawdza, czy podana przez użytkownika liczba jest parzysta czy nieparzysta, i wypisuje odpowiedni komunikat.
"""
# liczba = 8

# if liczba % 2 == 0:
#     print("Liczba jest parzysta.")
# else: 
#     print("Liczba nie jest parzysta.")


"""
Zadanie 2
Stwórz prosty program, który sprawdza, czy użytkownik podaje poprawne hasło. Jeśli wpisze hasło "tajne", to program powinien wypisać "Dostęp udzielony", w przeciwnym razie "Dostęp zabroniony". str == str
"""

dane = input("Podaj hasło: ")

if dane == 'tajne':
    print("Dostęp udzielony")
else:
    print("Dostęp zabroniony")    


