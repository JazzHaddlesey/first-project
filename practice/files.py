
# file1 = open("example.txt", "r")

# var1 = file1.readlines()

# file1.close()




# file = open("filename.txt", "r")

# outfile = ""

# for line in range(1, 10):
#     if line % 2 == 0:
#         outfile += file.readline()
#     else:
#         file.readline()

# file = open("filename.txt", "w")
# file.write(outfile)
# file.close()

# print(outfile)







with open("teams.txt", "w") as file1:
    file1.write("Miami Dolphins\nManchester United\nRaiders\nRangers\nChelsea")
    
with open("teams.txt", "r") as file1:
    list1 = file1.readlines()
    
for line in list1:
    if list1.index(line) == 0 or list1.index(line) == 3:
      print(line)


