'''
Wybierz i uzupełnij jeden (lub więcej) z operatorów logicznych podanych w komentarzu,
aby uzyskać oczekiwany wynik.

'''
# print(12 > 15) # Fałsz # ==, <, !=, <=
# print(5 < 15000) # Prawda # ==, >, >=, <=
# print(120 != 120) # Fałsz # ==, >=, !=, <=
# print(60 == 15) # Fałsz # ==, <, !=, >=
# print(25.3421 == 25.3421) # Prawda # ==, <, !=, <=

'''
Bardzo często ostateczny rezultat zależy od kilku czynników. Dla przykładu,
skorzystanie z rollercoastera posiada dodatkowe ograniczenie - wzrost maksymalny.

Aby możliwe było przejechanie się wagonikiem należy być wyższym niż minimalny
wzrost, ale jednocześnie być niższym niż wzrost maksymalny. To oznacza, że musimy
spełnić oba warunki jednocześnie:
wzrost musi być większy niż 150 cm i wzrost musi być mniejszy niż 215 cm

Pobierz informacje o wzroście od użytkownika i poinformuj go czy może wejść do wagonika.

Zadanie do 16:00
'''

# wzrost = int(input("Podaj swój wzrost: "))

# wynik = wzrost < 215 and wzrost > 150

# print(f"Czy możemy wejść do wagonika: {wynik}")

'''
Do każdej linijki dopisz and, or lub not, aby uzyskać oczekiwany wynik.
'''
print(True, 25 < 140 10 == 10)
print(True, 100 >= 1 2 > 10)
print(False, 25 < 14 10 != 10)
print(False, -1 < 3 2 < 9 10 == 15)
print(True, 20.05 < 21 < 10 -10 < 20 < 150 <= 150)
print(False, 1 < 10 2 < 15 -50 == 42)
print(True, 2 == 10)