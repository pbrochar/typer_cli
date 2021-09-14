import typer
from sort_string import sort_string

app = typer.Typer()


@app.command()
def sort(
        reverse: bool = typer.Option(False, "--desc", "-d", help="descending order"),
        insensitive: bool = typer.Option(False, "--insensitive", "-i", help="insensitive case sort"),
        sentence: str = typer.Argument(...),
) -> None:
    """Initializes the CLI 'sort' command and calls the sort function"""
    sort_string(reverse, insensitive, sentence)


@app.command()
def rev_letter(sentence: str) -> None:
    typer.echo(f"Hello {sentence}")


if __name__ == "__main__":
    app()
