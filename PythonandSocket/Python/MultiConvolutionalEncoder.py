import numpy as np

mybits = '110011'
K = [5, 4]
c_original = [
    [23, 0],
    [35, 5],
    [0, 13]]

def octan2binary(n , capa):
    res = list(str(bin(int(str(n), 8))[2:]))
    res = list(map(int , res))
    return [0] * (capa - len(res)) + res
def preprocess_c(c_original , K):
    return [[octan2binary(c_original[i][j], K[j]) for j in range(len(c_original[i]))] for i in range(len(c_original))]

def calculate(c, m):
    result = []
    for row in c:
        res = sum(np.dot(np.array(m[j]), np.array(row[j]).T) for j in range(len(row))) % 2
        result.append(res)
    return result

def ConvolutionalEncoder(c , mybits ):
    m = [[0] * k for k in K]
    result = []
    
    while mybits:
        for i in range(len(K)):
            if mybits:
                m[i] = [int(mybits[0])] + m[i][:-1]
                mybits = mybits[1:]

        result.extend(calculate(c, m))

    return "".join(map(str, result))

c = preprocess_c(c_original, K)
print(ConvolutionalEncoder(c , mybits))

