class Bad:
    items = []  # Yomon! Mutable class atribut

b1 = Bad()
b2 = Bad()
b1.items.append(1)
print(b2.items)  # [1] ← kutilmagan!

class Good:
    def __init__(self):
        self.items = []  # Yaxshi! Har instance uchun alohida

g1 = Good()
g2 = Good()
g1.items.append(1)
print(g2.items)  # [] ← to'g'ri!
