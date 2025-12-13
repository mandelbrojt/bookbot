def count_words(book_text):
    return len(book_text.split())


def count_characters(book_text):
    unique_chars = set(book_text.lower())
    char_counts = {}
    
    for item in unique_chars:
        count = 0
        for char in book_text.lower():
            if char == item:
                count += 1
        char_counts[item] = count
    return char_counts


def sort_on(items):
    return items["num"]


def sort_char_count(char_dicts):
    list_of_chars = []
    for key, value in char_dicts.items():
        list_of_chars.append({"char": key, "num": value})
    list_of_chars.sort(reverse=True, key=sort_on)
    return list_of_chars

