import sys


class supressed:
    def __init__(self):
        self.old_out = sys.stdout
        self.old_err = sys.stderr

    def __enter__(self):
        sys.stdout = self
        sys.stderr = self
        return self

    def __exit__(self, *args):
        sys.stdout = self.old_out
        sys.stderr = self.old_err

    def write(self, _):
        pass

    def flush(self):
        pass

class supressed_out:
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

class supressed_err:
    def __init__(self):
        self.old_err = sys.stderr

    def __enter__(self):
        sys.stderr = self
        return self

    def __exit__(self, *args):
        sys.stderr = self.old_err

    def write(self, _):
        pass

    def flush(self):
        pass

__all__ = (supressed, supressed_out, supressed_err)
