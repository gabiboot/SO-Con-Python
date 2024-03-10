with open("distanciaPlanetas.txt") as file:
...     for line in file:
...         print(line.strip().upper())

 with open("PersonajesDragonball.txt") as file:
...     for line in file:
...         print(line.upper())

file = open("distanciaPlanetas.txt")
>>> lines = file.readlines()
>>> file.close()
>>> lines.sort()
>>> print(lines)