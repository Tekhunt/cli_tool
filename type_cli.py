import typer
import os


app = typer.Typer()


@app.command()
def project_folder(app: str, name: str):
    """Generate a basic FastAPI application structure."""
    typer.echo(f"Creating FastAPI application: ")

    # Create project directory
    os.makedirs(app)
    os.chdir(app)

    # Create app directory
    os.makedirs(name)
    os.chdir(name)

    # Create __init__.py file
    with open("__init__.py", "w") as f:
        pass

    # Create main.py file
    with open("main.py", "w") as f:
        f.write(
            """
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, FastAPI!"}
"""
        )

    # Create dependencies.py file
    with open("dependencies.py", "w") as f:
        pass

    # Create routers directory
    os.makedirs("routers")
    os.chdir("routers")

    # Create __init__.py file
    with open("__init__.py", "w") as f:
        pass

    # Create items.py file
    with open("items.py", "w") as f:
        pass

    # Create users.py file
    with open("users.py", "w") as f:
        pass

    os.chdir("..")  # Go back to the app directory

    # Create internal directory
    os.makedirs("internal")
    os.chdir("internal")

    # Create __init__.py file
    with open("__init__.py", "w") as f:
        pass

    # Create admin.py file
    with open("admin.py", "w") as f:
        pass

    typer.echo("FastAPI application generated successfully!")


if __name__ == "__main__":
    app()
