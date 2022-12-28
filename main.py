import csv
import json

PATH = "comments.json"

def comments():
    with open(PATH, 'r') as file:
        print(type(json.load(file)))

if __name__ == "__main__":
    comments()