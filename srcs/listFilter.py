"""
Wordle Domination
Matthew Wong
22 Jan 2022

This script takes an input file with a list of words, pulls out only 5-letter
words without repeating characters and writes it to a new file.
"""
import math


class Words:
    """
    Class for words, calculating score etc.
    """

    def __init__(self, word, pos_score, abs_score):
        self.word = word
        self.pos_score = pos_score
        self.abs_score = abs_score

    def return_letter(self, pos):
        return self.word[pos-1]


class LetterStats:
    """
    Class for letter statistics to build scores
    """

    def __init__(self, pos_abs, pos1, pos2, pos3, pos4, pos5):
        self.abs = pos_abs
        self.pos1 = pos1
        self.pos2 = pos2
        self.pos3 = pos3
        self.pos4 = pos4
        self.pos5 = pos5


def filter_blacklist():
    """

    :return:
    """


def filter_whitelist():
    """

    :return:
    """


def score_array():
    log_score = []
    for i in range(1, 27):
        log_val = int(-100*math.log(0.035*i, 10))
        log_score.append(log_val)
    return log_score


def create_score_dict(score_array):
    """
    1 is highest position
    :param score_array:
    """
    for i in range(1, 27):
        score_dict[i] = score_array[i-1]


def read_input(file_name, pop_newline = False):
    """
    Reads input file, outputs as array
    :param pop_newline: (bool)
    :param file_name: (str) name of file containing words to be sorted
    :return word_array: (array) list of words from file
    """
    word_array = []
    with open(file_name) as word_list:
        for line in word_list:
            if pop_newline is True:
                line_pop = line.replace("\n", "")
                word_array.append(line_pop)
            else:
                word_array.append(line)
    return word_array


def filter_length(words, length):
    """
    :param words: (array)
    :param length: (int)
    :return word_array: (array)
    """
    filtered = []
    for word in words:
        if len(word) == length + 1:
            filtered.append(word)
    return filtered


def letter_stats(words):
    """
    :param words:
    :return:
    """


if __name__ == '__main__':
    # words = read_input("dict.txt")
    # filtered = filter_length(words, 5)
    filtered = read_input("filtered.txt", True)
    # print(len(filtered))
    # scores = score_array()
    # print(scores)
    # score_dict = {}
    # create_score_dict(scores)
    # print(score_dict)

    # with open('filtered.txt', 'w') as f:
    #   for item in filtered:
    #        f.write("%s" % item)
