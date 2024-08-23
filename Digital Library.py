import os
from datetime import datetime


def menu():
    print("Welcome to Digital Diary")
    print("What do you want to do? \n")
    print("1. Write a new update")
    print("2. Read diary updates")
    print("3. Exit")
    choice = input("Choose an option: ")
    return choice


def write_update():
    update = input("Write your update: ")
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")

    file = open("diary.txt", "a")
    file.write(timestamp)
    file.write("\n")
    file.write(update)
    file.write("\n\n")

    file.close()
    print("\n Saved Successfully! \n")


def read_updates():
    if os.path.exists("diary.txt"):
        file = open("diary.txt", "r")

        content = file.read()
        if content:
            print("\nYour Diary updates:")
            print(content)
        else:
            print("No updates found.")
    else:
        print("No updates found.")


def run_code():
    while True:
        choice = menu()
        if choice == "1":
            write_update()
        elif choice == "2":
            read_updates()
        elif choice == "3":
            print("Thankyou for using Digital Libray. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please choose between 1,2 or 3. \n")

run_code()