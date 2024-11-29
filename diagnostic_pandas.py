# diagnostic_pandas.py
import sys
print("Python Executable:", sys.executable)
print("\nPython Path:")
for path in sys.path:
    print(path)

print("\nChecking Pandas:")
try:
    import pandas
    print("Pandas imported successfully")
    print("Pandas Location:", pandas.__file__)
except ImportError as e:
    print("Import Error:", e)

import sys
print(sys.executable)

import sys
print("Python Executable:", sys.executable)
print("Python Path:", sys.path)

