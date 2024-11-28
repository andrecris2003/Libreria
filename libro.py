"""
def AggiungiLibro(Libreria):
    libro=ImportaLibro()
    Libreria.append(libro)
    return Libreria


def ImportaLibro():
    libro={"nome":input("Inserisci il nome del libro\n"),
           "autore":input("Inserisci il nome dell'utore del libro\n"),
           "genere":input("Inserisci il genere del Libro\n"),
           "inizioPrestito":{"giorno","mese","anno"},
           "finePrestito":{"giorno","mese","anno"}}
    return libro
"""
def AggiungiLibro(Libreria,Prestiti):
    libro=input("Inserisci il nome del libro che vuoi aggiungere alla libreria\n").strip().lower()
    if (libro in Libreria) or (libro in Prestiti):
        print("Libro gia esistente")
    else:
        Libreria.append(libro)

def isEmpty(Libreria):
    if len(Libreria)<=0:
        return True
    else:
        return False
"""
def PrestitoLibro(Libreria,Prestiti):
    if not isEmpty(Libreria):
        ricerca=input("Che libro vuoi prendere in prestito?\n")
        if ricerca in Libreria(get("nome")):
            #libro = Libreria[index]
            Prestiti.append(Libreria[Libreria.index(ricerca)])
        return Libreria,Prestiti
    else:
        print("Nessun libro disponibile")
    return Libreria,Prestiti
"""
def PrestitoLibro(Libreria,Prestiti):
    if not isEmpty(Libreria):
        ricerca=input("Che libro vuoi prendere in prestito?\n")
        if ricerca in Libreria:
            Prestiti.append(ricerca)
            Libreria.remove(ricerca)
            print(f"Hai preso in prestito {ricerca}")
        else:
            print("Libro non esistente")
    else:
        print("Nessun libro disponibile")

def RiportaLibro(Libreria,Prestiti):
    if not isEmpty(Prestiti):
        ricerca=input("Che libro vuoi restituire?\n")
        if ricerca in Prestiti:
            Libreria.append(ricerca)
            Prestiti.remove(ricerca)
            print(f"Hai restituito {ricerca}")
        else:
            print("Libro non esistente")
    else:
        print("Nessun libro in prestito")
    return

def DisponibilitaLibro(Libreria,Prestiti):
    if (not isEmpty(Libreria)) and (not isEmpty(Prestiti)):
        ricerca=input("Che libro vuoi cercare?\n")
        if ricerca in Libreria:
            print("Il libro che stai cercando è disponibile")
        elif ricerca in Prestiti:
            print("Il libro che stai cercando è in prestito")
        else:
            print("Libro non esistente")
    else:
        print("Nessun libro nella Libreria")
    return

def LibriDisponibili(Libreria):
    if not isEmpty(Libreria):
        print("Liri disponibili in Libreria")
        print("-----------------------------------------------")
        for i in Libreria:
            print(f"{i} ")
        print("-----------------------------------------------")
    else:
        print("Nessun libro nella Libreria")
    return

def LibriInPrestito(Prestiti):
    if not isEmpty(Prestiti):
        print("Liri disponibili in Libreria")
        print("-----------------------------------------------")
        for i in Prestiti:
            print(f"{i} ")
        print("-----------------------------------------------")
    else:
        print("Nessun libro in prestito")
    return