
def print_report(book_path,book_file):
    words_num = count_words(book_file)
    character_count  = count_characters(book_file)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_num} word found in the document")


    for x in sorted(character_count.items(),key=lambda item: item[1],reverse=True):
        if x[0].isalpha():
            print(f"The '{x[0]}' character was found {x[1]} times")
        else:
            pass
    
        
    print("--- End report ---")

def count_words(book_file):
    words = book_file.split()
    return len(words)
        

def count_characters (text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    
    return chars



def open_book(book_path):
    with open(book_path) as b:
        return b.read()



def main():
    book_path = "books/frankstein.txt"
    book_file = open_book(book_path)

    
    print_report(book_path,book_file)
    
    



main()