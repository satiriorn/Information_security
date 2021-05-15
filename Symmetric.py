ALPHA ='абвгдеєжзиіїйклмнопрстуфхцчшщьюя'

def encode(text, step):
    return text.translate(str.maketrans(ALPHA, ALPHA[step:] + ALPHA[:step]))


def decode(text, step):
    return text.translate(str.maketrans(ALPHA[step:] + ALPHA[:step], ALPHA))
a= encode("Практична робота 5", 4)
print(encode("Практична робота 5", 4))
print(decode(a, 4))