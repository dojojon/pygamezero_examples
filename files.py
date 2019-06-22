
# write data to a file

file = open("data.txt", "w+")

file.write("hello world")

print(file.name)

file.close()

# read from a file

file = open("data.txt", "r")

lines = file.read()

print("Read this from the files:", lines)

file.close()

