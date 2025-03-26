#setup
K = 3
G = ['111', '101']


class ConvolutionalEncoder:
    def __init__(self , input_bits):
        # setup by hand
        self.input_bits = input_bits

    def compute(self):
        for gen in G :
            res = 0
            for i in range(len(gen)):
                if gen[i] == '1':
                    res = XOR(res , int(self.input_bits[i]))
            print(res , end='')


def compute_bits(bits):
    bits = '0'*(K - 1) + bits
    for i in range(len(bits) - K + 1):
        ConvolutionalEncoder(bits[i : i + K][::-1]).compute()

def XOR(a , b):
    return 0 if a == b else 1

compute_bits('1100')


