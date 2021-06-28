#!/usr/bin/python

telephoneBook = dict()

choose = {"Q", "A", "U", "L", "D"}

def nameExists(_name):
    if telephoneBook.get(_name) != None:
        return True
    else:
        return False

def append():
    while True:
        name = input("Name : ")
        if nameExists(name) :
            print(f"Name {name} already exists. Try another name.")
        else:
            number = input(f"{name} telephone number : ")
            telephoneBook[name] = number
            break

def update():
    if len(telephoneBook) == 0:
        print("Nothing to update")
        return
    while True:
        list()
        name = input("Name : ")
        if nameExists(name):
            number = input("New number : ")
            telephoneBook[name] = number
            break
        else:
            print("Name doesn't present. Please try again")

def list():
    delim = "\t\t\t"
    print(f"Name:{delim}Number:")
    for name, number in telephoneBook.items():
        print(f"{name}{delim}{number}")

def delete():
    list()
    if len(telephoneBook) == 0:
        print("Nothing to delete")
        return

    while True:
        name = input("Name for remove: ")
        if not nameExists(name):
            print(f"Name {name} not exists. Please try again")
            continue
        else:
            telephoneBook.pop(name)
            break

while True:
    print("(A)ppend (U)pdate (L)ist (D)elete (Q)uit")
    inp = input("Your choose : ").capitalize()
    if inp in choose:
        if inp == "Q":
            exit()
        elif inp == "A":
            append()
        elif inp == "U":
            update()
        elif inp == "L":
            list()
        elif inp == "D":
            delete()
    else:
        print("Bad input")