
from listFilter import *

filtered = read_input("filtered.txt", True)
filtered_class = []
convert_array_class(filtered)

filtered_class = filter_grey(filtered_class, 'n')
filtered_class = filter_grey(filtered_class, 'e')
filtered_class = filter_green(filtered_class, 'a', 1)
filtered_class = filter_green(filtered_class, 'o', 3)
filtered_class = filter_yellow(filtered_class, 't', 2)

for word in filtered_class:
    print(word.word)

print(len(filtered_class))
score_dict = {}
