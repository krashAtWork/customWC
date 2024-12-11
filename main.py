# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(prog = 'ccwc', description ="Argument for custom wc")
parser.add_argument('filename', type=str, help='The file to be processed')
parser.add_argument('-c', '--count', action ='store_true', help="return number of bytes in the file")
parser.add_argument('-l', '--lines',action ='store_true', help="return number of lines in the file")
parser.add_argument('-w', '--words',action ='store_true', help="return number of words in the file")
parser.add_argument('-m', '--characters', action = 'store_true', help="return number of characters in the file")


parser.add_argument_group()
args = parser.parse_args()

def getAllResults():
    file_bytes = os.path.getsize(file_path)
    with open(file_path, encoding='utf-8') as file:
        lines = file.readlines()
        file_lines = len(lines)
        wordCount = 0
        charCount = 0
        for line in lines:
            if line.strip() != "":
                # print(line.strip())
                lineWords = line.strip().split(" ")  # not numbers
                wordCount += len(lineWords)
                for words in lineWords:
                    charCount += len(words)

        # charCount = 0
        # for line in lines:
        #     if line.strip() != "":
        #         # print(line.strip())
        #         lineWords = line.strip().split(" ")  # not numbers
        #         for words in lineWords:
        #             charCount += len(words)

    return file_bytes, file_lines, wordCount, charCount



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Arguments passed in as strings
    file_path = args.filename
    file_bytes, file_lines, wordCount, charCount = getAllResults()

    if args.count:
        # Open the file in binary read mode
        # Display the bytes
        print(f"{file_bytes} {file_path}")

    elif args.lines:
        print(f"{file_lines} {file_path}")

    elif args.words:
        # file_path = Path(file_path)
        # content = file_path.read_text()
        # print(content)
        print(f"{wordCount} {file_path}")

        # with open(file_path, 'r', encoding='utf-8') as file:
        #     lines = file.readlines()
        #     wordCount = 0
        #     for line in lines:
        #         if line.strip() != "":
        #             # print(line.strip())
        #             lineWords = line.strip().split(" ")  # not numbers
        #             wordCount += len(lineWords) print(f"{wordCount} {file_path}")

    elif args.characters:
        # with open(file_path, 'r', encoding='utf-8') as file:
        #     lines = file.readlines()
        #     charCount = 0
        #     for line in lines:
        #         if line.strip() != "":
        #             # print(line.strip())
        #             lineWords = line.strip().split(" ")  # not numbers
        #             for words in lineWords:
        #                 charCount += len(words)
            print(f"{charCount} {file_path}")

    elif not args.characters and not args.words and not args.lines and not args.count:
        print(f" {file_lines} {wordCount} {charCount} {file_path}")

    # elif cmd_option == "":
    #     cmd_option == "-c -l  -w"
    #
    #         # listWords = file_words.split(" ")
    #         # file_words = len(listWords)
    #         # print(f"{file_words} {file_path}")
    #
    #         # print(f"{file_words} {file_path}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
