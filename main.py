def main():
    path = "books/frankenstein.txt"

    book_content = get_text(path)
    word_count = text_count(book_content)

    print("--- Begin report of books/frankenstein.txt --- \n")
    print(f"The word count of the book is: {word_count}\n\n")

    char_dict = char_count(book_content)
    char_dict_list = print_report(char_dict)
    
    for char_dict in char_dict_list:
        final_char = char_dict["char"]
        final_num = char_dict["num"]
        print(f"The {final_char} character was found {final_num} times\n")

def text_count(text):
    words_list = text.split()
    return len(words_list)

def get_text(text):
    with open(text) as f:
        return f.read()
    
def char_count(text):

    char_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1

    return char_dict

def print_report(dict):

    list_of_dicts = []
    
    for key in dict.keys():
        temp_dict = {}
        temp_dict["char"] = key
        temp_dict["num"] = dict[key]
        
        if temp_dict["char"].isalpha() == True:
            list_of_dicts.append(temp_dict)

    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def sort_on(dict):
    return dict["num"]

main()
