def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    word_count = get_word_count(text)
    chars_dict = get_char_count(text)
    report_list = convert_dict(chars_dict)
    report_list.sort(reverse=True, key=report_sort)
    print(report_list)
    
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