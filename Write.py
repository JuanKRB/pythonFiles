# Write line to file
exmp2 = "C:\\Users\\juanr\\PycharmProjects\\pythonFiles\\Example2.txt"
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")

# Read file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

print("/////")

with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

print("/////")

Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

# Write the strings in the list to text file

with open(exmp2, 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

#setting the mode to w overwrites all the existing data in the file.

print("/////")

# We can write to files without losing
# any of the existing data  by setting the mode argument to
# append: a

with open(exmp2, 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

print("/////")
"""
It's fairly ineffecient to open the file in a or w and 
then reopening it in **r** to read any lines. Luckily we 
can access the file in the following modes:
- r+: Reading and writing. Cannot truncate the file.
- w+: Writing and reading. Truncates the file.
- a+: Appending and Reading. Creates a new file, if none exists.
You dont have to dwell on the specifics of each mode for this lab. 
"""

with open(exmp2, 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())