import numpy as np
import pandas as pd
import math

def activation_func(x, choice):
    if choice == 1:
        return 1 / (1 + math.e ** -x)
    elif choice == 2:
        return (2 / (1 + math.e ** -x)) - 1
    elif choice == 3:
        return math.tanh(x)
    elif choice == 4:
        return max(0, x)

def activation_derivative(o, choice):
    if choice == 1:
        return o * (1 - o)
    elif choice == 2:
        return 0.5 * (1 - o ** 2)
    elif choice == 3:
        return 1 - o ** 2
    elif choice == 4:
        return 1 if o > 0 else 0

def calculate_delta_rule(weights, table, targets, alpha, inputs, activation_choice):
    weights = np.array(weights)
    table = np.array(table)
    iteration = 0
    while True:
        nets, outputs, errors = [], [], []
        new_weights = weights.copy()
        for i in range(inputs):
            net = np.dot(weights, table[i])
            o = activation_func(net, activation_choice)
            o_derivative = activation_derivative(o, activation_choice)
            error = (targets[i] - o) * o_derivative
            new_weights = new_weights + alpha * error * np.array(table[i])

        nets.append(net.item())
        outputs.append(o)
        errors.append(error)

        if all(round(e, 6) == 0 for e in errors):
            print("\nTraining Converged!")
            break

        print(f"\nIteration {iteration + 1}:")
        df = pd.DataFrame({
            "Net": nets,
            "Output (o)": outputs,
            "Target (o_)": targets,
            "Error (o_ - o)": errors
        })
        print(df)
        print("Updated Weights:", new_weights)
        iteration += 1
        weights = new_weights.copy()
        print("\nFinal Updated Weights:", weights)

def delta_training():
    inputs = int(input("Enter no. of inputs: "))
    samples = int(input("Enter no. of samples: "))
    print("Enter initial weights separated by spaces: ", end="")
    weights = list(map(float, input().split()))
    if len(weights) != samples:
        print(f"Error: Please enter exactly {samples} weights.")
        return
    table = []
    print(f"\nEnter {samples} values for each of the {inputs} inputs:")
    for i in range(inputs):
        values = list(map(float, input(f"Enter {samples} values for input {i+1} (space-separated): ").split()))
    if len(values) != samples:
        print(f"Error: Please enter exactly {samples} values for input {i+1}.")
        return
    table.append(values)
    print("\nEnter the desired output (targets) separated by spaces: ", end="")
    targets = list(map(float, input().split()))
    if len(targets) != inputs:
        print(f"Error: Please enter exactly {inputs} target values.")
        return

    print("\nChoose an activation function:")
    print("1.) Unipolar Sigmoid\n2.) Bipolar Sigmoid\n3.) Tanh\n4.) ReLU")
    activation_choice = int(input("Enter function type (1-4): "))
    alpha = float(input("\nEnter the learning rate (alpha): "))
    calculate_delta_rule(weights, table, targets, alpha, inputs, activation_choice)

if __name__ == "__main__":
    delta_training()