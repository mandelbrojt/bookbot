def get_book_text(path):
    with open(path, "r") as f:
        return f.read()


def count_words(book_text):
    words_list = book_text.split()
    return len(words_list)


def main():
    book_text = get_book_text("./books/frankenstein.txt")
    book_words_count = count_words(book_text)
    print(f"Found {book_words_count} total words")


main()
