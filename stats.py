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
        char_counts[item] = char_count
    return char_counts
