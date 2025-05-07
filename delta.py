import math
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + math.exp(-x))
def sigmoid_derivative(x):
    return x * (1-x)
def dot_product(a,b):
    return sum([a[i] * b[i] for i in range(len(a))])

Xi = [
    [1, -2, 0, -1],
    [0, 1.5, -0.5, -1],
    [-1, 1, 0.5, -1]
]
d = [-1, -1, 1]  
w = [1, -1, 0, 0.5]

alpha = 0.1  
errors = []

print("Initial Weights:", w)

for i in range(len(d)):
    x = Xi[i]
    net_input = dot_product(w, x)
    y = sigmoid(net_input)
    error = d[i] - y
    y_derivative = sigmoid_derivative(y)

    delta_w = [alpha * error * y_derivative * xi for xi in x]
    w = [w[j] + delta_w[j] for j in range(len(w))]

    errors.append(abs(error))

    print(f"Iteration {i+1}:")
    print("Input:", x)
    print("Net Input:", net_input)
    print("Output (Sigmoid):", y)
    print("Error:", error)
    print("Weight Update:", delta_w)
    print("Updated Weights:", w)
    print("----------------------------------")

print("Final Weights:", w)
plt.plot(range(1, len(d) + 1), errors, marker='o', linestyle='-', color='r')
plt.xlabel('Iteration')
plt.ylabel('Absolute Error')
plt.title('Error Reduction Over Iterations')
plt.grid()
plt.show()
