def sort_string(reverse: bool, insensitive: bool, sentence: str) -> None:
    """Sort the sentence and print it"""
    words = sentence.split()
    print(sorted(words, reverse=reverse, key=str.casefold if insensitive is True else None))
