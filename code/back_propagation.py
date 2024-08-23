import numpy as np


# Initialize the weights and bias
def initialize_parameters():
    weights = np.array([0.0])
    bias = np.array([4.0])
    return weights, bias


# Define the mean squared error loss function
def mse_loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


# Define the derivative of the mean squared error loss function
def mse_loss_derivative(y_true, y_pred):
    return -2 * (y_true - y_pred)


# Perform forward propagation
def forward_propagation(x, weights, bias):
    return x * weights + bias


# Perform backward propagation and update parameters
def backward_propagation(x, y_true, y_pred, weights, bias, learning_rate):
    dW = np.sum(mse_loss_derivative(y_true, y_pred) * x)
    dB = np.sum(mse_loss_derivative(y_true, y_pred))

    weights -= learning_rate * dW
    bias -= learning_rate * dB

    return weights, bias


# Train the model using backpropagation
def train(x_train, y_train, epochs, learning_rate):
    weights, bias = initialize_parameters()

    for epoch in range(1, epochs + 1):
        y_pred = forward_propagation(x_train, weights, bias)
        loss = mse_loss(y_train, y_pred)

        weights, bias = backward_propagation(
            x_train, y_train, y_pred, weights, bias, learning_rate
        )

        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {loss}, Weights: {weights}, Bias: {bias}")

    return weights, bias


# Test data
x_data = np.array([[-1], [0], [1], [2], [3]])
y_data = np.array([-3, -1, 1, 3, 5])

# Hyperparameters
learning_rate = 0.001
epochs = 1000

# Train the model
weights, bias = train(x_data, y_data, epochs, learning_rate)

print(f"Trained Weights: {weights}")
print(f"Trained Bias: {bias}")

# Predict new output
x_test = np.array([[5], [6]])
y_test = forward_propagation(x_test, weights, bias)

print(f"Predictions: {y_test}")
