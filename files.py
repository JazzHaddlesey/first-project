
# file1 = open("example.txt", "r")

# var1 = file1.readlines()

# file1.close()

file = open("filename.txt", "r")

outfile = ""

for line in range(1, 10):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()

file = open("filename.txt", "w")
file.write(outfile)
file.close()

print(outfile)
