from stats import get_book_text, count_words, count_characters, sort_dict

book_text = get_book_text('books/frankenstein.txt')
char_dict = count_characters(book_text)

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    print_char_report()
    print("============= END ===============")

def print_char_report():
    sorted_list = sort_dict(char_dict)
    for entry in sorted_list:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['num']}")

main()