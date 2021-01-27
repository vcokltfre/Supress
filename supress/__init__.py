import sys


class supressed:
    def __init__(self):
        self.old_out = sys.stdout

    def __enter__(self):
        sys.stdout = self
        return self

    def __exit__(self, *args):
        sys.stdout = self.old_out

    def write(self, _):
        pass

    def flush(self):
        pass


__all__ = (supressed)
