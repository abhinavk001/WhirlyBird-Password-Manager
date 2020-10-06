# This is a password manager developed by Abhinav.
# The password stored is encrypted.
# It's using symmetric encryption, using a library built on top of AES algorithm.
# There are some lines which needs to be uncommented while being executed for the first time. Don't forget to comment
# them back after first execution.
from cryptography.fernet import Fernet
import tkinter as tk
import tkinter.simpledialog
from tkinter import messagebox


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("key.key", "rb").read()


def encrypt_file(filename, key):
    f = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)


def add():
    i = 0
    acc_name = input("Enter account name ")
    f1 = open("acc.txt", "a")
    f1.write(f"{acc_name}\n")
    f1.close()

    f1 = open("acc.txt", "r")
    for a in f1:
        i += 1

    pwd = input("Enter password ")

    # Uncomment it if u r running it for the first time
    # !!!!!!DON'T FORGET TO COMMENT THEM BACK ONCE U HAVE
    # RAN THIS PROGRAM ONCE!!!!!!!!!!
    #write_key()
    # <----Till here
    key = load_key()

    # uncomment it if u r running it for the first time
    # !!!!!!DONT FORGET TO COMMENT THEM BACK ONCE U HAVE
    # RAN THIS PROGRAM ONCE!!!!!!!!!!
    #encrypt_file("Whirlybird.txt", key)
    # <----Till here

    decrypt_file("Whirlybird.txt", key)

    f1 = open("Whirlybird.txt", "a")
    f1.write(f"{i}{pwd}\n")
    f1.close()

    encrypt_file("Whirlybird.txt", key)


def display():
    i = 1
    f1 = open("acc.txt", "r")
    for a in f1:
        print(f"{i}. {a}")
        i += 1
    f1.close()


def read():
    display()
    acc_choice = int(input("Enter the serial number of account "))

    key = load_key()

    decrypt_file("Whirlybird.txt", key)

    f1 = open("Whirlybird.txt", "r")

    for a in f1:
        if int(a[0]) == acc_choice:
            print(a[1:])
    f1.close()

    encrypt_file("Whirlybird.txt", key)


while True:
    tk.Tk().withdraw()

    userPassword = tkinter.simpledialog.askstring("WhirlyBird: The Password Manager", "Enter Master Password:", show='*')
    # Uncomment the lines below if you are running it for first time.
    # !!!!!!!!!!DON'T FORGET TO COMMENT THEM BACK ONCE U HAVE
    # RAN THIS PROGRAM ONCE!!!!!!!!!!
    #f = open("Whirlybird.txt", "x")
    #f.close()
    #f = open("acc.txt","x")
    #f.close()
    # <------Till here
    if userPassword == "Aires":
        print("Access granted\n")
        while True:
            #top = tk.Tk
            #label = Tk.Message(top, tetxvariable = "Select your opertaion", relief = tk.RAISED)
            #label.pack()
            #top.mainloop()

            #label = top.Message()
            print("\nMenu\n1.Add\n2.Read\n")
            choice = int(input("Enter choice number "))

            if choice == 1:
                add()
            else:
                read()

            ch = input("Do u want to continue?(y/n) ")
            if ch == 'y' or ch == 'Y':
                pass
            else:
                exit()
    else:
        if messagebox.askretrycancel("WhirlyBird: The Password Manager", "Wrong Password. Do you want to retry?"):
            pass
        else:
            exit()