def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    plain_text = lower_text(text)
    char_dictionary = get_chars(plain_text)
    print(char_dictionary)
    print(char_dictionary.sort())

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def lower_text(text):
    return text.lower()

def get_chars(text):
    counter = {}
    for chars in text:
        if chars in counter:
            counter[chars] += 1
        else:
            counter[chars] = 1
    return counter

def sort_dictionary(unsorted_dic):
    return unsorted_dic.sort()

main()