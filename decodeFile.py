import os
from bitarray import bitarray
arr = bitarray(endian='little')


def huffman_decode(filename, huffman_code_dict):
    decoded_file = open(os.path.splitext(filename)[0].split('_')[0]+"_decoded.txt", 'w')
    with open(filename, 'rb') as fh:
        arr.fromfile(fh)
    arr.decode(huffman_code_dict)
    print(arr)
    decoded_file.close()
