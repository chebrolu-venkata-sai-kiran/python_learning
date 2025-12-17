# method resolution order

class A:
    label ="A: Base Class"

class B(A):
    label = "B: Inherited Class"

class C(A):
    label = "C: Inherited Class"

class D(B,C):
    #label = "D: Inherited Class"
    pass

cup = D()

print(cup.label)
