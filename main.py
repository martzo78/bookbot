def main():

    path = "books/frankenstein.txt"
    with open(path) as textfile:
        text = textfile.read()
    number_of_words = countwords(text)
    dict_of_letters = countletters(text)
    
    print(f"--- Begin report of {path} ---")
    print(f"{number_of_words} words found in the document")
    print("")

    print(dict_of_letters)

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

main()