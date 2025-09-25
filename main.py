

def get_book_text(book):
    with open(book) as filepath:
        book = filepath.read()
        return book
    
def main():
    contents = get_book_text("books/frankenstein.txt")
    print(contents)

    
main()
 