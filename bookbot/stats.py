def count_words(book):
    words = book.split()
    return len(words)

def count_characters(book):
    collection = {}
    for letter in book.lower():
        if letter in collection:
            collection[letter] += 1
        else:
            collection[letter] = 1
    return collection

def sort(stuff):
    sorted_items = sorted(stuff.items(), key=lambda x: x[1], reverse=True)
    return sorted_items