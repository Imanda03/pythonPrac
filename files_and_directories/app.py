"""
Impoint the main class:
    from pathlib import Path        ----> Path should be capital


Two way for path:
1. absolute path:
    c:/program Files/windows

2. relative path

"""

from pathlib import Path

path = Path("carGames")
print(path.exists())            # to check the path

print(path.mkdir())             # to make a mew dir

print(path.rmdir())            #---> to remove the dir

for file in path.glob("*"):
    print(file)
