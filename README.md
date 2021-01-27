# vcokltfre/Supress

## A simple utility to supress output

Usage:
```py
from supress import supressed

with supressed():
    print("This output is supressed!")

print("This output isn't!")
```

### This package exists as a result of certain libraries that force printing output when it's unwanted