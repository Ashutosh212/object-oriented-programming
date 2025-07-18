class Vault:
    def __init__(self, a = 0, b = 0, c = 0):
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self):
        return f"a: {self.a}, b: {self.b}, c: {self.c}"

    # Operator Overloading
    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        c = self.c + other.c
        return Vault(a,b,c)



ashu = Vault(15, 50, 40)
pope = Vault(50, 20, 30)

dpog = ashu + pope
print(dpog)