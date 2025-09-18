# opens the file and reads it as string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

# passes the output of get_book_text() and splits and stores the separated words in a list 
# then returns the total count of words
def count_words(book_text):
    word_list = book_text.split()
    return len(word_list)

# passes the output of get_book_text() and returns a dict
# of character count. e.g. {'t': 29493, 'a': 25894}
def count_characters(book_text):
    char_list = []
    char_dict = {}
    word_list = book_text.split()

    # iterates each word, then iterates each char, appending lowercase chars to a list
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

# helper function that dictates that the sort should be by "num" key
def sort_on(items):
    return items["num"]

# passes the output of count_characters() then returns a new dictionary
# that is sorted based by character count descending
def sort_dict(dict):
    dict_list = []

    # loops through the dict
    for key, value in dict.items():
        # must create an empty dict each iteration so that it wont just update the current one
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = value
        dict_list.append(new_dict)
        
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
'''
counts = {"a": 3, "b": 5, " ": 2}

for key, value in counts.items():
    print(key, value)

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

vehicles = [
    {"name": "car", "num": 7},
    {"name": "plane", "num": 10},
    {"name": "boat", "num": 2}
]
vehicles.sort(reverse=True, key=sort_on)
print(vehicles)
# [{'name': 'plane', 'num': 10}, {'name': 'car', 'num': 7}, {'name': 'boat', 'num': 2}]
'''