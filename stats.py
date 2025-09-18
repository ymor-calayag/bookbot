def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    word_list = text.split()
    return len(word_list)

def count_characters(text):
    char_list = []
    char_dict = {}
    word_list = text.split()

    # split words into chars, appending lowercased chars to a list
    for w in word_list:
        for c in w:
            char_list.append(c.lower())
    
    # counting characters, then updating a dict of character counts
    for char in char_list:
        if char not in char_dict:
            char_dict[char] = 1
        elif char in char_dict:
            char_dict[char] += 1
    return char_dict

'''
problem:

Add a new function to your stats.py file that takes the text from the book as a string, and returns the number of times each character, 
(including symbols and spaces), appears in the string.
Convert any character to lowercase using the .lower() method, we don't want duplicates.
Use a dictionary of String -> Integer. The returned dictionary should look something like this:
{'p': 6121, 'r': 20818, 'o': 25225, ...

Import and call the function in main.py, and capture the result in a new variable.
After printing the word count, print the dictionary of characters and their counts.
'''