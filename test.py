import random
from lingo import *

# def grabbelen(ballenbak: list):
#     if not ballenbak:
#         return None, ballenbak
#     bal = random.choice(ballenbak)
#     nieuwe_bak = ballenbak[:]
#     nieuwe_bak.remove(bal)
#     return bal , nieuwe_bak



# ballenbak = ['rood', 'groen', 12, 3,3 ,5,5,5]

# print(grabbelen(ballenbak))

woorden = ["appel", "fiets", "tafel"]
print("Gekozen woord:", kies_woord(woorden))  # Verwacht: willekeurig woord uit lijst


raad = "appel"
geheim = "appel"
print("Feedback 1:", controleer_poging(raad, geheim))  # ['groen', 'groen', 'groen', 'groen', 'groen']

raad2 = "applo"
geheim2 = "appel"
print("Feedback 2:", controleer_poging(raad2, geheim2))  # ['groen', 'groen', 'groen', 'groen', 'rood']


raad = "appel"
geheim = "appel"
ingevuld = ['a', '_', '_', '_', '_']
print("Nieuw ingevuld:", update_gevonden_letters(raad, geheim, ingevuld))  # ['a', 'p', 'p', 'e', 'l']



print("Team 1 ballenbak:", maak_ballenbak(1))  # Verwacht: even getallen + 3 'groen' + 3 'rood'
print("Team 2 ballenbak:", maak_ballenbak(2))  # Verwacht: oneven getallen + 3 'groen' + 3 'rood'



bak = [1, 2, 'groen', 'rood']
bal, nieuw = grabbelen(bak)
print("Getrokken bal:", bal)
print("Overgebleven bak:", nieuw)



# kaart = maak_bingokaart(1)
# print("Bingokaart team 1:")
# for rij in kaart:
#     print(rij)



# nummer = 16
# nieuwe_kaart = markeer_bingokaart(kaart, nummer)
# print("Kaart na markeren:")
# for rij in nieuwe_kaart:
#     print(rij)  # verwacht dat 7 vervangen is door 'X'


kaart = [
    ['X', 'X', 'X', 'X'],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print("Heeft bingo:", check_bingo(kaart))  # True, eerste rij is bingo

kaart2 = [
    [1, 2, 3, 4],
    [5, 'X', 7, 8],
    [9, 'X', 11, 12],
    [13, 'X', 15, 16]
]
print("Heeft bingo:", check_bingo(kaart2))  # False, nog geen kolombingo
