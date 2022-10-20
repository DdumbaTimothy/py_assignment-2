birthyear = 2002
def take3(name, birthyear, weight):
    today = 2022
    age = today-birthyear
    print("your age is", age)
    return age 

name = str(input("What is your name ?"))
if name == "":
    name = "keron"
weight = int(input("What is your weight?"))
print("you are",name, "your weight is", weight)