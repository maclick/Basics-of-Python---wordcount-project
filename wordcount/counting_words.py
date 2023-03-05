from printing_results import print_single_result
from file_management import find_all_files_in_resources
from wordcount_options import print_provide_filenames
from os import sep as system_separator


def count_words(words):
    ans = {}
    for word in words:
        if word not in ans:
            ans[word] = 1
        else:
            ans[word] += 1
    return ans


def count_words_from_standard_input(output_file):
    contents = input()
    words = contents.split()
    print_single_result(count_words(words), "standard input", output_file)


def get_root_dir():
    return __file__.replace("wordcount" + system_separator + "counting_words.py", "resources" + system_separator)


def count_words_in_single_file(filename):
    with open(get_root_dir() + filename) as f:
        file_content = f.read()
    words = file_content.split()
    return count_words(words)


def read_from_files(chosen_option, output_file):
    sum_all = False
    if chosen_option in ['1', '3']:
        sum_all = True
    if chosen_option in ['1', '2']:
        filenames = find_all_files_in_resources()
    else:
        print_provide_filenames()
        filenames = input().split()

    wordcount_for_all_files = {}
    for file in filenames:
        try:
            wordcount_for_file = count_words_in_single_file(file)
            wordcount_for_all_files[file] = wordcount_for_file
        except FileNotFoundError:
            print("\033[91mFile ", file, " not found!\033[0m\n", sep="")

    if not sum_all:
        for file, wordcount in wordcount_for_all_files.items():
            filename = file.split(system_separator)[-1]
            print_single_result(wordcount, filename, output_file)
    else:
        ans = {}
        for wordcount in wordcount_for_all_files.values():
            ans.update(wordcount)
        print_single_result(ans, "all files", output_file)
