text = "This is to demonstrate file compression using Huffman coding"

def frequency_list():
    letter_freq = {}
    for c in range(0, len(text)):
        if letter_freq.__contains__(text[c]):
            letter_freq.update({text[c]: letter_freq.get(text[c]) + 1})
        else:
            letter_freq.update({text[c]: 0})
    print(letter_freq)
