from os import sep as system_separator


def choose_valid_option(permitted_options):
    chosen_option = input()
    while chosen_option not in permitted_options:
        print("Please provide a number corresponding to a correct option")
        chosen_option = input()
    return chosen_option


def print_init_message():
    print("Welcome to the word count program, where you can count words from standard input or from files stored in"
          "\033[0;32m resources\033[0m directory")


def print_input_options():
    print("\nPlease specify which option do you want to use by typing the corresponding number:")
    print("\t1. Read from standard input")
    print("\t2. Read from files")
    print("Choose your option: ", end='')


def print_standard_input_info():
    print("\nNow just type the text for which you want to count words for "
          "(unfortunately only available option is to type them in a single line):")


def print_files_input_options():
    print("\nI will give you a few more options now:")
    print("\t1. Read text from all files in resources directory and sum the results")
    print("\t2. Read text from all files in resources directory and print the results for each file separately")
    print("\t3. Read text from specific files in resources directory and sum the results")
    print("\t4. Read text from specific files in resources directory and print the result for each file separately")
    print("Choose your option: ", end='')


def print_do_you_want_to_continue():
    print("\nDo you want to continue? (1 - yes, 2 - no)")
    print("Choose your option: ", end='')


def print_provide_filenames():
    print("\nPlease provide filenames separated by spaces (for example: file1.txt file2.txt): ", end='')


def read_output_file():
    return input("\033[0;32m Provide output file name (or leave empty for standard output)\033[0m \nIf the file exist "
                 "it will append the results at the end of this file\nThis file will be stored in the answers"
                 "directory\nFilename: ")


def print_results_stored_in_file(output_file):
    if output_file == "":
        print("Look above for the results")
    else:
        print("Results stored are in a file:", "\033[0;32m answers" + system_separator + output_file + "\033[0m")
