node = [[] for _ in range(6)]
OUTPUT = [3, 5]
class ConvolutionalEncoder :
    def __init__(self , chars):
        # setup by hand
        self.chars = chars
        node[1] = ['A', 'B']
        node[2] = ['1', 'C']
        node[3] = ['2', 'D']
        node[4] = ['A', 'C']
        node[5] = ['4', 'D']

    def display(self):
        print("Hello worlddd")
        print(self.chars[get_indice('A')])

    def compute(self):
        com_node = [0]*6
        for i in range(1 , 6 , 1):
            print("node" , i)
            for char in node[i]:
                if char >= 'A' and char <= 'Z' :
                    print(f"Before res is  {com_node[i]} and {int(self.chars[get_indice(char)])}")
                    com_node[i] = XOR(com_node[i], int(self.chars[get_indice(char)]))
                    print(f"Computed {com_node[i]}")
                else:
                    com_node[i] = XOR(com_node[int(char)] , com_node[i])
        print("RESULT")
        for node_i in OUTPUT:
            print(com_node[node_i] , end="")


def get_indice(x):
    return int(ord(x) - ord('A'))

def XOR(a , b):
    if a == b:
        return 0
    else :
        return 1

encoder = ConvolutionalEncoder("1001")
encoder.display()
encoder.compute()


