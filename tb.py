#!env python

import configparser
import json
import pickle
import os

DELIM = "\t\t\t"

telephone_book = {}

choose = {"Q", "A", "U", "L", "D", "S", "R"}

serialize_types = {"json", "pickle"}

DEFAULT_SERIALIZER = "json"
SERIALIZE_FILE_NAME = "telephone_book"


def read_serialize_type():
    result = ""
    parser = configparser.ConfigParser()
    parser.read("book.ini")
    try:
        result = parser.get("Serialize", "type").strip().lower()
    except(configparser.NoSectionError):
        result = DEFAULT_SERIALIZER
    if not result in serialize_types:
        print("Unknown parser type. Use json by default")
    
    return result


def save_to_json():
    with open(SERIALIZE_FILE_NAME + ".json", "w") as file:
        json.dump(telephone_book, file)


def load_from_json():
    if not os.path.exists(SERIALIZE_FILE_NAME + ".json"):
        print("Couldn't read file. File not exists")
        return

    with open(SERIALIZE_FILE_NAME + ".json", "r") as file:
        data = json.loads(file.read())


def save_to_pickle():
    pass


def load_from_pickle():
    pass

def name_exists(name):
    return name in telephone_book


def append():
    name = input("Name : ")
    if name_exists(name) :
        print(f"Name {name} already exists. Try another name.")
        return

    while True:
        number = input(f"{name} telephone number : ")
        if number:
            telephone_book[name] = number
            break


def update():
    if not telephone_book:
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

if __name__ == "__main__":
    print(type(telephone_book))
    stype = read_serialize_type()
    while True:
        print("(A)ppend (U)pdate (L)ist (D)elete (Q)uit (S)ave (R)ead")
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
            elif inp == "S":
                save_to_json()
            elif inp == "R":
                load_from_json()
        else:
            print("Bad input")