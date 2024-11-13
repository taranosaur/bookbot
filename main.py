
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text_words = count_words(text)
    word_count = count_words_total(text)
    total_characters = count_characters(text)
    
    sorted_dict = sort_dict(total_characters)
    
    #print(sorted_dict[1][0])
    print(f"--- Begin report of {book_path} ---")
    print(f"{text_words} words found in the document.")
    print()
    for i in range(len(sorted_dict)):
        print(f"The '{sorted_dict[i][0]}' character was found {sorted_dict[i][1]} times.")
    print ("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
        

def count_words(book_text):
    split_text = book_text.split()
    return len(split_text)


def count_words_total(book_text):
    lower_case_text = book_text.lower()
    split_text = lower_case_text.split()
    word_dict = {}
    
    for word in split_text:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict

def count_characters(book_text):
    lower_case_text = book_text.lower()
    character_dict = {}
    
    for character in lower_case_text:
        if character.isalpha():
            if character in character_dict:
                character_dict[character] += 1
            else:
                character_dict[character] = 1

    return character_dict

def sort_dict(dict):
    sorted_items = sorted(dict.items(), key=lambda item: item[1], reverse=True) 
    return sorted_items



main()