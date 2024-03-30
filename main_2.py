from Operators import *
from ComputationalGraph import ComputationalGraph
from PlaceHolder import placeholder
from Variable import Variable
from Sessions import Session
from Constant import Constant

def eq1():
    # AB + (BC * AD)        = add(matmul(A,B), matmul(matmul(B,C), matmul(A,D)))
    A = Variable([[1, 0], [0, -1]], "A")
    B = Variable([[1, 1], [2, 0]], "B")
    AB = matmul(A, B)
    C = Variable([[3, 4], [4, 1]], "C")
    BC = matmul(B, C)
    D = Variable([[5, 2], [3, 1]], "D")
    AD = matmul(A, D)
    BCAD = matmul(BC, AD)
    print(BCAD.__name__)
    z = add(AB, BCAD)
    BCAD = matmul(BC, AD)
    z = add(AB, BCAD)

    sessio = Session()
    output = sessio.run(z, dict())
    print(output)

def eq2():
    # A*A + 2 A*B + B*B     = add(mul(A,A), add(mul(2*A,B), mul(B,B)))
    a = Variable(5, "A")
    b = Variable(7, "B")
    c = Constant(2)
    aa = power(a, c)
    ab = mul(a,b)
    twoab = mul(c,ab)
    bb = power(b, c)
    z = add(aa, add(twoab, bb))
    sessio = Session()
    output = sessio.run(z, dict())

def eq3():
    # 2A - 3B - 2A          = sub(mul(c,a),add(mul(d,b),mul(c,a)))
    a = Variable(5, "A")
    b = Variable(7, "B")
    c = Constant(2)
    d = Constant(3)
    z = sub(mul(c,a),add(mul(d,b),mul(c,a)))
    sessio = Session()
    output = sessio.run(z, dict())
    print(output)

def eq4():
    # A^2          = sub(mul(c,a),add(mul(d,b),mul(c,a)))
    A = Variable([2,5], "A")
    c = Constant(2)
    z = power(A, c)
    sessio = Session()
    output = sessio.run(z, dict())
    print(output)

def eq5():
    # A^T                   = matTranspose(A)
    A = Variable([[1, 1], [-1, 1]], "A")
    z = matInversion([A])
    z = matmul(A, z)
    sessio = Session()
    output = sessio.run(z, dict())
    print(output)

def eq6():
    pass

def eq7():
    pass

def eq8():
    pass


# Create a new graph
ComputationalGraph().set_default()


# # Create variables
# A = Variable([[1, 0], [0, -1]])
# b = Variable([1, 1])

# # Create placeholder
# x = placeholder()

# # Create hidden node y
# y = matmul(A, x)

# # Create output node z
# z = add(y, b)

# sessio = Session()
# output = sessio.run(z, {x:[1,2]})
# print(output)

# A = Variable([[1, 0], [0, -1]], 'A')
# B = Variable([[1, 1], [2, 0]], 'B')
# AB = matmul(A, B)
# C = Variable([[3, 4], [4, 1]], 'C')
# BC = matmul(B, C)
# D = Variable([[5, 2], [3, 1]], 'D')
# AD = matmul(A, D)
# BCAD = matmul(BC, AD)
# z = add(AB, BCAD)

## Matrix
# eq1()       # AB + (BC * AD)        = add(matmul(A,B), matmul(matmul(B,C), matmul(A,D)))
## Scalar
eq2()       # A*A + 2 A*B + B*B     = add(mul(A,A), add(mul(2*A,B), mul(B,B)))
# eq3()           # 2A - 3B - 2A        = sub(mul(c,a),add(mul(d,b),mul(c,a)))
# Vector
# eq4()           # A^2                   = power(A,c)
# eq5()           # A^T                   = matTranspose(A)
# eq6()           # AA^(-1)
# eq7()           # 3 abs(A-B) - A
