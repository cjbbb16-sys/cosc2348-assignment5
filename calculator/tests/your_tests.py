#!/usr/bin/env python3
from calculator_adapter import run


import subprocess

def test_addition():
    result = subprocess.run(["./calculator", "1", "+", "1"], capture_output=True, text=True)
    assert "2" in result.stdout

def test_multiplication():
    result = subprocess.run(["./calculator", "2", "+", "2"], capture_output=True, text=True)
    assert "4" in result.stdout


### ADD AT LEAST TWO TESTS HERE!


###

print("All tests passed!")
