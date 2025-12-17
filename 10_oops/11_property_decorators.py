class TeaLeaf:

    def __init__(self,age):
        self.age = age
        
    @property
    def age(self): 
        print("age",self._age)
        return self._age + 2
    
    @age.setter
    def age(self, age):
        print("aaage",age)
        if age < 0:

            raise ValueError("Age cannot be negative.")
        else :
            self._age = age

tea_leaf = TeaLeaf(10)
print(tea_leaf.age)  # Output: 12

# tea_leaf2 = TeaLeaf(-1111)
# print(tea_leaf2.age)