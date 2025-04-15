def get_book_text(path):
    with open(path) as f:
        output = f.read()
    return output

def main():
      print(get_book_text("books/frankenstein.txt"))

main()