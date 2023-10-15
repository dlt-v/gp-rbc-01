from datetime import datetime

uzytkownik1 = ["Tomek", "4444", 100, ["15.10.2023, 15:57 - Konto zostało utworzone."]]
uzytkownik2 = ["Marcin ", "5555", 0, ["12.10.2023, 15:57 - Konto zostało utworzone."]]
wybor = 0
saldo = 0
historia_konta = [
    "15.10.2023, 15:57 - Konto zostało utworzone."
]

def dodaj_aktywnosc(aktywnosc):
    now = datetime.now()
    czas = now.strftime("%d.%m.%Y, %H:%M") # 15.10.2023, 16:03
    historia_konta.append(f"{czas} - {aktywnosc}")

def glowne_menu():
    print("Wybierz opcję:")
    print("1. Wpłata")
    print("2. Wypłata")
    print("3. Sprawdzenie stanu konta")
    print("4. Wyświetl historię konta")
    print("5. Zakończ")

def pobierz_wybor_klienta():
    return int(input("Podaj wybór: "))

def pobierz_kwote(tekst):
    return float(input(tekst))

def wplata():
    kwota_wplaty = pobierz_kwote("Podaj kwotę do wpłaty: ")
    global saldo
    saldo += kwota_wplaty
    print(f"Stan konta po operacji wynosi {saldo} złotych")
    dodaj_aktywnosc(f"Użytkownik wpłacił kwotę {kwota_wplaty} złotych.")

def wyplata():
    kwota_wyplaty = pobierz_kwote("Podaj kwotę do wypłaty: ")
    global saldo
    if kwota_wyplaty <= saldo:
        saldo -= kwota_wyplaty
        print(f"Stan konta po operacji wynosi {saldo} złotych")
        dodaj_aktywnosc(f"Użytkownik wypłacił kwotę {kwota_wyplaty} złotych.")
    else:
        print("Nie masz wystarczająco wysokiego salda.")

def wyswietlenie_historii():
    for element in historia_konta:
        print(element)

def glowna_petla():
    global saldo
    global wybor

    while wybor != 5:
        glowne_menu()
        wybor = pobierz_wybor_klienta() 

        if wybor == 1: #Wpłata
            wplata()
        elif wybor == 2: 
            wyplata()
        elif wybor == 3:
            print(f"Twój stan konta na dziś wynosi {saldo} złotych.")
        elif wybor == 4: # Wyświetlanie historii konta
            wyswietlenie_historii()
        elif wybor == 5:
            print("Zostałeś pomyślnie wylogowany.")
        else:
            print("Niepoprawny wybór")



if input("Podaj PIN: ") == "1234":
    print("Zostałeś pomyślnie zalogowany.")
    dodaj_aktywnosc("Użytkownik został zalogowany.")
    glowna_petla()

else:

    print("Niepoprawne dane.")

"""
Zadanie:
Pozwól na utworzenie własnego użytkownika oraz logowanie do niego albo do innego użytkownika.
Czas do 16:30
"""