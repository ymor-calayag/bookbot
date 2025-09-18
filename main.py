from stats import get_book_text, count_words, count_characters

def main():
    text = get_book_text('books/frankenstein.txt')
    print(f"{count_words(text)} words found in the document")
    print(count_characters(text))

main()