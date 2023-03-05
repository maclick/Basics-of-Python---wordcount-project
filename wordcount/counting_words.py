from printing_results import print_single_result
from file_menagement import find_all_files_in_resources
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


def count_words_in_single_file(filename):
    try:
        f = open(filename)
    except FileNotFoundError:
        print("File ", filename, " not found")
        return {}
    file_content = f.read()
    words = file_content.split()
    f.close()
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
    files = []
    for filename in filenames:
        files.append("resources" + system_separator + filename)

    wordcount_for_all_files = {}
    for file in files:
        wordcount_for_file = count_words_in_single_file(file)
        wordcount_for_all_files[file] = wordcount_for_file

    if not sum_all:
        for file, wordcount in wordcount_for_all_files.items():
            filename = file.split(system_separator)[-1]
            print_single_result(wordcount, filename)
    else:
        ans = {}
        for wordcount in wordcount_for_all_files.values():
            ans.update(wordcount)
        print_single_result(ans, "all files", output_file)
