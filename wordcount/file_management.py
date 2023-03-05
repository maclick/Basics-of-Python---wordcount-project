from os import listdir
from os import sep as system_separator


def find_all_files_in_resources():
    temp = listdir(__file__.replace("wordcount" + system_separator + "file_management.py", "") + "resources")
    ans = []
    for file in temp:
        if file.endswith(".txt") or file.endswith(".md") or file.endswith(".in") or file.endswith(".out"):
            ans.append(file)
    return ans
