def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    plain_text = lower_text(text)
    char_dictionary = get_chars(plain_text)
    free_dict = remove_symboles(char_dictionary)
    sorted_dict = sort_dictonary(free_dict)
    send_report(book_path, num_words, sorted_dict)

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

def remove_symboles(dicto):
    free_dicto = {}
    for key in dicto:
        if key.isalpha():
            free_dicto[key] = dicto[key]
    return free_dicto 

def sort_dictonary(dicto): 
    new_dicto = {}
    new_dicto = sorted(dicto.items(), key=lambda item: item[1], reverse=True)
    return new_dicto

def send_report(path, count, dict_list):
    print(f"---Begin report of {path} ---\n{count} words found in the document\n")
    for entry in dict_list:
        print(f"The '{entry[0]}' character was found {entry[1]} times")
    print("--- End report ---")  

main()