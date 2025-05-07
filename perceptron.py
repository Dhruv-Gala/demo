import numpy as np
import pandas as pd

def activation_function(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0

def calculate_table(table, targets, alpha, weights, bias, new_weights, new_bias, nets, outputs):
    for i in range(len(table)):
        net = 0
        for j in range(len(table[0])):
            net = net + table[i][j] * weights[j]
        nets[i] = net + bias
        output = activation_function(nets[i])
        outputs[i] = output

        if targets[i] != output:
            for j in range(len(new_weights[0])):
                new_weights[i][j] = weights[j] + alpha * (targets[i] - output) * table[i][j]
                weights[j] = new_weights[i][j]
            new_bias[i] = bias + alpha * (targets[i] - output)
            bias = new_bias[i]
        else:
            for j in range(len(new_weights[0])):
                new_weights[i][j] = weights[j]
            new_bias[i] = bias

    return new_weights, new_bias, nets, outputs
    


def perceptron():
    inputs = int(input("Enter no.of inputs: "))
    samples = int(input("Emter no.of samples: "))

    table = [list(map(int, input(f"Enter sample {i+1}: ").split())) for i in range(samples)]
    targets = [ int(input(f"Enter target {i+1}: ")) for i in range(samples)]

    alpha = int(input("Enter alpha: "))
    epoches = int(input("Enter epoch: "))

    weights = np.zeros(inputs, dtype=int)
    bias = 0

    new_weights = np.zeros((samples, inputs), dtype=int)
    new_bias = np.zeros(samples, dtype=int)
    nets = np.zeros(samples, dtype=int)
    outputs = np.zeros(samples, dtype=int)

    for epoch in range(epoches):
        new_weights, new_bias, nets, outputs = calculate_table(table, targets, alpha, weights, bias, new_weights, new_bias, nets, outputs)

        data = []
        for i in range(samples):
            row = {}
            for j in range(inputs):
                row[f'x{j+1}'] = table[i][j]
            row['Target'] = targets[i]
            row['Yin (Net)'] = nets[i]
            row['Output (Y)'] = outputs[i]
            for j in range(inputs):
                row[f'w{j+1}'] = new_weights[i][j]
            row['Bias'] = new_bias[i]
            data.append(row)
        
        df = pd.DataFrame(data)
        print(df)

if __name__ == "__main__":
    perceptron()
