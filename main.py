
# takes a filepath as input and return the contents of the file as a string
def get_book_text(book):
    with open(book) as filepath:
        book = filepath.read()
        return book

# accepts text from books as a str
def number_of_words(text):
    return len(text.split())


def main():
    contents = get_book_text("books/frankenstein.txt")
    num_words = number_of_words(text=contents)
    print(f"Found {num_words} total words")

    
main()


     