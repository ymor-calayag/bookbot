def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    word_list = text.split()
    return len(word_list)

def main():
    text = get_book_text('books/frankenstein.txt')
    print(f"{count_words(text)} words found in the document")

main()