# packages: collections of Python modules bundled together for reuse
# pypi.org: the official repository for sharing and downloading Python packages
# pip: Python’s package manager used to install and manage packages
# pip install cowsay: a command that downloads and installs the cowsay package
# cowsay: a Python package that prints text as ASCII art of a cow

import cowsay
import sys

if len(sys.argv) == 2:
    # this function only accepts one string so we use + for concatenation
    cowsay.cow("hello, " + sys.argv[1]) 
else:
    sys.exit 

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
