import typer
import json
from pathlib import Path
from contractguard.openapi import generate_openapi
from contractguard.comparator import compare_contracts
from contractguard.docs import show_contract_docs
app = typer.Typer(
    name="contractguard",
    help="[yellow]Now Pratham Detects [bold bright_magenta]breaking changes[/bold bright_magenta] in API Contracts | Please use command --docs for more information",
    rich_markup_mode="rich"
)

@app.command("docs")
def show_docs():
    """Show ContractGuard documentation."""

    show_contract_docs()

@app.command("init")
def init(app_path:str=typer.Option(...,"--app")):
    """Initialize ContractGuard in the current project."""
    try:
        typer.echo("Loading FastAPI application....")

        schema = generate_openapi(app_path)
        folder = Path('.contractguard')
        folder.mkdir(exist_ok=True)

        print(f"Scehama : {schema}")
        # schema["paths"]["path"]["description"]
        baseline = folder / "baseline.json"


        paths = schema.get("paths",{})

        protected_routes = []
        for path,methods in paths.items():
            for method,details in methods.items():
                if "protect" in details.get("description","").lower():
                    details["is_protected"]=True
                else:
                    details["is_protected"]=False

        with open(baseline,"w",encoding="utf-8") as file:
            json.dump(schema,file,indent=2)

        typer.echo("✓ FastAPI app loaded")
        typer.echo("✓ OpenAPI schema generated")
        typer.echo(f"✓ Baseline saved: {baseline}")

    except Exception as error:
        typer.echo(f"✗ Error: {error}", err=True)
        raise typer.Exit(code=1)


@app.command("say-hi")
def sayhi():
    """Say Hi as a test message"""
    typer.echo("Hello from contractguard")


@app.command("check")
def check(app_path:str = typer.Option(...,"--app",help="FastAPI application path . eg: main:app")):
    """Comparator logic : heart"""

    try:
        baseline_path = Path(".contractguard/baseline.json")

        #check if baseline is there: 
        if not baseline_path.exists():
            typer.echo("No baseline found. Please run `init` first")
            raise typer.Exit(code=1)

        protected_routes = []

        # else load the basline 
        with open(baseline_path,"r",encoding="utf-8") as file:
            old_contract = json.load(file)

        typer.echo("Loading the FastAPI application...")
        new_contract = generate_openapi(app_path)

        #Compare the paths
        changes = compare_contracts(old_contract,new_contract)

        typer.echo("Changes in the contracts :\n")

        if not changes:
            typer.echo(
                "No changes beem occurred | "
            )

        for change in changes:
            typer.echo(f"\nchange value : {change}")

            if change["severity"] == "breaking":
                icon = "🔴"
                label = 'BREAKING CHANGE'
            else:
                icon = "🟢"
                label = "SAFE CHANGE"

            method = change.get("method")

            if method:
                endpoint = (
                    f"{method} {change['path']}"
                )
            else:
                endpoint = change['path']

            typer.echo(
                f"{icon} {label}: "
                f"{endpoint}"
            )

    except Exception as error:
        typer.echo(
            f"✗ Failed to check API contract: {error}",
            err=True,
        )

        raise typer.Exit(code=1)


@app.command("update")
def update(
    app_path:str=typer.Option(
        ...,
        "--app",
        help="To update the baseline Eg.main:app"
    )
):

    """Updating the openapi.json"""

    try:
        typer.echo("Generating the current Current API contract...")

        openapi_schema = generate_openapi(app_path=app_path)
        print("Got the protected route info : ",openapi_schema[""])
        print(f"OPEN API SCHEMA : \n",openapi_schema)
        contractguard_path=Path('.contractguard')
        contractguard_path.mkdir(exist_ok=True)

        baseline_path = contractguard_path / "baseline.json"

        with open(baseline_path,"w",encoding="utf-8") as file:
            json.dump(openapi_schema,file,indent=2)

        typer.echo(f"✓ API baseline updated: {baseline_path}")

    except Exception as e:
        typer.echo(
            f"✗ Failed to update baseline: {e}",
            err=True,
        )
if __name__ == "__main__":
    app()