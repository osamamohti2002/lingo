import random

def kies_woord(woorden):
    return random.choice(woorden)


# Geeft feedback per letter: 'groen', 'geel', of 'grijs'.

def controleer_poging(raad, geheim):
    feedback = []
    for i in range(len(geheim)):
        if raad[i] == geheim[i]:
            feedback.append('groen')
        elif raad[i] in geheim:
            feedback.append('geel')
        else:
            feedback.append('rood')



def update_gevonden_letters(raad, geheim, ingevuld):
    # geeft nieuwe lijst terug met goed geraden letters ingevuld
    nieuw = ingevuld[:]
    for i in range(len(geheim)):
        if raad[i] == geheim[i]:
            nieuw[i] == geheim[i]
    return nieuw



def maak_ballenbak(team):
    nummers = list(range(1, 33))
    if team == 1:
        nummers = [n for n in nummers if n % 2 == 0]
    else:
        nummers = [n for n in nummers if n % 2 == 1]
    groene = ['groen'] * 3
    rode = ['rood'] * 3
    return nummers + groene + rode


def grabbelen(ballenbak: list):
    if not ballenbak:
        return None, ballenbak
    bal = random.choice(ballenbak)
    nieuwe_bak = ballenbak[:]
    nieuwe_bak.remove(bal)
    return bal , nieuwe_bak



def maak_bingokaart(team):
    nummers = list(range(1, 33))
    nummers = [n for n in nummers if (n % 2 == 0 if team == 1 else n % 2 == 1)]
    random.shuffle(nummers)
    kaart = []
    for i in range(4):
        rij = nummers[i * 4 : (i + 1) * 4]
        kaart.append(rij)
    return kaart


def markeer_bingokaart(kaart, nummer):
    nieuwe_kaart = []
    for rij in kaart:
        nieuwe_rij = ['X' if vak == nummer else vak for vak in rij]
        nieuwe_kaart.append(nieuwe_rij)
    return nieuwe_kaart



def check_bingo(kaart: list[list]) -> bool:
    for i in range(4):
        if all(x == 'X' for x in kaart[i]) or all(kaart[j][i] == 'X' for j in range(4)):
            return True
    if all(kaart[i][i] == 'X' for i in range(4)) or all(kaart[i][3 - i] == 'X' for i in range(4)):
        return True
    return False