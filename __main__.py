import sys, os, importlib
from flask.cli import shell_command
from fkart.app import app

if __name__ == '__main__':
    os.environ["PYTHONPATH"] = os.getcwd()
    os.environ["FLASK_APP"] = "fkart/app.py"
    try:
        ARG = sys.argv.pop(1)
    except IndexError:
        ARG = ""
    if ARG == "":
        app.run(host="0.0.0.0")
    elif ARG == 'database':
        with app.app_context():
            pass
    elif ARG == "shell":
        shell_command()