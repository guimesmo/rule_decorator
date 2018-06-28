import os

from decorators.rules import run_all
from importlib import import_module


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for f in os.listdir(os.path.join(dir_path, "rules")):
        module_name = f.split(".")[0]
        import_module(".".join(["rules", module_name]))
    run_all("Lorem Ipsum")


if __name__ == '__main__':
    main()
