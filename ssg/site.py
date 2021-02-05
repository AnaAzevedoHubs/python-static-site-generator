import pathlib

class Site:
    def __init__(self, source, dest) -> None:
        self._source = pathlib.Path(source)
        self._dest = pathlib.Path(dest)