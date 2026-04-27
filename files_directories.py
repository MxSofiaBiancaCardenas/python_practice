from pathlib import Path

# Absolute path
# c:\Program Files\Microsoft
# /usr/local/bin
# Relative path

# check if directory exists
# path = Path("ecommerce")
# print(path.exists())

# create new directory
# path1 = Path("emails")
# print(path1.mkdir())

# remove directory
# path1 = Path("emails")
# print(path1.rmdir())

path = Path()
# print(path.glob('*')) # searches everything 
print(path.glob("*.*")) # get the files in the current directory
print(path.glob("*.py")) # searches all the py files
print(path.glob("*.xls")) # searches all the xls files

# Iterating over files
for file in path.glob('*'):
    print(file)