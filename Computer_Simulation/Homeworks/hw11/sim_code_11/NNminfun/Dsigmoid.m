function f = Dsigmoid(x)

f = sigmoid(x).*(1-sigmoid(x));
