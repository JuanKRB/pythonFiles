

"""from pyodide.http import pyfetch

import pandas as pd

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"
filename = "example1.txt"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(url, filename)

print("done")"""
""""
import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"
filename = "example1.txt"

response = requests.get(url)
if response.status_code == 200:
    with open(filename, "wb") as f:
        f.write(response.content)
        
print("done")"""

""""
# \\ para que lo detecte como slash
example1 = "C:\\Users\\juanr\\PycharmProjects\\pythonFiles\\example1.txt"
file1 = open(example1, "r")

print("El nombre es: ", file1.name)
print("El mode es: ", file1.mode)

print("////////")

FileContent = file1.read()

print(FileContent)
print(type(FileContent))

# This frees up resources and ensures consistency
# across different python versions.
file1.close()"""

example1 = "C:\\Users\\juanr\\PycharmProjects\\pythonFiles\\example1.txt"

# Using the with statement is better practice, it
# automatically closes the file even if the code
# encounters an exception. The code will run everything
# in the indent block then close the file object.

with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

# Verify if the file is closed
print(file1.closed)

# It reads the first 4 characters
with open(example1, "r") as file1:
    print(file1.read(4))

print("//////")

with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

print("//////")

with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))

print("//////")

with open(example1, "r") as file1:
    print("first line: " + file1.readline())

print("//////")

with open("example1.txt", "r") as file1:
    print(file1.readline(20))  # Lee hasta 20 caracteres o hasta el final de la línea, lo que ocurra primero
    print(file1.tell())  # Muestra la posición del cursor después de leer la línea
    print(file1.read(25))  # Lee 25 caracteres desde la posición actual
    print(file1.tell())  # Muestra la nueva posición del cursor

print("//////")

with open(example1,"r") as file1:
        for index,line in enumerate(file1):
            print("Iteration", str(index), ": ", line)

print("//////")

# Read all lines and save as a list

with open(example1, "r") as file1:
    FileasList = file1.readlines()

print(FileasList)
print(FileasList[0])
print(FileasList[1])
print(FileasList[2])


