
def PrintName():
    name = input("Enter your name: ")
    i = len(name)
    new_name = name[i:i]
    while i != 0:
        i = i-1
        new_name = new_name + name[i]
    print('Your backwards name is ' + new_name)
PrintName()

def FavNumSq(i):
    return i * i # favourite number squared
num = input("Enter your favourite number: ")

print(FavNumSq(int(num)))

class Engineers:
    #skill = "Problem Solver" # fixed class attribute
    def __init__(self, eng_name, eng_type, eng_exp):
        self.eng_name = eng_name # name of engineer
        self.eng_type = eng_type # engineer type
        self.eng_exp = eng_exp # years of experience
    def GetName(self):
        return self.eng_name
    def GetType(self):
        return self.eng_type
    def GetExp(self):
        return self.eng_exp
Eng01 = Engineers("Bob", "Civil", 5)
Eng02 = Engineers("Sheryl", "Electronic", 2)

def PrintEng(Engineer):
    print(Engineer.GetName(), end="")
    print(" is a " + Engineer.GetType() + " Engineer", end="")
    print(" with " + str(Engineer.GetExp()) + " years experience.")

PrintEng(Eng01)
PrintEng(Eng02)
#print("new")