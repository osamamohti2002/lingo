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





