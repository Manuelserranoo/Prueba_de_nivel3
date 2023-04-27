import random

# Generar el mazo de cartas
mazo = []
for palo in ["espada", "basto", "copa", "oro"]:
    for numero in range(1, 13+1):
        mazo.append((numero, palo))

random.shuffle(mazo)

pilas = {palo: [] for palo in ["espada", "basto", "copa", "oro"]}
for carta in mazo:
    pilas[carta[1]].append(carta)

# Ordenar la pila de espadas de manera creciente por número y palo
pilas["espada"] = sorted(pilas["espada"], key=lambda carta: (carta[0], carta[1]))


for palo, pila in pilas.items():
    print(f"{palo}: {pila}")





