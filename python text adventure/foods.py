foods = []
more_items = True

def pretty_print_unordered(ls):
    for item in ls:
        print ("* " + str(item))

def pretty_print_ordered(ls):
    for i, value in enumerate(ls,1):
        print(str(value) + ". " + str(i))


while more_items:
    INPUT = input("Enter something you like: ")
    if INPUT == "":
        more_items = False
    else:
        foods.append(INPUT)

pretty_print_unordered(foods)


