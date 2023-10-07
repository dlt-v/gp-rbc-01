# Czym są funkcje wbudowane

# Przykłady to: input(), print(), str(), int()

# Metody wbudowane najcześciej są programowane w C++. Dlaczego to jest ważne?
# C++ jest o dużo szybszym językiem programowania niż Python.
# W sytuacji gdy macie wybór pomiędzy własną implemetnacjią kodu a użyciem wbudowych funkcji, o dużo szybciej będzie użycie tej drugiej opcji.

print(f"Wartość bezwględna: {abs(-10)}")
print(f"Najwyższa wartość: {max(1, 2, -4, 8, -12, 4)}")
print(f"Najmniejsza wartość: {min(1, 2, -4, 8, -12, 4)}")
print(f"Zaokrąglenie: {round(3.32525)}")
print(f"Zaokrąglenie: {round(3.92525)}")

print(f"Długość napisu (oraz później list): {len('Ala ma kota')}")
print(f"Konwersja danych z jednego typu na drugi {int('43')}")
print(f"Konwersja danych z jednego typu na drugi {str(43)}")
print(f"Konwersja danych z jednego typu na drugi {int(43.93424)}")

print(f"Konwersja boolowska {int(True)}")
print(f"Konwersja boolowska {int(False)}")

print(f"Konwersja boolowska {bool(0)}")
print(f"Konwersja boolowska {bool(-23)}") # Wszystko co nie jest zerem konwertuje się na True

print(f"Konwersja boolowska {bool('')}") # Pusty napis
print(f"Konwersja boolowska {bool('Ala ma kota')}") # Niepusty napis

print(f"Wyświetlenie typu funckji {type('Jestem str')}")
print(f"Wyświetlenie typu funckji {type(43)}")
print(f"Wyświetlenie typu funckji {type(True)}")
print(f"Wyświetlenie typu funckji {type(23.33)}")



