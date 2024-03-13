

import csv
>>> f = open("chavocsv.txt")
>>> csv_f = csv.reader(f)
>>> for row in csv_f:
...     nombre, numero_de_casa, representacion = row
...     print("nombre {}, casa {}, papel {}".format(nombre,numero_de_casa, representacion))
...
nombre Nombre, casa Numero_de_Casa, papel Representacion
nombre El Chavo, casa 8, papel NiÃ±o
nombre Quico, casa 14, papel NiÃ±o
nombre La Chilindrina, casa 71, papel NiÃ±a
nombre Don RamÃ³n, casa 72, papel Adulto
nombre DoÃ±a Florinda, casa 14, papel Adulto
nombre Profesor Jirafales, casa 9, papel Adulto
nombre DoÃ±a Clotilde (La Bruja del 71), casa 14, papel Adulto
nombre SeÃ±or Barriga, casa 7, papel Adulto
nombre Ã‘oÃ±o, casa 71, papel NiÃ±o
nombre Godinez, casa 22, papel Adulto
>>> f.close()