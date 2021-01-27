import sys
import contextlib
from io import BytesIO


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

__all__ = (supressed)
