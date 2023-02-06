# 3x2

A = [[1, 2],
     [3, 4],
     [5, 6]]
    
print('A')
for row in A:
    print(row)
    
def scalar_product_loop(k, A):
    B = []
    for row in A:
        r = []
        for a in row:
            r.append(k*a)
        B.append(r)
    return B

def scalar_product(k, A):
    return [[k*a for a in row] for row in A]

B = scalar_product(10, A)

print('B = 10A')
for row in B:
    print(row)


def addition(A, B):
    m = len(A)
    n = len(A[0])
    return [
        [A[i][j] + B[i][j] for j in range(n)]
          for i in range(m)]

C = addition(A, B)

print('A + B')
for row in C:
    print(row)



