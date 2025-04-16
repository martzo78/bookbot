from stats import *
import sys

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return
    
    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    list = sorted_list(count_caracters(text))
    for item in list:
        if item["car"].isalpha():
            print(f"{item["car"]}: {item["count"]}")
    print ("============= END ===============")


main()