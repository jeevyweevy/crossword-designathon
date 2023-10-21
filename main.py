import crossword
import random
import string

from pprint import pprint


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



def main():
    with open("dictionary", "r") as file:
        terms = file.readlines()
    terms = [term.strip() for term in terms]


    words = random.sample(terms, 10)
    for word in words:
        print (word)




if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
