from random import randint
from convert_numbers_to_japanese import Convert, ConvertKanji

def generate_number():
    return randint(0, 1000000)

def get_message(opt) -> str:
    if (opt is "audio"):
        return "not yet implimented"
    elif opt != "hiragana" and opt != "kanji":
        return "Error: invalid option in get_message"
    num = randint(0, 1000000)
    str = Convert(num, opt)
    return str
