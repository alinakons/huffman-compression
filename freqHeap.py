import heapq

import decodeFile
import frequency_list
import huffmanCode
import encodeFile

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



str1 = ""
print_nodes(root)
print(huffmanCode.generate_codes(root, str1))
encoded_file = encodeFile.huffman_encode(filename, huffmanCode.generate_codes(root, str1))
decodeFile.huffman_decode(encoded_file, huffmanCode.generate_codes(root, str1))















