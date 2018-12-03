import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from math import sqrt
from numpy import cos ** 2 (x/2), linspace

def f(x):
    return cos**2(x/2)

x = linspace(0, 4, 11)
print(x)
#y = sin(x)
y = f(x)
print(y)

legend[]

from mathplotlib import pyplot as plt
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Cosinus funkcija un taas atvasinaajumi")
plt.plot(x, y, "k")
legend.append("$scos**2(x/2)$ funkcija")

plt.plot(x, y, "go")
legend.append("$cos**2(x/2)$ funkcija(dazhi punkti)")
