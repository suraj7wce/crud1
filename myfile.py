# Creating a new file
file_path = "example.txt"
file = open(file_path, "w")

# Writing to the file
file.write("Hello, World!\n")
file.write("This is a sample file.\n")
file.write("Writing data to a file.")

# Closing the file
file.close()

# Reading from the file
file = open(file_path, "r")
content = file.read()
file.close()

# Displaying the file content
print(content)
