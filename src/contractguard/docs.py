import typer

def show_contract_docs():
    typer.echo("")
    typer.secho(
        "CONTRACTGUARD",
        fg=typer.colors.YELLOW,
        bold=True,
    )

    typer.echo(
        "\nContractGuard detects breaking changes "
        "in FastAPI API contracts."
    )

    typer.echo("\nCOMMANDS")
    typer.echo("  init     Create the initial API baseline")
    typer.echo("  check    Check the current API against the baseline")
    typer.echo("  update   Update the approved API baseline")
    typer.echo("  docs     Show ContractGuard documentation")

    typer.echo("\nWORKFLOW")
    typer.echo("  1. Initialize the baseline")
    typer.echo("  2. Modify your FastAPI API")
    typer.echo("  3. Run check")
    typer.echo("  4. Review the detected changes")
    typer.echo("  5. Run update when the changes are approved")

    typer.echo("\nPROTECTED ROUTES")
    typer.echo(
        '  If a route must be strictly protected, '
        'include the word "protected" in the route docstring.'
    )

    typer.echo("\nEXAMPLE")
    typer.echo(
        '  @app.get("/users", description="protected")'
    )
    typer.echo("\nEXAMPLES")
    typer.echo(
        "  contractguard init --app main:app"
    )
    typer.echo(
        "  contractguard check --app main:app"
    )
    typer.echo(
        "  contractguard update --app main:app"
    )

    typer.echo("")