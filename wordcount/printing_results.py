import sys
from os import sep as system_separator


def print_results(input_name, wordcount):
    print("Printing results from", input_name, ":")
    for word, count in wordcount.items():
        print(word, ": ", count, sep="")
    print('\n')


def get_answers_dir():
    return __file__.replace("wordcount" + system_separator + "printing_results.py", "answers" + system_separator)


def print_single_result(wordcount, input_name, output_file=""):
    if output_file != "":
        with open(get_answers_dir() + output_file, "a") as f:
            sys.stdout = f
            print_results(input_name, wordcount)
            sys.stdout = sys.__stdout__
    else:
        print_results(input_name, wordcount)
