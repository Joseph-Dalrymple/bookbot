
# takes a filepath as input and return the contents of the file as a string
def get_book_text(book):
    with open(book) as filepath:
        book = filepath.read()
        return book

from stats import number_of_words


def main():
    contents = get_book_text("books/frankenstein.txt")
    num_words = number_of_words(text=contents)
    print(f"Found {num_words} total words")

    
main()


     