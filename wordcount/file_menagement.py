from os import listdir


def find_all_files_in_resources():
    temp = listdir("resources")
    ans = []
    for file in temp:
        if file.endswith(".txt"):
            ans.append(file)
    return ans
