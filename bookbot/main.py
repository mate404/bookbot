import sys

from stats import count_words
from stats import count_characters
from stats import sort

def get_book_text():
    with open(sys.argv[0], encoding="utf-8") as f:
        content = f.read()
    return content




def main():
    char_count = count_characters(get_book_text())
    sorted_chars = sort(char_count)
    print(sorted_chars)
    print("Usage: python3 main.py books/frankenstein.txt")
    sys.exit(1)
main()