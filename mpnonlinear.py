import math

def mp(inputs, weights, threshold):
    sum_w = sum(i*w for i, w in zip(inputs, weights))
    return 1 if sum_w >= threshold else 0

def and_gate(i, j):
    return mp([i, j], [1, 1], 2)

def nand_gate(i, j):
    return mp([i, j], [-1, -1], -1)

def or_gate(i, j):
    return mp([i, j], [1, 1], 1)

def xor_gate(i, j):
    nand_o = nand_gate(i, j)
    or_o = or_gate(i, j)
    return and_gate(nand_o, or_o)

def xnor_gate(i, j):
    return not_gate(xor_gate(i, j))


def not_gate(i):
    return mp([i], [-1], 0)

def main():
    print("XOR GATE")
    for i in [0, 1]:
        for j in [0, 1]:
            xor_o = xor_gate(i, j)
            for k in [0, 1]:
                print(f"({i} XOR {j} XOR {k}) = ", xor_gate(xor_o, k))

    print("\nXNOR GATE")
    for i in [0, 1]:
        for j in [0, 1]:
            print(f"({i} XNOR {j}) = ", xnor_gate(i, j))


    
if __name__ == "__main__":
    main()
