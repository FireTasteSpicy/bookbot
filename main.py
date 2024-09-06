def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    # print(chars_dict)
    sorted_list = sorting_count(chars_dict)
    for obj in sorted_list:
        print(f"The '{obj['char']}' character was found {obj['num']} times")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def sorting_count(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char" : char, "num": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
