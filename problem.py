rucksack_size = 0
rucksack_books = []
books_count = 0
list_of_books = []
list_of_books_in_order = []
# set all parameters
rucksack_size = int(input('How many kilograms can support yout rucksack? '))
books_count = int(input('How many books do you want to sell? '))
count = 0
while (count < books_count):
    wight = int(input('Weight of the book '+ str(count) + ' : '))
    prize = int(input('Cost of the book: '))
    book = (wight,prize)
    list_of_books.append(book);
    count = count + 1;

print("list of books: " + str(list_of_books))

first = list_of_books[0]

for book in list_of_books:
    temperol_book = (book[0],book[1],book[1]/book[0])
    list_of_books_in_order.append(temperol_book)


list_of_books_in_order = sorted(list_of_books_in_order, key=lambda x: x[2])
list_of_books_in_order = list_of_books_in_order[::-1]
print(list_of_books_in_order)

wight = 0
count = 0
while ((wight < rucksack_size) & (count < len(list_of_books_in_order))):
    if(wight + list_of_books_in_order[count][0] <= rucksack_size):
        rucksack_books.append(list_of_books_in_order[count])
        wight = wight + list_of_books_in_order[count][0]
    count = count + 1


print(rucksack_books)






