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

def nor_gate(i, j):
    return mp([i, j], [-1, -1], 0)

def andnot_gate(i, j):
    return mp([i, j], [1, -1], 1)

def not_gate(i):
    return mp([i], [-1], 0)

def main():
    print("AND GATE")
    for i in [0, 1]:
        for j in [0, 1]:
            print(f"({i} AND {j}) = ", and_gate(i, j))

    print("\nNAND GATE")
    for i in [0, 1]:
        for j in [0, 1]:
            print(f"({i} NAND {j}) = ", nand_gate(i, j))

    print("\nOR GATE")
    for i in [0, 1]:
        for j in [0, 1]:
            print(f"({i} OR {j}) = ", or_gate(i, j))

    print("\nNOR GATE")
    for i in [0, 1]:
        for j in [0, 1]:
            print(f"({i} NOR {j}) = ", nor_gate(i, j))
            
    print("\nANDNOT GATE")
    for i in [0, 1]:
        for j in [0, 1]:
            print(f"({i} ANDNOT {j}) = ", andnot_gate(i, j))

    print("\nNOT GATE")
    for i in [0, 1]:
        print(f"(NOT {i}) = ", not_gate(i))
    
if __name__ == "__main__":
    main()
