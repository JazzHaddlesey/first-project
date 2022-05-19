
from budget import Budget

rent = Budget(600)
with open("rent.txt", "w") as file1:
    file1.write(str(rent.balance))
    
bills = Budget(150)
with open("billst.txt", "w") as file1:
    file1.write(str(bills.balance))

food = Budget(220)
with open("food.txt", "w") as file1:
    file1.write(str(food.balance))

entertain = Budget(125)
with open("enterrain.txt", "w") as file1:
    file1.write(str(entertain.balance))

cloth = Budget(80)
with open("cloth.txt", "w") as file1:
    file1.write(str(cloth.balance))
    
    


print("food; \n" +  (str(food)))

