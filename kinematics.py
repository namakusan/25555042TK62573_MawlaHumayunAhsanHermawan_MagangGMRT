import numpy as np

L1 = int(input("Panjang 1: "))
L2 = int(input("Panjang 2: "))
t1 = int(input("Rotasi 1: "))
t2 = int(input("Rotasi 2: "))

t1 = np.deg2rad(t1)
t2 = np.deg2rad(t2)

x = L1 * np.cos(t1) + L2 * np.cos(t1 + t2)
y = L1 * np.sin(t1) + L2 * np.sin(t1 + t2)

print(f"Final position: x = {x}, y = {y}")
