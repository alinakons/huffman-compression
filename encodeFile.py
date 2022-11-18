import os
from bitarray import bitarray
arr = bitarray(endian='little')


def huffman_encode(filename, huffman_code_dict):
    file = open(filename, 'r')
    encoded_file = open(os.path.splitext(filename)[0]+"_encoded.txt", 'w+b')
    while 1:
        # read by character
        char = file.read(1)
        if not char:
            break
        arr.encode(huffman_code_dict, char)

    with open(os.path.splitext(filename)[0]+"_encoded.txt", 'wb') as fh:
        arr.tofile(fh)
    print(arr.padbits)
    print(arr.nbytes)
    return os.path.splitext(filename)[0]+"_encoded.txt"
    file.close()
    encoded_file.close()


