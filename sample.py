import numpy as np

# https://arxiv.org/pdf/1309.1541.pdf

D = 100
y = np.random.randn(D) 

u = np.sort(y)[::-1]
arg_u = np.argsort(y)[::-1]

for i in range(40):
    print(u[i], y[arg_u[i]])

rho = 0
for j in range(D):
    if u[j] + 1/(j+1)*(1 - np.sum(u[0:j+1])) > 0:
        rho = j+1
lambda_val = 1.0 / rho * (1 - np.sum(u[0:rho]))

x = np.zeros([D])
for i in range(D):
    x[i] = max(y[i] + lambda_val, 0)
print(np.sum(x))