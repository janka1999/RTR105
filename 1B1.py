
#SIN un COS funkcijas
#print(vars())

import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
#print(vars())

from numpy import cos, linspace, sin
#print(vars())

#x = linspace(0, 7, 70) #solis = (7-0)/(70-1)
x = linspace(0, 4, 11) # solis = (4-0)/(11-1)
y0 = cos(x)
y1 = sin(x)
#print(vars())

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Funkcija $cos(x)$ un $sin(x)$")
plt.plot(x, y0, "bo")
plt.plot(x, y1, "go")
plt.plot(x, y0, color = "#FF0000")
plt.plot(x, y1, color = "#FFFF00")
plt.plot(x,y1)
plt.legend(["$cos(x)$", "$sin(x)$", "$cos(X)$", "$sin(x)$"])
plt.show()

