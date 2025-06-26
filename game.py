import random
from lingo import *
from lingowords import words


woorden_lijst = [
    "appel", "stoel", "molen", "ijsje", "fiets", "vogel", "jurk", "klimt",
    "speer", "tafel", "krijt", "broek", "ijsje", "feest", "groen", "kleur"
]

MAX_POGINGEN =  5

def toon_feedback(raad, feedback):
    gekleurd = ''
    for letter, status, in zip(raad, feedback):
        if status == 'groen':
            gekleurd += f'\033[92m{letter}\033[0m'
        elif status == 'geel':
            gekleurd += f'\033[93m{letter}\033[0m'
        else:
            gekleurd += letter
    return gekleurd

def geef_bingokaart_string(kaart):
    regels = []
    for rij in kaart:
        regel = " ".join([f"\033[92mX\033[0m" if x == 'X' else str(x) for x in rij])
        regels.append(regel)
    return "\n".join(regels)


def speel_woordronde(woord, input_functie):
    pogingen = 0
    ingevuld = ['_' for _ in woord]
    ingevuld[0] = woord[0]
    poging_resultaten = []

    while pogingen < MAX_POGINGEN:
        huidige_invul = ''.join(ingevuld)
        raad = input_functie(pogingen + 1, huidige_invul).lower()

        if len(raad) != len(woord):
            poging_resultaten.append(("ongeldig", raad))
            print("Ongeldig woord, probeer opnieuw.")  # meteen tonen
            continue

        feedback = controleer_poging(raad, woord)
        print(toon_feedback(raad, feedback))  # ✅ feedback direct na invoer tonen
        poging_resultaten.append((raad, feedback))

        if raad == woord:
            return True, poging_resultaten

        ingevuld = update_gevonden_letters(raad, woord, ingevuld)
        pogingen += 1

    return False, poging_resultaten

print("Welkom bij Lingo!")
team = int(input("Welk team speelt? (1 of 2): "))
win_groen = 0
verlies_rood = 0
goed_geraden = 0
fout_op_rij = 0

ballenbak = maak_ballenbak(team)
bingokaart = maak_bingokaart(team)




while True:
    woord = kies_woord(woorden_lijst)
    print(f"\nHint: Het woord begint met een '{woord[0]}'")

    def invoer(poging_nr, ingevuld):
        return input(f"Poging {poging_nr}: {ingevuld}\nRaad het woord: ")

    goed, resultaten = speel_woordronde(woord, invoer)

    for entry in resultaten:
        if entry[0] == "ongeldig":
            print("Ongeldig woord, probeer opnieuw.")
        else:
            raad, feedback = entry
            print(toon_feedback(raad, feedback))

    if goed:
        print("Goed geraden!")
        goed_geraden += 1
        fout_op_rij = 0
        print("Grabbelen uit de ballenbak...")

        eerste, ballenbak = grabbelen(ballenbak)
        print(f"Eerste bal: {eerste}")
        if eerste == 'groen':
            win_groen += 1
        elif eerste == 'rood':
            verlies_rood += 1
        elif isinstance(eerste, int):
            bingokaart = markeer_bingokaart(bingokaart, eerste)

        if eerste != 'rood':
            tweede, ballenbak = grabbelen(ballenbak)
            print(f"Tweede bal: {tweede}")
            if tweede == 'groen':
                win_groen += 1
            elif tweede == 'rood':
                verlies_rood += 1
            elif isinstance(tweede, int):
                bingokaart = markeer_bingokaart(bingokaart, tweede)

        print("\nBingokaart:")
        print(geef_bingokaart_string(bingokaart))
    else:
        fout_op_rij += 1
        print(f"Helaas, het woord was: {woord}")

    # Win/verlies condities
    if win_groen >= 3:
        print("Team wint: 3 groene ballen!")
        break
    if verlies_rood >= 3:
        print("Team verliest: 3 rode ballen!")
        break
    if check_bingo(bingokaart):
        print("Team wint: BINGO!")
        break
    if goed_geraden >= 10:
        print("Team wint: 10 woorden geraden!")
        break
    if fout_op_rij >= 3:
        print("Team verliest: 3 fouten op rij!")
        break

    verder = input("Volgende ronde? (j/n): ").lower()
    if verder != 'j':
        break

print("Spel afgelopen. Bedankt voor het spelen!")