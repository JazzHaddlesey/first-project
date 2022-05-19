# user_funds = 10.31
# price = {10.20 : "Burger"}
# item_price = price["Burger"]

# if item_price < user_funds:
#     print("You have enough money!")
# if item_price == user_funds:
#     print("You have the precise amount of money")
# if item_price > user_funds:
#     print("Sorry you don't have enough money")

# def product(n):
#     total = 1
#     for i in n:
#         total *= i
#     return total

# print(product([4,4,5]))

# def is_prime(x):
#     if x < 2:
#         return False
#     else:
#         for n in range(2, x-1):
#             if x % n == 0:
#                 return f"False, is not prime"
#             return f"True, Is prime"
    
# print(is_prime(10))



# from operator import itemgetter


item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    n += 1
    for i in item_list:
        print(i)
        
    
print(item_list[4])


