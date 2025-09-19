import sys
from stats import get_book_text, count_words, count_characters, sort_dict

def main():
    # sys.argv represents the arguments passed to the script, access it by index.
    book_text = get_book_text(sys.argv[1])

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    print_char_report()
    print("============= END ===============")

def print_char_report():
    book_text = get_book_text(sys.argv[1])
    char_dict = count_characters(book_text)

    sorted_list = sort_dict(char_dict)
    for entry in sorted_list:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['num']}")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>") 
    sys.exit(1)
else:
    main()