# vcokltfre/Supress

## A simple utility to supress output

Usage:
```py
from supress import supressed

with supressed():
    print("This output is supressed!")

print("This output isn't!")