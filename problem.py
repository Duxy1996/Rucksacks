
rucksack_size = 0
list_of_books = []

# set all parameters

books_count = input('How many books do you want to sell? ')
count = 0
while (count < books_count):
    wight = input('Weight of the book: ')
    prize = input('Cost of the book: ')
    book = (wight,prize)
    list_of_books.append(book);

print("list of books: " + list_of_books)
   