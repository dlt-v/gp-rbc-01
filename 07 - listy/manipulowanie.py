import random
# Manipulacja indeksami

lista_losowych_liczb = []

for element in range(20):
    lista_losowych_liczb.append(random.randint(0, 100))

print(lista_losowych_liczb)

# print(lista_losowych_liczb[0:10])
# print(lista_losowych_liczb[10:25]) # Dostęp do specyficznej porcji listy.

# print(lista_losowych_liczb[-1]) # Ostatni element tablicy
# print(lista_losowych_liczb[5:]) # Od 5 indeksu do końca
# print(lista_losowych_liczb[-3:]) # Od trzeciego ostatniego indeksu do końca

podlista = lista_losowych_liczb[0: 5] # Kopiowanie elementów z listy
print(podlista)

if 5 in podlista: # Sprawdzenie czy dany element jest w liście
    print("Numer 5 znajduje się w liście.")
else:
    print("Numer 5 nie jest w liście.")