import numpy as np
import matplotlib.pyplot as plt

# Define the sigmoid function
def sigmoid(x):
    return np.sinh(x)
    # return 1 / (1 + np.exp(-x))

# Generate a range of values for x
x = np.linspace(-10, 10, 1000)

# Calculate the sigmoid values
y = sigmoid(x)

# Plot the sigmoid function
plt.plot(x, y, label="Sigmoid Function", color="r")
plt.title("Sigmoid Function Plot")
plt.xlabel("x")
plt.ylabel("Sigmoid(x)")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()
