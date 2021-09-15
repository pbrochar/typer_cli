def invert_first_letters(sentence: str) -> None:
    """Invert the two first letters of each words and print it"""
    words = sentence.split()
    for word in words:
        print("".join([
            word[i:i + 2][::-1]
            for i in range(0, len(word), 2)
        ]))
