import os

DATA_FILE = "password.txt"


def init():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            file.write("")


def read_data():
    with open(DATA_FILE, "r") as file:
        return file.readlines()


def write_data(data):
    with open(DATA_FILE, "w") as file:
        file.writelines(data)


def append_data(data):
    with open(DATA_FILE, "a") as file:
        file.write(data + "\n")
