import os

try:
    os.remove("../file_writer/my_first_file.txt")

except FileNotFoundError:
    print("File already deleted!")