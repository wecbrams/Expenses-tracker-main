class A: 
    def __init__(self, a): self.a = a
    def __lt__(self, other): return "ob1 is less than ob2" if self.a < other.a else "ob2 is less than ob1"
    def __eq__(self, other): return "Both are equal" if self.a == other.a else "Not equal"
print(A(2).a, A(3).a, A(2) < A(3)); print(A(4).a, A(4).a, A(4) == A(4))