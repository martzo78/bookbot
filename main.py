def main():
    path = "books/frankenstein.txt"
    with open(path) as textfile:
        text = textfile.read()
    number_of_words = countwords(text)
    print (f"Der Text besteht aus {number_of_words} Wörtern.")

def countwords(text):
    words = text.split()
    return len(words)

main()