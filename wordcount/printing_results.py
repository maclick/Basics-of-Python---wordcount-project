def print_single_result(wordcount, input_name):
    print("\nPrinting results from ", input_name, ":")
    for word, count in wordcount.items():
        print(word, ": ", count, sep="")
