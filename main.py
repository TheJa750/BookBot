def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    word_count = get_word_count(text)
    chars_dict = get_char_count(text)
    report_list = convert_dict(chars_dict)
    report_list.sort(reverse=True, key=report_sort)
    print_report(report_list, word_count, book_path)

def print_report(list, words, path):
    print(f"--- Begin report of {path} ---")
    print(f"There are {words} words found in the document.")
    letters = []
    counts = []
    for dict in list:
        for key in dict:
            if key == "letter":
                letters.append(dict[key])
            if key == "num":
                counts.append(dict[key])
    for i in range(0, len(letters)):
        print(f"The '{letters[i]}' character was found {counts[i]} times.")
        
    print("--- End of report ---")
    
def convert_dict(dict):
    new_list = []
    for key in dict:
        if key.isalpha():
            temp = {"letter": key, "num": dict[key]}
            new_list.append(temp)
    return new_list

def report_sort(dict):
    return dict["num"]

def get_book(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return(len(words))
        
def get_char_count(text):
    counts = {}
    words = text.lower().split()

    for word in words:
        letters = [*word]
        for letter in letters:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1    
    return counts

main()