data = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 10), (6, 12), (7, 14), (8, 17), (9, 18)]
x_n = 10

def f(x):
  return w*x + b

def J(w):
  return sum((f(x) - y)**2 for x, y in data)

def dJ_dw(w):
  return sum(2*x*(w*x + b - y) for x, y in data)

def dJ_db(w):
  return sum(2*(w*x + b - y) for x, y in data)

w, b = 0, 0
alpha = 0.001
estimate = 0
w_l = []
b_l = []
e_l = []
print(w, b)
for i in range (100):
  value = J(w)
  gradient_w = dJ_dw(w)
  gradient_b = dJ_db(b)
  w = w - alpha*gradient_b
  b = b - alpha*gradient_b
  estimate = f(x_n)
  print('estimate = {estimate}, w= {w}, b= {b}'.format(w=w, b=b, estimate=estimate))
  e_l.append(estimate)
  w_l.append(w)
  b_l.append(b)


import matplotlib.pyplot as plt

X =[x for x, y in data]
Y = [y for x, y in data]

print(X, Y, e_l)

plt.scatter(range(len(e_l)), e_l)
plt.show()
