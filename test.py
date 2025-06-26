import random


def grabbelen(ballenbak: list):
    if not ballenbak:
        return None, ballenbak
    bal = random.choice(ballenbak)
    nieuwe_bak = ballenbak[:]
    nieuwe_bak.remove(bal)
    return bal , nieuwe_bak



ballenbak = ['rood', 'groen', 12, 3,3 ,5,5,5]

print(grabbelen(ballenbak))

