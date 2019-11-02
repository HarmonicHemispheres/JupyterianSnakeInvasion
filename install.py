"""
---------------------------- INSTALL ----------------------------
Use this script to install the required python packages. This is
a useful script for installing dependancies in environments like
binder.org

USE:
    > python install.py
"""

import os

commands = [
    "conda install numpy",
    "conda install pandas",
    "pip install matplotlib",
    "pip install ipywidgets",
    "conda install sklearn",
    "conda install graphviz",
    "pip install pydotplus",
    "conda install -c conda-forge ipyvolume",
    "conda install -c conda-forge ipysheet",
]

# execute commands
for cmd in commands:
    os.system(cmd)
