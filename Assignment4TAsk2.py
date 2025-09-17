file_data = input("Enter text to write to the file: ")
with open('output.txt',"w") as file:
    file.write(file_data)
print("Data successfully written to output.txt")

file_data = input("Enter additional text to append: ")
with open('output.txt',"a") as file:
    file.write("\n")
    file.write(file_data)
print("Data successfully appended to output.txt")

with open("output.txt","r") as file:
    print("Final content of output.txt:")
    print(file.read())