wybor = 0
saldo = 0

def glowne_menu():
    print("Wybierz opcję:")
    print("1. Wpłata")
    print("2. Wypłata")
    print("3. Sprawdzenie stanu konta")
    print("4. Zakończ")

def pobierz_wybor_klienta():
    return int(input("Podaj wybór: "))

def pobierz_kwote(tekst):
    return float(input(tekst))

def wplata():
    kwota_wplaty = pobierz_kwote("Podaj kwotę do wpłaty: ")
    global saldo
    saldo += kwota_wplaty
    print(f"Stan konta po operacji wynosi {saldo} złotych")

def wyplata():
    kwota_wyplaty = pobierz_kwote("Podaj kwotę do wypłaty: ")
    global saldo
    if kwota_wyplaty <= saldo:
        saldo -= kwota_wyplaty
        print(f"Stan konta po operacji wynosi {saldo} złotych")
    else:
        print("Nie masz wystarczająco wysokiego salda.")

while wybor != 4:
    glowne_menu()
    wybor = pobierz_wybor_klienta() 

    if wybor == 1: #Wpłata
        wplata()
    elif wybor == 2: 
        wyplata()
    elif wybor == 3:
        print(f"Twój stan konta na dziś wynosi {saldo} złotych.")
    elif wybor == 4:
        print("Zostałeś pomyślnie wylogowany.")
    else:
        print("Niepoprawny wybór")