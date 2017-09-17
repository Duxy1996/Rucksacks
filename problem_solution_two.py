rucksack_size = 0
rucksack_books = []
books_count = 0
list_of_books = []
list_of_books_in_order = []

amount_of_money_posible = 0
kilogrms_of_books = 0
# set all parameters
rucksack_size = int(input('How many kilograms can support your rucksack? '))
books_count = int(input('How many books do you want to sell? '))
count = 0
while (count < books_count):
    wight = int(input('Weight of the book '+ str(count) + ' : '))
    kilogrms_of_books = kilogrms_of_books + wight
    prize = int(input('Cost of the book: '))
    amount_of_money_posible = amount_of_money_posible + prize
    book = (wight,prize)
    list_of_books.append(book);
    count = count + 1;

print("List of books: " + str(list_of_books))

first = list_of_books[0]

for book in list_of_books:
    temperol_book = (book[0],book[1],book[1]/(rucksack_size - book[0] + 1))
    list_of_books_in_order.append(temperol_book)

print(str(kilogrms_of_books)+' kgms of books')
print(str(amount_of_money_posible)+' money of books')

list_of_books_in_order = sorted(list_of_books_in_order, key=lambda x: x[2])
list_of_books_in_order = list_of_books_in_order[::-1]

winned_money = 0
wight = 0
count = 0
while ((wight < rucksack_size) & (count < len(list_of_books_in_order))):
    if(wight + list_of_books_in_order[count][0] <= rucksack_size):
        rucksack_books.append(list_of_books_in_order[count])
        wight = wight + list_of_books_in_order[count][0]
        winned_money = winned_money + list_of_books_in_order[count][1]
    count = count + 1

print('In the rucksack there are/is these/this books:')
print(rucksack_books)
print('You have won all this money:')
print(winned_money)





