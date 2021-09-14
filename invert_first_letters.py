def invert_first_letters(sentence: str) -> None:
    """Invert the two first letters of each words and print it"""
    words = sentence.split()
    for i in words:
        print(i[1::-1] + i[2::])
