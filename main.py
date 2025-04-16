from stats import *

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    list = sorted_list(count_caracters(text))
    for item in list:
        if item["car"].isalpha():
            print(f"{item["car"]}: {item["count"]}")
    print ("============= END ===============")


main()