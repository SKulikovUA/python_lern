#!env python

DELIM = "\t\t\t"

telephone_book = {}

choose = {"Q", "A", "U", "L", "D"}

def name_exists(name):
    return name in telephone_book

def append():
    while True:
        name = input("Name : ")
        if name_exists(name) :
            print(f"Name {name} already exists. Try another name.")
        else:
            number = input(f"{name} telephone number : ")
            telephone_book[name] = number
            break

def update():
    if len(telephone_book) == 0:
        print("Nothing to update")
        return
    while True:
        show()
        name = input("Name : ")
        if name_exists(name):
            number = input("New number : ")
            telephone_book[name] = number
            break
        else:
            print("Name doesn't present. Please try again")

def show():
    print(f"Name:{DELIM}Number:")
    for name, number in telephone_book.items():
        print(f"{name}{DELIM}{number}")

def delete():
    show()
    if len(telephone_book) == 0:
        print("Nothing to delete")
        return

    while True:
        name = input("Name for remove: ")
        if not name_exists(name):
            print(f"Name {name} not exists. Please try again")
            continue
        else:
            del telephone_book[name]
            break

while True:
    print("(A)ppend (U)pdate (L)ist (D)elete (Q)uit")
    inp = input("Your choose : ").strip().upper()
    if inp in choose:
        if inp == "Q":
            exit()
        elif inp == "A":
            append()
        elif inp == "U":
            update()
        elif inp == "L":
            show()
        elif inp == "D":
            delete()
    else:
        print("Bad input")