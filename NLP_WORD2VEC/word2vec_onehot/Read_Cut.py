import re

def read_the_file_as_string():
    filename = input("please input the filename of article")
    file = open(filename, 'r')
    try:
        strings = file.read()
    finally:
        file.close()
    return strings

def cut_the_strings_into_words(source):
    result = re.split(r'\W+', source)
    return result