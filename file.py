# Open the file in read ('r') mode
file = open('file.txt', 'r')


# With automatically closes the file when operations
# within the indented block are completed.
# Open the file using 'with' in read ('r') mode
with open('file.txt', 'r') as file:
    file_stuff = file.read()
    print(file_stuff)

    line1 = file.readline()  # Reads the first line
    line2 = file.readline()  # Reads the second line

    if 'important' in line2:
        print('This line is important!')

    while True:
        line = file.readline()
        if not line:
            break  # Stop when there are no more lines to read
        print(line)

    file.seek(10)  # Move to the 11th byte (0-based index)

    characters = file.read(5)  # Read the next 5 characters

    print(characters)

    file.close()

