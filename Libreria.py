# import funzioni libreria
from libro import AggiungiLibro, PrestitoLibro, RiportaLibro, DisponibilitaLibro, LibriDisponibili, LibriInPrestito
import time
import os

Libreria = []
Prestiti = []
print("Benvenuto in Libreria.")
inputFlag = False
exitFlag = False
while not exitFlag:
    scelta = input("Cosa vuoi fare?\n0)Esci dalla Libreria\n1)Dona un libro alla Libreria\n2)Prendi in prestito un libro\n3)Riporta un libro in prestito\n4)Ricerca la disponibilità di un libro\n5)Visualizza i libri disponibili in libreria\n6)Visualizza i libri in prestito\n")
    try:
        s = int(scelta)
    except ValueError:
        s = scelta.strip().lower()
    if s == 0 or s == "exit" or s == "esci" or s == "uscita":
        exitFlag = True
        break
    elif s == 1 or s == "aggiungi":
        AggiungiLibro(Libreria, Prestiti)
    elif s == 2 or s == "prestito":
        PrestitoLibro(Libreria, Prestiti)
    elif s == 3 or s == "riporta":
        RiportaLibro(Libreria, Prestiti)
    elif s == 4 or s == "ricerca disponibilita" or s == "ricerca disponibilità":
        DisponibilitaLibro(Libreria, Prestiti)
    elif s == 5 or s == "disponibili":
        LibriDisponibili(Libreria)
    elif s == 6 or s == "in prestito":
        LibriInPrestito(Prestiti)
    else:
        print("Non puoi farloooooooooooo!!!!!!!!!!")
y = 600
for i in range(0, y+1):
    os.system('clear')
    if (y / 60 >= 1):
        print(f"Chiusura del programma in {int(y/60)} min e {y % 60} sec...")
    else:
        print(f"Chiusura del programma in {y % 60} sec...")
    y -= 1
    time.sleep(1)
print("Programma chiuso.")
