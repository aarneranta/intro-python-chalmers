xs = [(x, x**3) for x in range(10) if x % 2 == 0]
print(xs)

xs = []
for x in range(10):
    if x % 2 == 0:
        xs.append((x, x**3))

print(xs)

