import random # biblioteka do losowanie liczb
import time # biblioteka do mierzenia czasu

range(5) # Od zera do 5, range(10), od zera do 10
range(5, 10) # Od 5, do 9 (10 wyłącznie)
range(5, 10, 2) # Od 5 do 9, ale przeskakujemy co drugą liczbę - 5, 7, 9

# for liczba in range(10, 5, -2):
#     print(liczba)

# Wypisz liczby od 10 do 1 za pomocą range.

# break - służy do całkowitego wyjścia z pętli
# continue - przechodzi od razu do następnej iteracji, to co jest niżej w pętli jest pomijane.

for liczba in range(10, 0, -1):
    time.sleep(.5)
    print(liczba)

print("Wyszedłem z pętli.")


