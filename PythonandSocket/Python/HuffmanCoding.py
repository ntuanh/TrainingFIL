from collections import Counter

def normal_bits(news):
    res = 0
    while 2**res < len(news) :
        res += 1
    return 2**res

def HuffmanEncoder(news):
    # news = "BUNCHANGONQUA"
    # print(f"message : {news}")

    # Count frequency and sort
    cnt_fre = dict(sorted(Counter(news).items(), key=lambda item: item[1], reverse=True))
    # print(f"Frequency of characters: {cnt_fre}")

    # Initialize Huffman coding dictionary
    codingHuffman = {key: '' for key in cnt_fre}

    cnt_step = 0

    while len(cnt_fre) > 1:
        # Extract two least frequent characters
        keys = list(cnt_fre.keys())
        values = list(cnt_fre.values())

        key1, key2 = keys[-1], keys[-2]  # Smallest two elements
        val1, val2 = values[-1], values[-2]

        # Update Huffman encoding
        for char in key1:
            codingHuffman[char] += '0'
        for char in key2:
            codingHuffman[char] += '1'

        # Remove two smallest elements and add merged node
        cnt_fre.pop(key1)
        cnt_fre.pop(key2)

        cnt_fre[key2 + key1] = val1 + val2
        cnt_fre = dict(sorted(cnt_fre.items(), key=lambda item: item[1], reverse=True))

        # print(f"Step [{cnt_step}]: {cnt_fre}")
        cnt_step += 1

    # Display Huffman codes
    # print("\nResult:")
    # for key, value in codingHuffman.items():
    #     print(f"{key}: {value}")

    # Encode the input string
    # print("\nHuffman Encoding:")
    encoded_string = ''.join(codingHuffman[char] for char in news)
    # print(encoded_string)

    # print(f"Save { - normal_bits(news) + len(encoded_string)} bits ")
    return encoded_string



