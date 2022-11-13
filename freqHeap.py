import heapq
import frequency_list
from node import Node
from huffmanTree import HuffmanTree
import  tkinter
# Huffman Coding in python
from tkinter.filedialog import askopenfilename
filetypes = (
    ('Text files', '*.TXT'),
    ('All files', '*.*'),
)

filename = askopenfilename(
    filetypes=filetypes,)

text_file = open(filename, "r")
text = text_file.read()
text_file.close()
print(text)

#text = "aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffff"
letter_freq = frequency_list.generate_frequency_dictionary(text)
print(letter_freq)
li = []
heapq.heapify(li)
for value in letter_freq.values():
    heapq.heappush(li, value)
print(li)
root = li[0].generate_huffmantree(li)
print(root)


def print_nodes(root):
    if root.left is not None:
        print_nodes(root.left)
    if root.right is not None:
        print_nodes(root.right)
    print({root.get_frequency()}, {root.get_data()})

def generate_codes(root, str1):
    str1 = str1 + root.code
    if root.left is not None:
        #str1 = str1 + "0"
        generate_codes(root.left, str1)
    if root.right is not None:
        #str1 = str1 + "1"
        generate_codes(root.right, str1)
    if root.get_data() is not None:
        print({root.get_frequency()}, {root.get_data()}, str1)
        str1 = ""

str1 = ""
print_nodes(root)
generate_codes(root,str1)














