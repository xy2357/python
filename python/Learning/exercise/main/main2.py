# class Rectangle:
#     length = None
#     width = None
#
# r1 = Rectangle()
# print(r1.__dict__)

# class Rectangle:
#     def __init__(self):
#         self.length = None
#         self.width = None
#
# r1 = Rectangle()
# print(r1.__dict__)

# print(isinstance(bool, str))
# print(type('bool'))
# class Microwave:
#     def __init__(self) -> None:
#         pass
# 
# smeg: Microwave = Microwave()

class Player:
    def __init__(self, hp):
        self.hp = hp


p1 = Player(20)
p2 = p1
p2.hp = 30
print(p1.hp)

