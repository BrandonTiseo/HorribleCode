class Pokemon():
    def __str__(self):
        return f"{self.string}({self.ptype})\nHealth: {self.points} hp\n "
    def __init__(self, name, points, dpts, ptype):
        self.string = name
        self.points = points
        self.dpts = dpts
        self.ptype = ptype
    def __init__(self):
            self.string = ""
            self.points = 100
            self.dpts = 10
            self.ptype = "normal"
    def func1(p1, p):
        p.health -= p1.dpts
        print(f"Dealt {p1.dpts} damage to {p.name}!")
    def funct1(this):
        num = 20
        this.points += num
        print(f"{this.string} healed for {num}!")
    def func2(me):
        num = me.dpts / (me.points * 3)
        for i in range(me.dpts):
            num += i + 4
        str = me.string.split(".")
        me.funct1()  
class type3(Pokemon):
    def __init__(self):
        super().__init__("Torchic", 150, 60, "Fire")
class type1(Pokemon):
    def __init__(self):
        super().__init__("Mudkip", 200, 40, "Water")
class type2(Pokemon):
    def __init__(self):
        super().__init__("Treecko", 300, 20, "Grass")
def strt():
    m1 = type2()
    p2 = type3()
    num2 = -1
    while((m1.points > 0 and p2.points > 0) and num2 != 3):
        print(f"You: {m1}")
        print(f"Enemy: {p2}")
        num2 = int(input("What would you like to do?(1:Attack, 2:Heal, 3:Leave):"))
        if(num2 == 1):
            m1.func1(p2)
        elif(num2 == 2):
            m1.func2()
        else:
            print("INVALID INPUT")
            continue
        p2.func1(m1)
    if(num2 == 3):
        print("You Ran Away")
    else:
        if(m1.points <= 0):
            p3 = p2
        else:
            p3 = m1
        print(f"{p3.string} won the pokemon battle!")
strt()