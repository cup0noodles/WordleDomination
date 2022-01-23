"""
Wordle Domination
Matthew Wong
22 Jan 2022

listFilter

This script takes an input file with a list of words, pulls out only 5-letter
words without repeating characters and writes it to a new file.
"""


def read_input(file_name):
    """
    Reads input file, outputs as array
    :param file_name: (str) name of file containing words to be sorted
    :return word_array: (array) list of words from file
    """
    with open(file_name) as word_list:
        word_array = word_list.readline()
    return word_array


def filter_words(words, length, repeats):
    """
    :param words: (array)
    :param length: (int)
    :param repeats: (bool)
    :return word_array: (array)
    """
    

def main():

    print("test")
