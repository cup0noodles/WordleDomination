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

    def __init__(self, word, pos_score=0, abs_score=0):
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


def convert_array_class(word_array):
    """

    :param word_array:
    """
    for word in word_array:
        filtered_class.append(Words(word))


def filter_blacklist(word_class, letter, position):
    filtered_word_class = []
    for i in word_class:
        letter_check = i.return_letter(position)
        if letter_check != letter:
            filtered_word_class.append(i)
    return filtered_word_class


def filter_global_blacklist(word_class, letter):
    filtered_word_class = []
    for i in word_class:
        for j in range(1, 6):
            letter_check = i.return_letter(j)
            if letter_check == letter:
                break
            elif j == 5:
                filtered_word_class.append(i)
            else:
                continue

    return filtered_word_class


def filter_whitelist(word_class, letter, position):
    """

    :return:
    """
    filtered_word_class = []
    for i in word_class:
        letter_check = i.return_letter(position)
        if letter_check == letter:
            filtered_word_class.append(i)
    return filtered_word_class


def filter_global_whitelist(word_class, letter):
    filtered_word_class = []
    for i in word_class:
        for j in range(1, 6):
            letter_check = i.return_letter(j)
            if letter_check == letter:
                filtered_word_class.append(i)
                break
            else:
                continue

    return filtered_word_class


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
    filtered_class = []
    convert_array_class(filtered)
    """
    # Solution for 1/24 - 3 tries
    # From Guess 1 "atone"
    filtered_class = filter_global_whitelist(filtered_class, 'a')
    filtered_class = filter_global_blacklist(filtered_class, 't')
    filtered_class = filter_global_blacklist(filtered_class, 'e')
    filtered_class = filter_global_blacklist(filtered_class, 'o')
    filtered_class = filter_global_blacklist(filtered_class, 'n')
    filtered_class = filter_blacklist(filtered_class, 'a', 1)
    
    # From Guess 2 "scorn"
    filtered_class = filter_global_blacklist(filtered_class, 's')
    filtered_class = filter_global_blacklist(filtered_class, 'c')
    filtered_class = filter_global_blacklist(filtered_class, 'r')
    filtered_class = filter_blacklist(filtered_class, 'n', 5)
    filtered_class = filter_global_whitelist(filtered_class, 'n')
    """

    """
    Solution for 1/25 - 4 tries
    filtered_class = filter_global_whitelist(filtered_class, 'a')
    filtered_class = filter_global_whitelist(filtered_class, 's')
    filtered_class = filter_global_blacklist(filtered_class, 't')
    filtered_class = filter_global_blacklist(filtered_class, 'o')
    filtered_class = filter_global_blacklist(filtered_class, 'n')
    filtered_class = filter_global_blacklist(filtered_class, 'e')
    filtered_class = filter_blacklist(filtered_class, 'a', 1)
    filtered_class = filter_blacklist(filtered_class, 'a', 2)
    filtered_class = filter_blacklist(filtered_class, 's', 3)
    filtered_class = filter_global_blacklist(filtered_class, 'd')
    filtered_class = filter_global_blacklist(filtered_class, 'c')
    filtered_class = filter_global_blacklist(filtered_class, 'h')
    filtered_class = filter_global_blacklist(filtered_class, 'i')
    filtered_class = filter_whitelist(filtered_class, 's', 1)
    filtered_class = filter_whitelist(filtered_class, 'r', 5)
    filtered_class = filter_whitelist(filtered_class, 'a', 4)
    filtered_class = filter_global_whitelist(filtered_class, 'u')
    filtered_class = filter_blacklist(filtered_class, 'u', 4)
    """

    """
    Guess for 1/26
    
    # Atone
    filtered_class = filter_global_whitelist(filtered_class, 'a')
    filtered_class = filter_global_blacklist(filtered_class, 't')
    filtered_class = filter_global_blacklist(filtered_class, 'e')
    filtered_class = filter_global_blacklist(filtered_class, 'o')
    filtered_class = filter_global_blacklist(filtered_class, 'n')
    filtered_class = filter_blacklist(filtered_class, 'a', 1)
    # Basil
    filtered_class = filter_global_blacklist(filtered_class, 'b')
    filtered_class = filter_global_blacklist(filtered_class, 's')
    filtered_class = filter_global_blacklist(filtered_class, 'i')
    filtered_class = filter_global_blacklist(filtered_class, 'l')
    filtered_class = filter_blacklist(filtered_class, 'a', 2)
    # Fraud
    filtered_class = filter_global_blacklist(filtered_class, 'f')
    filtered_class = filter_global_blacklist(filtered_class, 'r')
    filtered_class = filter_global_blacklist(filtered_class, 'u')
    filtered_class = filter_global_blacklist(filtered_class, 'd')
    filtered_class = filter_whitelist(filtered_class, 'a', 3)
    """
    """
    Guess for 1/27
    
    # Atone
    filtered_class = filter_global_blacklist(filtered_class, 'a')
    filtered_class = filter_global_whitelist(filtered_class, 't')
    filtered_class = filter_global_whitelist(filtered_class, 'o')
    filtered_class = filter_whitelist(filtered_class, 'n', 4)
    filtered_class = filter_global_blacklist(filtered_class, 'e')
    filtered_class = filter_blacklist(filtered_class, 't', 2)
    filtered_class = filter_blacklist(filtered_class, 'o', 3)
    """
    for word in filtered_class:
        print(word.word)

    print(len(filtered_class))
    # scores = score_array()
    # print(scores)
    score_dict = {}
    # create_score_dict(scores)
    # print(score_dict)

    # with open('filtered.txt', 'w') as f:
    #   for item in filtered:
    #        f.write("%s" % item)
