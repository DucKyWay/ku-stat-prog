C = [39.85, 25, 32]

F = []
for temp in C:
    F.append((9/5)*temp + 32)
print(F)

K = []
for temp in C:
    K.append(temp + 273.15)
print(K)

for i in range(len(C)):
    print(f"{C[i]} °C = {F[i]} °F = {K[i]} °K")