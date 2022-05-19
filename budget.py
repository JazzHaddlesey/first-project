
'''
“Create a Budget class that can instantiate objects 
based on different budget categories like food, clothing, and entertainment.
These objects should allow for depositing and withdrawing funds from each category,
as well computing category balances and transferring balance amounts between categories”
'''

# class Balance():
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

# class Category():
#     def __init__(self, rent, food, cloth, entertain):
#         self.rent = rent
#         self.food = food
#         self.cloth = cloth
#         self.entertain = entertain 
        
#     def deposit():
        
        
        
        
#     def withdraw():
        
        
        
        
# budg1 = Category(600, 200, 50, 120)

# print(budg1.rent)


class Budget():
    def __init__(self, balance):
        self.balance = balance
        
    
    def __repr__(self):   
        return f"Current budget: , {self.balance}"
        
        
    def withdraw(self, amount):
        self.balance -= amount
        return amount
        
    def deposit(self, amount):
        self.balance += amount
        return "Deposited: ", amount 

        
        
       