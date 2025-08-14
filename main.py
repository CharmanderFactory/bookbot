import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import word_count, char_count, sort_dic

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = get_book_text(sys.argv[1])
    num_words = word_count(file_contents)
    chars = char_count(file_contents)
    char_list = sort_dic(chars)
    sorted = []
    for sort_char in char_list:
        if sort_char["char"].isalpha():
            sorted.append(sort_char)

    print(f"============ BOOKBOT ============ \n Analyzing book found at {sys.argv[1]}... \n ----------- Word Count ---------- \n Found {num_words} total words \n --------- Character Count -------")
    for print_char in sorted:
        print(f"{print_char['char']}: {print_char['num']}")

     

main()