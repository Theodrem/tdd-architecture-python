# coding: utf-8
import typer
from ns_architecture.management_tests.task import create_test

app = typer.Typer()


@app.command()
def cmd_create_test(path_config: str):
    create_test(path_config)


@app.command()
def my_command2():
    typer.echo("Exécuter ma commande 2")


if __name__ == "__main__":
    app()
