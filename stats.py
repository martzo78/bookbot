def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def count_words(text):
     return len(text.split())