"""
File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
"""

def readWrite():
    """"a program that reads a file and writes a modified version to a new file"""
    try:
        filename = input('Enter the File you want to read from : ')
        modified = input('Enter the File you want to write into : ')
        filename = filename + '.txt'
        newfile = modified + '.txt'

        with open(filename, 'r', encoding='utf-8') as file:
            file_text = file.read()

        with open(newfile, 'w', encoding='utf-8') as f:
            f.write(f"\nHere i am writing a new message to the new file {file_text}")
            print(file_text)
    except FileNotFoundError:
        print('File does not exist')

    except IOError:
        print('unfortunately this File could not be read...try again')

#call the function
readWrite()
