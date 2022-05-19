from budget import Budget

def updateRent():
    with open("rent", 'w') as file1:
        file1.write(str(rent.balance))
        
def updateBills():
    with open("bills.txt", "w") as file1:
        file1.write(str(bills.balance))
        
def updateFood():
    with open("food", 'w') as file1:
        file1.write(str(food.balance))
        
def updateEntertain():
    with open("entertain", 'w') as file1:
        file1.write(str(entertain.balance))    
        
def updateCloth():
    with open("cloth", 'w') as file1:
        file1.write(str(cloth.balance))
        



with open("rent.txt", "r") as file1:
    var1 = int(file1.read())
rent = Budget(var1)

with open("bills.txt", "r") as file1:
    var1 = int(file1.read())
bills = Budget(var1)

with open("food.txt", "r") as file1:
    var1 = int(file1.read())
food = Budget(var1)

with open("entertain.txt", "r") as file1:
    var1 = int(file1.read())
entertain = Budget(var1)

with open("cloth.txt", "r") as file1:
    var1 = int(file1.read())
cloth = Budget(var1)



running = True

while running:
    control = input("1: edit budget")
    if control == "1":
        updateRent()
        updateBills()
        updateFood()
        updateEntertain()
        updateCloth()
    elif control == "0":
        running = False    
        
        