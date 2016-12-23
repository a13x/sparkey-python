import os

from cffi import FFI

with open(os.path.join(os.path.dirname(__file__), "sparkey.cdef")) as f:
    SPARKEY_CDEF = f.read()

SPARKEY_DEFAULT_INCLUDE = ["/usr/local/include/sparkey"]
SPARKEY_DEFAULT_LIB = ["/usr/local/lib"]
SPARKEY_SRC = """
#include "sparkey.h"
"""

ffi = FFI()
ffi.set_source("sparkey._sparkey", SPARKEY_SRC,
        include_dirs=SPARKEY_DEFAULT_INCLUDE,
        library_dirs=SPARKEY_DEFAULT_LIB,
        libraries=["sparkey"])
ffi.cdef(SPARKEY_CDEF)

if __name__ == "__main__":
    ffi.compile()
