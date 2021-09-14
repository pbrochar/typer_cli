import typer
from sort_string import sort_string
from invert_first_letters import invert_first_letters
from define_words import define_words_in_sentence

app = typer.Typer(add_completion=False, help="Sort, invert letters or define words in a string")


@app.command("sort", help="Sort the words in the string.")
def sort(
        reverse: bool = typer.Option(False, "--desc", "-d", help="descending order"),
        insensitive: bool = typer.Option(False, "--insensitive", "-i", help="insensitive case sort"),
        sentence: str = typer.Argument(...),
) -> None:
    """Initializes the CLI 'sort' command and calls the sort_string function"""
    sort_string(reverse, insensitive, sentence)


@app.command("invert", help="Invert the first two letters of each word in the string.")
def invert_letter(sentence: str = typer.Argument(...)) -> None:
    """Initializes the CLI 'invert-letter' command and calls the invert_first_letters function"""
    invert_first_letters(sentence)


@app.command("define", help="Define, if possible, each word in the sentence.")
def define_words(sentence: str = typer.Argument(...)) -> None:
    """Initializes the CLI 'define-words' command and calls the define_words_in_sentence function"""
    define_words_in_sentence(sentence)


if __name__ == "__main__":
    app()
