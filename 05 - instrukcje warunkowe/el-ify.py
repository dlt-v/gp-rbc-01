"""
if warunek:

    fragment_kodu

else:

    fragment_kodu


"""

"""
if warunek:         - główny warunek
    fragment_kodu1
elif warunek:       - jeżeli warunek główny jest fałszywy, to ten warunek zostanie         
                        sprawdzony
    fragment_kodu2
elif warunek:       - jeżeli warunek nad tym jest fałszywy, to ...
    fragment_kodu3
else:
    fragment_kodu4 - else musi być na samym końcu "drabiny"

"""

# liczba = 55

# if liczba > 100:
#     print("Liczba jest większa od 100.")
# elif liczba > 50:
#     print("Liczba jest większa od 50.")
# elif liczba > 10:
#     print("Liczba jest większa od 10.")
# else:
#     print("Liczba jest mniejsza bądź równa 10.")

pieniadze = int(input("Ile masz gotówki? "))
wiek = int(input("Ile masz lat? "))

if pieniadze > 10 and wiek >= 16:
    print("Możesz wejść do kina.")
elif pieniadze <= 10 and wiek >= 16:
    print("Nie masz wystarczająco dużo pieniędzy")
elif pieniadze > 10 and wiek < 16:
    print("Nie masz wymaganego wieku.")
else:
    print("Nie masz wymaganego wieku oraz nie masz wystarczająco dużo pieniędzy")

"""
Zadanie:
Prosty kalkulator. Program wyświetli znaki działań, które można wykonywać:
- ‘+’ dla dodawania,
- ‘-’ dla odejmowania,
- itd (4 w sumie operacje)
Po wybraniu odpowiedniej opcji program zapyta o liczby potrzebne do wykonania
działania, a następnie wyświetli wynik.
Do 12:15

"""