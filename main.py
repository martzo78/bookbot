def main():

    path = "books/frankenstein.txt"
    with open(path) as textfile:
        text = textfile.read()
    number_of_words = countwords(text)
    dict_of_letters = countletters(text)
    sorted_dict_of_letters = sort(dict_of_letters)
    
    print(f"--- Begin report of {path} ---")
    print(f"{number_of_words} words found in the document")
    print("")

    for letter in sorted_dict_of_letters:
        print(f"The '{letter}' was found {dict_of_letters[letter]} times")

    print("--- End report ---")

    return


def countwords(text):

    words = text.split()

    return len(words)

def countletters(text):

    dict = {}
    
    text = text.lower()
    words = text.split()

    for word in words:
        for letter in word:
            if letter in dict.keys():
                dict[letter] = dict[letter] + 1
            elif letter.isalpha():
                dict[letter] = 1
    
    return dict

def sort_on(dict):
    return dict['num']

def sort(dict):

    list = []
    for entry in dict:
        list.append({'letter': entry, 'num': dict[entry]})
    
    list.sort(reverse=True, key=sort_on)
    
    new_dict = {}
    for entry in list:
        new_dict[entry['letter']] = entry['num']

    return new_dict
    
main()