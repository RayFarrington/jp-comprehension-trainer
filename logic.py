from random import randint
from convert_numbers_to_japanese import Convert, ConvertKanji

def generate_number():
    return randint(0, 1000000)

def get_message():
    num = randint(0, 1000000)
    hiragana = Convert(num, "hiragana")
    return hiragana
