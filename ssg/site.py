import pathlib

class Site:
    def __init__(self, source, dest) -> None:
        self.source = pathlib.Path(source)
        self.dest = pathlib.Path(dest)