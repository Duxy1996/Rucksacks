
def best_combination(rucksack_size,list_of_books):
    if len(list_of_books) == 1:
        if rucksack_size >= list_of_books[0][0]:
            return list_of_books[0][1]
        else:
            return 0
    else:
        list_of_results = []
        for book in list_of_books:
            pass_list = []
            for booki in list_of_books:                
                if booki != book:
                    pass_list.append(booki) 
            add = 0
            diff = 0
            if  rucksack_size >= book[0]:
                add = book[1]
                diff = book[0]        

            list_of_results.append(add + best_combination((rucksack_size - diff),pass_list))        
        return max(list_of_results)


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

print(best_combination(rucksack_size,list_of_books))






