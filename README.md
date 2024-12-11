"# customWC" 

Demonstration of using argparse

In this customwc project, if you have any text file. and you supply its path:

python main.py test.txt [-l, -m, -c, -w]
you can get:
parser.add_argument('-c', '--count',help="return number of bytes in the file")
parser.add_argument('-l', '--lines',help="return number of lines in the file")
parser.add_argument('-w', '--words', help="return number of words in the file")
parser.add_argument('-m', '--characters', help="return number of characters in the file")

Learnt how to use arg parse on this

