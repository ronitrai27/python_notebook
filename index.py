import sys
import numpy as np
# import sklearn as sk
print(sys.executable)

def func1(a:10, b:100):
    try:
        print("Inside func1")
        c = a/b
        return c
    except Exception as e:
        print(f"Error in func1: {e}")
        return None

func1(10, 0)
print(sys.version)

