

def find_duck(animals_row):
    duck = '🦆'
    counter = 0
    for animal in animals_row:
        if animal != ' ':
            counter = counter + 1
        if animal == duck:
            return counter
    return -1     