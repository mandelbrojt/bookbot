import sys
from stats import count_words, count_characters, sort_char_count

def get_book_text(path):
    with open(path, "r") as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_filepath = f"./{sys.argv[1]}"
    book_text = get_book_text(book_filepath)
    book_words_count = count_words(book_text)
    counted_chars = count_characters(book_text)
    sorted_chars = sort_char_count(counted_chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath[2:]}...")
    print("----------- Word Count ----------")
    print(f"Found {book_words_count} total words")
    print("--------- Character Count -------")
    for dictionary in sorted_chars:
        if dictionary["char"].isalpha():
            print(f"{dictionary['char']}: {dictionary['num']}")
    print("============= END ===============")


main()
