#x = [1, 2, 3, 4, 5]
#y = [3, 5, 7, 9, 11]

#w = 0.5
#b = 0.1

outputs_list = []

#lr = 0.01

def gradient_w(x, y_actual, y_predicted):
    return 2 * (y_predicted - y_actual) * x

def gradient_b(y_actual, y_predicted):
    return 2 * (y_predicted - y_actual)

def update_weight(w, lr, x, y_actual, y_predicted):
    return w - (lr * gradient_w(x, y_actual, y_predicted))

def update_bias(b, lr, y_actual, y_predicted):
    return b - (lr * gradient_b(y_actual, y_predicted))

#num_epochs = 5
#y_predicted = 0

def do_sgd(x, y, num_epochs=5, w=0.5, b=1, lr=0.01):
    for _ in range(num_epochs):
        for i in range(len(x)):
            y_predicted = x[i] * w + b
            w = update_weight(w, lr, x[i], y[i], y_predicted)
            b = update_bias(b, lr, y[i], y_predicted)
        outputs_list.append((w, b))
        #print(f"Epoch = {_}:\n{w:.4f}, {b:.4f}\n")
    return outputs_list