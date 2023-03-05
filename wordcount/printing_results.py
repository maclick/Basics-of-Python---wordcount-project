import sys
from os import sep as system_separator


def print_single_result(wordcount, input_name, output_file=""):
    if output_file != "":
        f = open("answers" + system_separator + output_file, "a")
        sys.stdout = f
    print("Printing results from ", input_name, ":")
    for word, count in wordcount.items():
        print(word, ": ", count, sep="")
    print('\n')
    if output_file != "":
        f.close()
        sys.stdout = sys.__stdout__
