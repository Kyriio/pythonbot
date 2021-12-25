def roman_to_int(num: str) -> int:
    nombre_romain = {
        'I': 1,
        'II': 2,
        'III':3,
        'IV':4,
        'V':5,
    }
    return nombre_romain[num]