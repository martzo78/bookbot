def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def count_words(text):
     return len(text.split())

def count_caracters(text):
    text = text.lower()
    caracters = {}
    for c in text:
        if c in caracters:
            caracters[c] += 1
        else:
            caracters[c] = 1
    return caracters

def sort_on_count(dict):
    return dict["count"]

def sorted_list(caracters):
    list = []
    for caracter in caracters:
        list.append({"car": caracter, "count": caracters[caracter]})
    list.sort(key=sort_on_count, reverse=True)
    return list



    

