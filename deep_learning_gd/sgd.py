from template import *
import math

def gradient_descent(
    gradient, start, learn_rate, n_iter=50, tolerance=1e-06
):
    vector = start
    for _ in range(n_iter):
        diff = -learn_rate * gradient(vector)
        if np.all(np.abs(diff) <= tolerance):
            break
        vector += diff
    return vector

#create sample linear data


x = [1, 2, 3, 4]
y = [math.sin(z) for z in x]

dense1 = Layer_Dense(1,2)
activation1 = Activation_ReLU()

dense2 = Layer_Dense(2, 1)
activation2 = Activation_ReLU()

while True:
    dense1.forward(x)
    activation1.forward(dense1.output)

    dense2.forward(activation1.output)
    activation2.forward(dense2.output)

    #TODO implement loss function