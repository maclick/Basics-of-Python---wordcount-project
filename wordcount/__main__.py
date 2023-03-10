import os
from counting_words import read_from_files
from counting_words import count_words_from_standard_input
from wordcount_options import choose_valid_option
from wordcount_options import print_input_options
from wordcount_options import print_standard_input_info
from wordcount_options import print_files_input_options
from wordcount_options import print_do_you_want_to_continue
from wordcount_options import print_init_message
from wordcount_options import read_output_file
from wordcount_options import print_results_stored_in_file


def get_answers_dir():
    return __file__.replace("wordcount" + os.sep + "__main__.py", "answers")


def main():
    path = get_answers_dir()
    if not os.path.exists(path):
        os.makedirs(path)

    print_init_message()
    running = "1"
    while running == "1":
        print_input_options()
        chosen_option = choose_valid_option(['1', '2'])

        if chosen_option == "1":
            output_file = read_output_file()
            print_standard_input_info()
            count_words_from_standard_input(output_file)
        else:
            print_files_input_options()
            chosen_option = choose_valid_option(['1', '2', '3', '4'])
            output_file = read_output_file()
            read_from_files(chosen_option, output_file)
        print_results_stored_in_file(output_file)
        print_do_you_want_to_continue()
        running = choose_valid_option(['1', '2'])


if __name__ == '__main__':
    main()
