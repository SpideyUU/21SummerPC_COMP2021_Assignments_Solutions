import os.path
import sys


def main():
    key_words = {"and", "as", "assert", "break", "class",
                 "continue", "def", "del", "elif", "else",
                 "except", "False", "finally", "for", "from",
                 "global", "if", "import", "in", "is", "lambda",
                 "None", "nonlocal", "not", "or", "pass", "raise",
                 "return", "True", "try", "while", "with", "yield"}

    filename = input("Enter a Python filename: ").strip()

    if not os.path.isfile(filename):
        print("File", filename, "does not exist")
        sys.exit()

    readfile = open(filename, "r")
    words = readfile.read().split()
    count = 0
    count_keyword = {}
    for word in words:
        if word in key_words:
            count += 1
            count_keyword[word] = count

    for key in count_keyword:
        print(key + ":" + str(count_keyword[key]))

    readfile.close()


main()
