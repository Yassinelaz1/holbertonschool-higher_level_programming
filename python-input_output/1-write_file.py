#!/usr/bin/python3
"""
module documentation
"""

def write_file(filename="", text=""):
    """
    function documentation
    """
    with open(filename, encoding="utf-8") as f:
        return f.write(text)
